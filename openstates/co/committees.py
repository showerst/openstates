from openstates.utils import LXMLMixin
from billy.scrape.committees import CommitteeScraper, Committee

COMMITTEE_URL = ("http://leg.colorado.gov/content/committees")


class COCommitteeScraper(CommitteeScraper, LXMLMixin):
    jurisdiction = "co"

    def scrape_page(self, link, chamber, term):
        page = self.lxmlize(link.attrib['href'])
        comName = link.text
        roles = {
            "Chair": "chair",
            "Vice Chair": "vice-chair"
        }
        committee = Committee(chamber, comName)
        committee.add_source(link.attrib['href'])

        for member in page.xpath('//div[@class="members"]/' +
                                 'div[@class="roster-item"]'):
            details = member.xpath('.//div[@class="member-details"]')[0]
            person = details.xpath('./h4')[0].text_content()
            # This page does random weird things with whitepace to names
            person = ' '.join(person.strip().split())
            if not person:
                continue
            role = details.xpath('./span[@class="member-role"]')
            if role:
                role = roles[role[0].text]
            else:
                role = 'member'
            committee.add_member(person, role)
        self.save_committee(committee)
        return

    def scrape(self, term, chambers):
        page = self.lxmlize(COMMITTEE_URL)
        # Actual class names have jquery uuids in them, so use
        # contains as a workaround
        comList = page.xpath('//div[contains(@class,' +
                             '"view-committees-overview")]')
        for comType in comList:
            header = comType.xpath('./div[@class="view-header"]/h3')[0].text
            if "House Committees" in header:
                chamber = 'lower'
            elif "Senate Committees" in header:
                chamber = 'upper'
            else:
                chamber = 'joint'
            for comm in comType.xpath('./div[@class="view-content"]' +
                                      '/table/tbody/tr/td'):
                link = comm.xpath('.//a')
                # ignore empty cells
                if link:
                    self.scrape_page(link[0], chamber, term)
