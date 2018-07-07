import pandas as pd
import sys, os
import requests
sys.path.append(os.path.join(os.path.dirname(os.curdir)))

url = 'https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'

def q03_scrape_clean(url):
    r = requests.get(url)
    tables = pd.read_html(url,header = 0) #but reading the url via requests and then parsing the text is good enough.
    t = tables[0]
    t.rename(columns= {"Codes:  ISO ISO 3166 codes (2-letter, 3-letter, and 3-digit codes from ISO 3166-1; 2+2-letter codes from ISO 3166-2)  ANSI 2-letter and 2-digit codes from the ANSI standard INCITS 38:2009  USPS 2-letter codes used by the United States Postal Service  USCG 2-letter codes used by the United States Coast Guard (red text shows differences between ANSI and USCG) Abbreviations:  GPO Older variable-length official US Government Printing Office abbreviations  AP Abbreviations from the AP Stylebook (red text shows differences between GPO and AP)" : "United States of America",
                        "ISO 3166 codes (2-letter, 3-letter, and 3-digit codes from ISO 3166-1; 2+2-letter codes from ISO 3166-2)": "C4",
                        "2-letter and 2-digit codes from the ANSI standard INCITS 38:2009":"C6",
                        "2-letter codes used by the United States Postal Service":"Codes used by US' Postal Service",
                        "2-letter codes used by the United States Coast Guard (red text shows differences between ANSI and USCG)":"Codes used by US' Coast Guard",
                        "Abbreviations from the AP Stylebook (red text shows differences between GPO and AP)":"Abbreviations from the AP Stylebook",
                        "Codes:":"Codes"},inplace = True)
    t = t[11:]
    return t
