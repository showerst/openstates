from billy.utils.fulltext import worddata_to_text
from .bills import OKBillScraper
from .legislators import OKLegislatorScraper
from .committees import OKCommitteeScraper
from .events import OKEventScraper

settings = dict(SCRAPELIB_TIMEOUT=120)

metadata = dict(
    name='Oklahoma',
    abbreviation='ok',
    legislature_name='Oklahoma Legislature',
    legislature_url='http://www.oklegislature.gov/',
    capitol_timezone='America/Chicago',
    chambers = {
        'upper': {'name': 'Senate', 'title': 'Senator'},
        'lower': {'name': 'House', 'title': 'Representative'},
    },
    terms=[
        {'name': '2011-2012',
         'start_year': 2011,
         'end_year': 2012,
         'sessions': ['2011-2012', '2012SS1']},
         {'name': '2013-2014',
          'start_year': 2013,
          'end_year': 2014,
          'sessions': ['2013-2014', '2013SS1']},
         {'name': '2015-2016',
          'start_year': 2015,
          'end_year': 2016,
          'sessions': ['2015-2016']},
         {'name': '2017-2018',
          'start_year': 2017,
          'end_year': 2018,
          'sessions': ['2017-2018','2017SS1']},
        ],
    session_details={
        # On the Oklahoma website they list 2011/2012 as separate sessions, but
        # bill numbering does not restart in even year sessions so we treat
        # them as the same session.  This means the session_id/_scraped_name
        # will change in even years and we'll need to ignore odd years
        '2011-2012':
            {'display_name': '2011-2012 Regular Session',
             'session_id': '1200',
             '_scraped_name': '2012'
            },
        '2012SS1':
            {'display_name': '2012 Special Session',
             'session_id': '121X',
             '_scraped_name': '2012s'
            },
        '2013SS1':
            {'display_name': '2013 Special Session',
             'session_id': '131X',
             '_scraped_name': '2013s',
            },
         '2013-2014':
            {'display_name': '2013-2014 Regular Session',
             'session_id': '1400',
             '_scraped_name': '2014',
            },
         '2015-2016':
            {'display_name': '2015-2016 Regular Session',
             'session_id': '1600',
             '_scraped_name': '2016',
            },
         '2017-2018':
            {'display_name': '2017-2018 Regular Session',
             'session_id': '1700',
             '_scraped_name': '2017',
            },
        '2017SS1':
            {'display_name': '2017 Special Session',
             'session_id': '171X',
             '_scraped_name': '2017s'
            },            
        },
    feature_flags=['subjects', 'influenceexplorer'],
    _ignored_scraped_sessions=[
u'2015', u'2013', u'2011s', u'2011', u'2010', u'2009', u'2008', u'2007', u'2006', u'2005', u'2005s', u'2004', u'2003', u'2003s', u'2002', u'2001', u'2001s', u'2000', u'2000s', u'1999', u'1998', u'1997', u'1997s']
    )


def session_list():
    from billy.scrape.utils import url_xpath
    sessions = url_xpath('http://www.sdlegislature.gov/Legislative_Session/archive.aspx',
                        '//table//td[@data-title="Year"]/text()')
    # OK Sometimes appends (Mainsys) to their session listings
    sessions = [s.replace('(Mainsys)', '').strip() for s in sessions]
    return sessions

def extract_text(doc, data):
    return worddata_to_text(data)
