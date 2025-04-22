## litrevlib.py
## Module to connect NASA ADS API and retrieve bibliography metadata in the .bibtex format

import ads
import random
import string

def abstract_ads(query_term, pages=1):
    """Queries NASA ADS database entries abstract fields for a given string (not a list as in q!).
    !!! This part requires internet connection, the rest does not !!!
    Parameters:
    query_term (string): Term to query the abstract fields of the NASA ADS.
    pages (int): number of pages to retrieve, multiply by 50 to expect the maximum number of returned entry
    Returns a list of ads.SearchQuery output that can be fed to print_lit and make_bibtex for further processing    
    """
    
    sq = ads.SearchQuery(abstract=query_term,
                         fl=['title', 'abstract', 'year', 'citation_count',
                             'bibcode', 'author', 'pub', 'doi'],
                         sort="year",
                         max_pages=pages)
    results = list(sq)
    print("Query completed successfully, returning ",len(results),"results.")
    return results

def print_lit(results):
    for i, item in enumerate(results, 1):
        print(i, item.title, "Pub. year:", item.year, "# of cit.", item.citation_count, '\n', item.abstract, '\n')

def make_bibtex(item):
    """Craft Bibtex entries with abstract and doi fields."""
    key = item.author[0].split()[-1] + str(item.year) + ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    authors = ' and '.join(item.author)
    bibtex = f"@article{{{key},\n" \
             f"  author = {{{authors}}},\n" \
             f"  title = {{{item.title[0]}}},\n" \
             f"  year = {{{item.year}}},\n" \
             f"  journal = {{{item.pub}}},\n" \
             f"  abstract = {{{item.abstract}}},\n" \
             f"  bibcode = {{{item.bibcode}}},\n"
    if hasattr(item, 'doi') and item.doi:
        bibtex += f"  doi = {{{item.doi[0]}}},\n"
    bibtex += "}"
    return bibtex

def handle_selection(results, indices, loca=""):
    """Transfers necessary entry information from results to the specified bibtex file at loca as bibtex entries."""
    for i, item in enumerate(results, 1):
        if (isinstance(indices, list) and i in indices) or (isinstance(indices, int) and i == indices):
            bib = make_bibtex(item)
            if loca:
                with open(loca, 'a', encoding='utf-8') as f:
                    f.write(bib + "\n")
