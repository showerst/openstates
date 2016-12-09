import re
import datetime
from collections import defaultdict

from billy.scrape.bills import Bill, BillScraper
from billy.scrape.votes import Vote
from .utils import build_legislators, legislator_name, db_cursor
from .legacyBills import NHLegacyBillScraper

from openstates.utils import LXMLMixin

body_code = {'lower': 'H', 'upper': 'S'}
code_body = {'H': 'lower', 'S': 'upper'}

bill_type_map = {
    'HB': 'bill',
    'SB': 'bill',
    'HR': 'resolution',
    'SR': 'resolution',
    'CACR': 'constitutional amendment',
    'HJR': 'joint resolution',
    'SJR': 'joint resolution',
}

# When a Committee acts Inexpedient to Legislate, it's a committee:passed:unfavorable ,
# because they're _passing_ a motion to the full chamber that recommends the bill be killed.
# When a Chamber acts Inexpedient to Legislate, it's a bill:failed
# The actions don't tell who the actor is, but they seem to always add BILL KILLED when the chamber acts
# So keep BILL KILLED as the first action in this list to avoid subtle misclassfication bugs.
# https://www.nh.gov/nhinfo/bills.html
action_classifiers = [
    ('BILL KILLED', ['bill:failed']),
    ('ITL', ['committee:passed:unfavorable']),
    ('OTP', ['committee:passed:favorable']),
    ('OTPA', ['committee:passed:favorable']),
    ('Ought to Pass', ['bill:passed']),
    ('Passed by Third Reading', ['bill:reading:3', 'bill:passed']),
    ('.*Ought to Pass', ['committee:passed:favorable']),
    ('.*Introduced(.*) and Adopted',
     ['bill:introduced']),    
    ('.*Introduced(.*) and (R|r)eferred',
     ['bill:introduced', 'committee:referred']),
    ('.*Inexpedient to Legislate', ['committee:passed:unfavorable']),
    ('Proposed(.*) Amendment', 'amendment:introduced'),
    ('Amendment .* Adopted', 'amendment:passed'),
    ('Amendment .* Failed', 'amendment:failed'),
    ('Signed', 'governor:signed'),
    ('Vetoed', 'governor:vetoed'),
]


def classify_action(action):
    for regex, classification in action_classifiers:
        if re.match(regex, action):
            return classification
    return 'other'


def extract_amendment_id(action):
    piece = re.findall(r'Amendment #(\d{4}-\d+[hs])', action)
    if piece:
        return piece[0]


def get_version_code(description):
    version_code = None

    if 'Introduced' in description:
        version_code = 'I'
    elif 'As Amended' in description and not '2nd committee' in description:
        version_code = 'A'
    elif 'As Amended' in description and '2nd committee' in description:
        version_code = 'A2'
    elif 'adopted by both bodies' in description:
        version_code = 'A'
    # Some document version texts exist in the DB, but are not used, so
    # they do not appear here.
    # Final version should have no code - returned as current version.

    return version_code

class NHBillScraper(BillScraper, LXMLMixin):
    jurisdiction = 'nh'

    def __init__(self, *args, **kwargs):
        super(BillScraper, self).__init__(*args, **kwargs)
        #self.cursor = db_cursor()
        self.legislators = {}
        self._subjects = defaultdict(list)

    def scrape(self, chamber, session):
        
        if int(session) < 2016:
            legacy = NHLegacyBillScraper(self.metadata, self.output_dir, self.strict_validation)
            legacy.scrape(chamber, session)
            # This throws an error because object_count isn't being properly incremented, 
            # even though it saves fine. So fake the output_names
            self.output_names = ['1']
            return
        

        list_url = 'http://www.gencourt.state.nh.us/bill_status/Results.aspx?q=1&txtsessionyear={}'.format(int(session))

        #page =   lxml.html.fromstring(requests.get(
        #list_url).text)
        page = self.lxmlize(list_url)

        # tr[count(*)=2]
        bills = page.xpath('//table[contains(@class,"ptable")][2]/tr[count(td)=2]')

        for row in bills:
            bill_id = row.xpath('string(td[1]/big)').strip()

            bill_title = row.xpath('td[2]/text()[normalize-space()]')[0].strip()

            bill = Bill(
                session,
                chamber,
                bill_id,
                bill_title)

            docket_url = row.xpath('td/a[starts-with(normalize-space(),"Bill Docket")]/@href')[0]

            self.scrape_actions(bill, docket_url)

            status_url = row.xpath('td/a[starts-with(normalize-space(),"Bill Status")]/@href')[0]

            bill.add_source(status_url)

            self.scrape_sponsors(bill, status_url)

            self.save_bill(bill)
    

    def scrape_actions(self, bill, url):
        page = self.lxmlize(url)

        action_rows = page.xpath('//td[@style="BORDER-BOTTOM: navy 1px solid; BORDER-LEFT: navy 1px solid; BORDER-TOP: navy 1px solid; BORDER-RIGHT: navy 1px solid"]/table/tr')

        for row in action_rows[1:]:
            action = row.xpath('string(td[3])')

            actor = row.xpath('string(td[2])')
            actor = code_body[actor]

            date = row.xpath('string(td[1])')
            date = datetime.datetime.strptime(date, '%m/%d/%Y')

            action_type = classify_action(action)
            bill.add_action(actor, action, date, action_type)


    def scrape_sponsors(self, bill, status_url):
        page = self.lxmlize(status_url)
        if page.xpath('string(//table[@id="drep"]/tr/td[1])'):
            sponsor = page.xpath('string(//table[@id="drep"]/tr/td[1])')
            bill.add_sponsor('primary', sponsor_name)
