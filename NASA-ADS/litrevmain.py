import ads
from litrevlib import query_ads, print_lit, handle_selection

ads.config.token = '' # You should generate this token after registering NASA/ADS freely. You can do this via Accounts >> Settings >> Account Settings >> API Token

# Initial query according to the parameters defined below

query = ['lunar thermal environment'] # specify your query, like what you would enter when you reach out NASA/ADS web api search box.

results = query_ads(query,1) # 1 page = 50 entries at max.

locat = "" #location for your .bib file to transfer bibtex entries

print_lit(results) # This prints titles, year of publication, number of citations, and abstract to the command panel screen

handle_selection(results, [1,5], loca = locat) # transfer 1st and 5th entries as bibtex entries to the locat bib file. 
