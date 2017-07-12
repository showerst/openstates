import lxml.html
import datetime
from .legislators import TXLegislatorScraper
from .committees import TXCommitteeScraper
from .bills import TXBillScraper
from .votes import TXVoteScraper
from .events import TXEventScraper

metadata = {
    'name': 'Texas',
    'abbreviation': 'tx',
    'capitol_timezone': 'America/Chicago',
    'legislature_name': 'Texas Legislature',
    'legislature_url': 'http://www.capitol.state.tx.us/',
    'chambers': {
        'upper': {'name': 'Senate', 'title': 'Senator'},
        'lower': {'name': 'House', 'title': 'Representative'},
    },
    'terms': [
        {
            'name': '81',
            'start_year': 2009,
            'end_year': 2010,
            'sessions': ['81', '811'],
        },
        {
            'name': '82',
            'start_year': 2011,
            'end_year': 2012,
            'sessions': ['82', '821'],
        },
        {
            'name': '83',
            'start_year': 2013,
            'end_year': 2014,
            'sessions': ['83', '831', '832', '833'],
        },
        {
            'name': '84',
            'start_year': 2015,
            'end_year': 2016,
            'sessions': ['84'],
        },
        {
            'name': '85',
            'start_year': 2017,
            'end_year': 2018,
            'sessions': ['85', '851'],
        }
    ],
    'session_details': {
        '81': {
            'type': 'primary',
            'start_date': datetime.date(2009, 1, 13),
            'end_date': datetime.date(2009, 6, 1),
            'display_name': '81st Legislature (2009)',
            '_scraped_name': '81(R) - 2009',
        },
        '811': {
            'type': 'special',
            'start_date': datetime.date(2009, 7, 1),
            'end_date': datetime.date(2009, 7, 2),
            'display_name': '81st Legislature, 1st Called Session (2009)',
            '_scraped_name': '81(1) - 2009',
        },
        '82': {
            'type': 'primary',
            'start_date': datetime.date(2011, 1, 11),
            'end_date': datetime.date(2011, 5, 30),
            'display_name': '82nd Legislature (2011)',
            '_scraped_name': '82(R) - 2011',
        },
        '821': {
            'type': 'special',
            'start_date': datetime.date(2011, 5, 31),
            'end_date': datetime.date(2011, 6, 29),
            'display_name': '82nd Legislature, 1st Called Session (2011)',
            '_scraped_name': '82(1) - 2011',
        },
        '83': {
            'type': 'primary',
            'start_date': datetime.date(2013, 1, 8),
            'end_date': datetime.date(2013, 5, 27),
            'display_name': '83rd Legislature (2013)',
            '_scraped_name': '83(R) - 2013',
        },
        '831': {
            'type': 'special',
            'start_date': datetime.date(2013, 5, 27),
            'end_date': datetime.date(2013, 6, 25),
            'display_name': '83nd Legislature, 1st Called Session (2013)',
            '_scraped_name': '83(1) - 2013',
        },
        '832': {
            'type': 'special',
            'start_date': datetime.date(2013, 7, 1),
            'end_date': datetime.date(2013, 7, 30),
            'display_name': '83nd Legislature, 2st Called Session (2013)',
            '_scraped_name': '83(2) - 2013',
        },
        '833': {
            'type': 'special',
            'start_date': datetime.date(2013, 7, 30),
            'end_date': datetime.date(2013, 8, 5),
            'display_name': '83nd Legislature, 3rd Called Session (2013)',
            '_scraped_name': '83(3) - 2013',
        },
        '84': {
            'type': 'primary',
            'start_date': datetime.date(2015, 1, 13),
            'end_date': datetime.date(2015, 6, 1),
            'display_name': '84th Legislature (2015)',
            '_scraped_name': '84(R) - 2015',
        },
        '85': {
            'type': 'primary',
            'start_date': datetime.date(2017, 1, 13),
            'end_date': datetime.date(2017, 6, 1),
            'display_name': '85th Legislature (2017)',
            '_scraped_name': '85(R) - 2017',
        },
        '851': {
            'type': 'special',
            'start_date': datetime.date(2017, 7, 10),
            'display_name': '85th Legislature, 1st Called Session (2017)',
            '_scraped_name': '85(1) - 2017',
        },
    },
    'feature_flags': ['events', 'subjects', 'influenceexplorer'],
    '_ignored_scraped_sessions': [
        '80(R) - 2007',
        '79(3) - 2006',
        '79(2) - 2005',
        '79(1) - 2005',
        '79(R) - 2005',
        '78(4) - 2004',
        '78(3) - 2003',
        '78(2) - 2003',
        '78(1) - 2003',
        '78(R) - 2003',
        '77(R) - 2001',
        '76(R) - 1999',
        '75(R) - 1997',
        '74(R) - 1995',
        '73(R) - 1993',
        '72(4) - 1992',
        '72(3) - 1992',
        '72(2) - 1991',
        '72(1) - 1991',
        '72(R) - 1991',
        '71(6) - 1990',
        '71(5) - 1990',
        '71(4) - 1990',
        '71(3) - 1990',
        '71(2) - 1989',
        '71(1) - 1989',
        '71(R) - 1989',
    ]
}


def session_list():
    from billy.scrape.utils import url_xpath
    return url_xpath( 'http://www.legis.state.tx.us/',
        '//select[@name="cboLegSess"]/option/text()')


def extract_text(doc, data):
    doc = lxml.html.fromstring(data)
    return doc.xpath('//html')[0].text_content()
