import datetime
import lxml.html
from billy.utils.fulltext import text_after_line_numbers, pdfdata_to_text
from .bills import AZBillScraper
from .legislators import AZLegislatorScraper
from .committees import AZCommitteeScraper
from .events import AZEventScraper

metadata = dict(
    name='Arizona',
    abbreviation='az',
    legislature_name='Arizona State Legislature',
    legislature_url='http://www.azleg.gov/',
    capitol_timezone='America/Denver',
    chambers = {
        'upper': {'name': 'Senate', 'title': 'Senator'},
        'lower': {'name': 'House', 'title': 'Representative'},
    },
    terms = [
        {'name': '49',
            'sessions': [
            '49th-1st-special',
            '49th-2nd-special',
            '49th-1st-regular',
            '49th-3rd-special',
            '49th-4th-special',
            '49th-5th-special',
            '49th-6th-special',
            '49th-7th-special',
            '49th-8th-special',
            '49th-2nd-regular',
            '49th-9th-special',

            ],
            'start_year': 2009, 'end_year': 2010
        },

        {'name': '50',
            'sessions': [
            '50th-1st-special',
            '50th-2nd-special',
            '50th-3rd-special',
            '50th-4th-special',
            '50th-1st-regular',
            '50th-2nd-regular',
            ],
            'start_year': 2011, 'end_year': 2012
        },
        {'name': '51',
            'sessions': [
            '51st-1st-regular',
            '51st-1st-special',
            '51st-2nd-regular',
            '51st-2nd-special',
            ],
            'start_year': 2013, 'end_year': 2014
        },
        {
            'name': '52',
            'sessions': [
                '52nd-1st-regular',
                '52nd-1st-special',
                '52nd-2nd-regular',
            ],
            'start_year': 2015,
            'end_year': 2016
        },
        {
            'name': '53',
            'sessions': [
                '53rd-1st-regular',
                '53rd-2nd-regular',
            ],
            'start_year': 2017,
            'end_year': 2018
        },
        ],
        session_details={
            '49th-1st-regular':
                {'type': 'primary', 'session_id': 87,
                'display_name': '49th Legislature, 1st Regular Session (2009)',
                'start_date': datetime.date(2009, 1, 12),
                'end_date': datetime.date(2009, 7, 1),
                '_scraped_name': '2009 - Forty-ninth Legislature - First Regular Session',
                },
            '49th-1st-special':
                {'type': 'special', 'session_id': 89,
                'display_name': '49th Legislature, 1st Special Session (2009)',
                'start_date': datetime.date(2009, 1, 28),
                'end_date': datetime.date(2009, 1, 31),
                '_scraped_name': '2009 - Forty-ninth Legislature - First Special Session',
                },
            '49th-2nd-special':
                {'type': 'special', 'session_id': 90,
                'display_name': '49th Legislature, 2nd Special Session (2009)',
                'start_date': datetime.date(2009, 5, 21),
                'end_date': datetime.date(2009, 5, 27),
                '_scraped_name': '2009 - Forty-ninth Legislature - Second Special Session',
                },
            '49th-3rd-special':
                {'type': 'special', 'session_id': 91,
                'display_name': '49th Legislature, 3rd Special Session (2009)',
                'start_date': datetime.date(2009, 7, 6),
                'end_date': datetime.date(2009, 8, 25),
                '_scraped_name': '2009 - Forty-ninth Legislature - Third Special Session',
                },
            '49th-4th-special':
                {'type': 'special', 'session_id': 92,
                'display_name': '49th Legislature, 4th Special Session (2009)',
                'start_date': datetime.date(2009, 11, 17),
                'end_date': datetime.date(2009, 11, 23),
                '_scraped_name': '2009 - Forty-ninth Legislature - Fourth Special Session',
                },
            '49th-5th-special':
                {'type': 'special', 'session_id': 94,
                'display_name': '49th Legislature, 5th Special Session (2009)',
                'start_date': datetime.date(2009, 12, 17),
                'end_date': datetime.date(2009, 12, 19),
                '_scraped_name': '2009 - Forty-ninth Legislature - Fifth Special Session',
                },
            '49th-6th-special':
                {'type': 'special', 'session_id': 95,
                'display_name': '49th Legislature, 6th Special Session (2010)',
                'start_date': datetime.date(2010, 2, 1),
                'end_date': datetime.date(2010, 2, 11),
                '_scraped_name': '2010 - Forty-ninth Legislature - Sixth Special Session',
                },
            '49th-7th-special':
                {'type': 'special', 'session_id': 96,
                'display_name': '49th Legislature, 7th Special Session (2010)',
                'start_date': datetime.date(2010, 3, 8),
                'end_date': datetime.date(2010, 3, 16),
                '_scraped_name': '2010 - Forty-ninth Legislature - Seventh Special Session',
                },
            '49th-8th-special':
                {'type': 'special', 'session_id': 101,
                'display_name': '49th Legislature, 8th Special Session (2010)',
                'start_date': datetime.date(2010, 3, 29),
                'end_date': datetime.date(2010, 4, 1),
                '_scraped_name': '2010 - Forty-ninth Legislature - Eighth Special Session',
                },
            '49th-9th-special':
                {'type': 'special', 'session_id': 103,
                'display_name': '49th Legislature, 9th Special Session (2010)',
                'start_date': datetime.date(2010, 8, 9),
                'end_date': datetime.date(2010, 8, 11),
                '_scraped_name': '2010 - Forty-ninth Legislature - Ninth Special Session',
                },
            '49th-2nd-regular':
                {'type': 'primary', 'session_id': 93,
                'display_name': '49th Legislature, 2nd Regular Session (2010)',
                'start_date': datetime.date(2010, 1, 11),
                'end_date': datetime.date(2010, 4, 29),
                '_scraped_name': '2010 - Forty-ninth Legislature - Second Regular Session',
                },
            '50th-1st-special':
                {'type': 'special', 'session_id': 104,
                'display_name': '50th Legislature, 1st Special Session (2011)',
                'start_date': datetime.date(2011, 1, 19),
                'end_date': datetime.date(2011, 1, 20),
                '_scraped_name': '2011 - Fiftieth Legislature - First Special Session',
                },
            '50th-2nd-special':
                {'type': 'special', 'session_id': 105,
                'display_name': '50th Legislature, 2nd Special Session (2011)',
                'start_date': datetime.date(2011, 2, 14),
                'end_date': datetime.date(2011, 2, 16),
                '_scraped_name': '2011 - Fiftieth Legislature - Second Special Session',
                },
            '50th-3rd-special':
                {'type': 'special', 'session_id': 106,
                'display_name': '50th Legislature, 3rd Special Session (2011)',
                'start_date': datetime.date(2011, 6, 10),
                'end_date': datetime.date(2011, 6, 13),
                '_scraped_name': '2011 - Fiftieth Legislature - Third Special Session',
                },
            '50th-4th-special':
                {'type': 'special', 'session_id': 108,
                'display_name': '50th Legislature, 4th Special Session (2011)',
                'start_date': datetime.date(2011, 11, 1),
                'end_date': datetime.date(2011, 11, 1),
                '_scraped_name': '2011 - Fiftieth Legislature - Fourth Special Session',
                },
            '50th-1st-regular':
                {'type': 'primary', 'session_id': 102,
                'display_name': '50th Legislature, 1st Regular Session (2011)',
                'start_date': datetime.date(2011, 1, 10),
                'end_date': datetime.date(2011,4,20),
                '_scraped_name': '2011 - Fiftieth Legislature - First Regular Session',
                },
            '50th-2nd-regular':
                {'type': 'primary', 'session_id': 107,
                'display_name': '50th Legislature, 2nd Regular Session (2012)',
                '_scraped_name': '2012 - Fiftieth Legislature - Second Regular Session',
                #'start_date': , 'end_date':
                },
            '51st-1st-regular':
                {'type': 'primary', 'session_id': 110,
                 'display_name': '51st Legislature - 1st Regular Session (2013)',
                 '_scraped_name': '2013 - Fifty-first Legislature - First Regular Session'
                },
            '51st-1st-special':
                {'type': 'primary', 'session_id': 111,
                 'display_name': '51st Legislature - 1st Special Session (2013)',
                 '_scraped_name': '2013 - Fifty-first Legislature - First Special Session'
                },
            '51st-2nd-regular':
                {'type': 'primary', 'session_id': 112,
                 'display_name': '51st Legislature - 2nd Regular Session',
                 '_scraped_name': '2014 - Fifty-first Legislature - Second Regular Session'
                },
            '51st-2nd-special':
                {'type': 'special', 'session_id': 113,
                 'display_name': '51st Legislature - 2nd Special Session',
                 '_scraped_name': '2014 - Fifty-first Legislature - Second Special Session'
                },
            '52nd-1st-regular':
                {'type': 'primary', 'session_id': 114,
                 'display_name': '52nd Legislature - 1st Regular Session',
                 '_scraped_name': '2015 - Fifty-second Legislature - First Regular Session'
                },
            '52nd-1st-special': {
                'type': 'special',
                'session_id': 116, # Yes, this is weirdly out of order.
                 'display_name': '52nd Legislature - 1st Special Session',
                 '_scraped_name': '2015 - Fifty-second Legislature - First Special Session',
            },
            '52nd-2nd-regular': {
                'type': 'primary',
                'session_id': 115,
                'display_name': '52nd Legislature - 2nd Regular Session',
                '_scraped_name': '2016 - Fifty-second Legislature - Second Regular Session',
            },
            '53rd-1st-regular': {
                'type': 'primary',
                'session_id': 117,
                'display_name': '53rd Legislature - 1st Regular Session',
                '_scraped_name': '2017 - Fifty-third Legislature - First Regular Session',
            },
            '53rd-2nd-regular': {
                'type': 'primary',
                'session_id': 119,
                'display_name': '53rd Legislature - 2nd Regular Session',
                '_scraped_name': '2018 - Fifty-third Legislature - Second Regular Session',
            }
            # get session id from http://www.azleg.gov/SelectSession.asp select
        },
        _ignored_scraped_sessions=[
			'2008 - Forty-eighth Legislature - Second Regular Session',
			'2007 - Forty-eighth Legislature - First Regular Session',
			'2006 - Forty-seventh Legislature - First Special Session',
			'2006 - Forty-seventh Legislature - Second Regular Session',
			'2005 - Forty-seventh Legislature - First Regular Session',
			'2004 - Forty-sixth Legislature - Second Regular Session',
			'2003 - Forty-sixth Legislature - Second Special Session',
			'2003 - Forty-sixth Legislature - First Special Session',
			'2003 - Forty-sixth Legislature - First Regular Session',
			'2002 - Forty-fifth Legislature - Sixth Special Session',
			'2002 - Forty-fifth Legislature - Fifth Special Session',
			'2002 - Forty-fifth Legislature - Fourth Special Session',
			'2002 - Forty-fifth Legislature - Third Special Session',
			'2002 - Forty-fifth Legislature - Second Regular Session',
			'2001 - Forty-fifth Legislature - Second Special Session',
			'2001 - Forty-fifth Legislature - First Special Session',
			'2001 - Forty-fifth Legislature - First Regular Session',
			'2000 - Forty-fourth Legislature - Seventh Special Session',
			'2000 - Forty-fourth Legislature - Sixth Special Session',
			'2000 - Forty-fourth Legislature - Fifth Special Session',
			'2000 - Forty-fourth Legislature - Fourth Special Session',
			'2000 - Forty-fourth Legislature - Second Regular Session',
			'1999 - Forty-fourth Legislature - Third Special Session',
			'1999 - Forty-fourth Legislature - Second Special Session',
			'1999 - Forty-fourth Legislature - First Special Session',
			'1999 - Forty-fourth Legislature - First Regular Session',
			'1998 - Forty-third Legislature - Sixth Special Session',
			'1998 - Forty-third Legislature - Fifth Special Session',
			'1998 - Forty-third Legislature - Fourth Special Session',
			'1998 - Forty-third Legislature - Third Special Session',
			'1998 - Forty-third Legislature - Second Regular Session',
			'1997 - Forty-third Legislature - Second Special Session',
			'1997 - Forty-third Legislature - First Special Session',
			'1997 - Forty-third Legislature - First Regular Session',
			'1996 - Forty-second Legislature - Seventh Special Session',
			'1996 - Forty-second Legislature - Sixth Special Session',
			'1996 - Forty-second Legislature - Fifth Special Session',
			'1996 - Forty-second Legislature - Second Regular Session',
			'1995 - Forty-second Legislature - Fourth Special Session',
			'1995 - Forty-second Legislature - Third Special Session',
			'1995 - Forty-Second Legislature - Second Special Session',
			'1995 - Forty-Second Legislature - First Special Session',
			'1995 - Forty-second Legislature - First Regular Session',
			'1994 - Forty-first Legislature - Ninth Special Session',
			'1994 - Forty-first Legislature - Eighth Special Session',
			'1994 - Forty-first Legislature - Second Regular Session',
			'1993 - Forty-first Legislature - Seventh Special Session',
			'1993 - Forty-first Legislature - Sixth Special Session',
			'1993 - Forty-first Legislature - Fifth Special Session',
			'1993 - Forty-first Legislature - Fourth Special Session',
			'1993 - Forty-first Legislature - Third Special Session',
			'1993 - Forty-first Legislature - Second Special Session',
			'1993 - Forty-first Legislature - First Special Session',
			'1993 - Forty-first Legislature - First Regular Session',
			'1992 - Fortieth Legislature - Ninth Special Session',
			'1992 - Fortieth Legislature - Eighth Special Session',
			'1992 - Fortieth Legislature - Seventh Special Session',
			'1992 - Fortieth Legislature - Fifth Special Session',
			'1992 - Fortieth Legislature - Sixth Special Session',
			'1992 - Fortieth Legislature - Second Regular Session',
			'1991 - Fortieth Legislature - Fourth Special Session',
			'1991 - Fortieth Legislature - Third Special Session',
			'1991 - Fortieth Legislature - Second Special Session',
			'1991 - Fortieth Legislature - First Special Session',
			'1991 - Fortieth Legislature - First Regular Session',
			'1990 - Thirty-ninth Legislature - Fifth Special Session',
			'1990 - Thirty-ninth Legislature - Fourth Special Session',
			'1990 - Thirty-ninth Legislature - Third Special Session',
			'1990 - Thirty-ninth Legislature - Second Regular Session',
			'1989 - Thirty-ninth Legislature - Second Special Session',
			'1989 - Thirty-ninth Legislature - First Special Session',
			'1989 - Thirty-ninth Legislature - First Regular Session'
            ],
        feature_flags=[ 'events', 'influenceexplorer' ],
    )


def session_list():
    import re
    import requests
    session = requests.Session()

    data = session.get('http://www.azleg.gov/')

    #TODO: JSON at https://apps.azleg.gov/api/Session/

    doc = lxml.html.fromstring(data.text)
    sessions = doc.xpath('//select/option/text()')
    sessions = [re.sub(r'\(.+$', '', x).strip() for x in sessions]
    return sessions