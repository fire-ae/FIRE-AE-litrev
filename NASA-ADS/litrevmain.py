import ads
import litrevlib

ads.config.token = '' # You should generate this token after registering NASA/ADS freely. You can do this via Accounts >> Settings >> Account Settings >> API Token

# Query parameters
query = ['JWST', 'disk', 'exoplanet'] # parameters to query the .bibtex metadata
locat = "D:/jwst-tex/oja/to-oja.bib" # location of the .bib extended bibliography file to export requested .bibtex entries

# page_num is number of pages you would like to retrieve, default is 1 and corresponds to 50 articles, please use it with caution to not choking server

# Print titles, year, citation counts
litrevlib.ret(query, page_num=1)

# Retrieve and print the 3rd item's detailed information
litrevlib.ret(query, page_num=1, 3)

# Retrieve and append the 3rd item's BibTeX citation to a file
litrevlib.ret(query, page_num=1, 3, cite=True, loca=locat)

# Retrieve and print multiple selected items' details
litrevlib.ret(query, page_num=1, [6, 8, 9, 13, 17, 22, 23, 24, 25, 27, 30, 36, 37, 39, 47])

# Retrieve multiple selected items' BibTeX citations and append them to a file
litrevlib.ret(query, page_num=1, [13, 17, 23, 24, 25, 27, 30, 36, 37, 39, 47], cite=True, loca=locat)
