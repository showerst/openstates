import datetime
from billy.utils.fulltext import pdfdata_to_text, text_after_line_numbers
from billy.scrape.utils import url_xpath
from .bills import MOBillScraper
from .legislators import MOLegislatorScraper
from .committees import MOCommitteeScraper
from .votes import MOVoteScraper

metadata = dict(
    name = 'Missouri',
    abbreviation = 'mo',
    legislature_name = 'Missouri General Assembly',
    legislature_url = 'http://www.moga.mo.gov/',
    capitol_timezone = 'America/Chicago',
    chambers = {
        'upper': {
            'name': 'Senate',
            'title': 'Senator'
        },
        'lower': {
            'name': 'House',
            'title': 'Representative'
        },
    },
    terms = [
        {
            'name': '2011-2012',
            'sessions': ['2012'],
            'start_year': 2011,
            'end_year': 2012,
        },
        {
            'name': '2013-2014',
            'sessions': ['2013', '2014'],
            'start_year': 2013,
            'end_year': 2014,
        },
        {
            'name': '2015-2016',
            'sessions': ['2015', '2016'],
            'start_year': 2015,
            'end_year': 2016,
        },
        {
            'name': '2017-2018',
            'sessions': ['2017','2017S1','2017S2'],
            'start_year': 2017,
            'end_year': 2018,
        },        
    ],
    # General Assembly sessions convene the Wed. following the first Mon.
    # of January and adjourn May 30.
    # http://www.house.mo.gov/content.aspx?info=/info/howbill.htm
    session_details = {
        '2012': {
            'type': 'primary',
            'start_date': datetime.date(2012,1,4),
            'end_date': datetime.date(2012,5,30),
            'display_name': '2012 Regular Session',
            '_scraped_name': '2012 Regular Session',
        },
        '2013': {
            'type': 'primary',
            'start_date': datetime.date(2013,1,9),
            'end_date': datetime.date(2013,5,30),
            'display_name': '2013 Regular Session',
            '_scraped_name': '2013 Regular Session',
        },
        '2014': {
            'type': 'primary',
            'start_date': datetime.date(2014,1,8),
            'end_date': datetime.date(2014,5,30),
            'display_name': '2014 Regular Session',
            '_scraped_name': '2014 Regular Session',
        },
        '2015': {
            'type': 'primary',
            'start_date': datetime.date(2015,1,7),
            'end_date': datetime.date(2015,5,30),
            'display_name': '2015 Regular Session',
            '_scraped_name': '2015 Regular Session',
        },
        '2016': {
            'type': 'primary',
            'start_date': datetime.date(2016,1,6),
            'end_date': datetime.date(2016,5,30),
            'display_name': '2016 Regular Session',
            '_scraped_name': '2016 Regular Session',
        },
        '2017': {
            'type': 'primary',
            'start_date': datetime.date(2017,1,4),
            'end_date': datetime.date(2017,5,12),
            'display_name': '2017 Regular Session',
            '_scraped_name': '2017 Regular Session',
        },        
        '2017S1': {
            'type': 'special',
            'start_date': datetime.date(2017,5,24),
            'end_date': datetime.date(2017,5,26),
            'display_name': '2017 Extraordinary Session',
            '_scraped_name': '2017 Extraordinary Session',
        },     
        '2017S2': {
            'type': 'special',
            'start_date': datetime.date(2017,6,12),
            'end_date': datetime.date(2017,6,13),
            'display_name': '2017 2nd Extraordinary Session',
            '_scraped_name': '2017 2nd Extraordinary Session',
        },   
    },
    feature_flags = ['subjects', 'influenceexplorer'],
    _ignored_scraped_sessions = [
        '2013 Extraordinary Session',
        '2011 Extraordinary Session',
        '2011 Regular Session',
        '2010 Extraordinary Session',
        '2010 Regular Session',
        '2009 Regular Session',
        '2008 Regular Session',
        '2007 Extraordinary Session',
        '2007 Regular Session',
        '2006 Regular Session',
        '2005 Extraordinary Session',
        '2005 Regular Session',
        '2004 Regular Session',
        '2003 2nd Extraordinary Session',
        '2003 1st Extraordinary Session',
        '2003 Regular Session',
        '2002 Regular Session',
        '2001 Extraordinary Session',
        '2001 Regular Session',
        '2000 Regular Session',
        '1999 Regular Session',
        'Search All Past Sessions',
    ]
)


def session_list():
    sessions = url_xpath('http://www.house.mo.gov/billcentral.aspx?page=1&q=HB%201',
        '//select[@id="ctl00_ContentPlaceHolder1_SearchSession"]/option/text()')
    return sessions


def extract_text(doc, data):
    text = pdfdata_to_text(data)
    return text_after_line_numbers(text).encode('ascii', 'ignore')
