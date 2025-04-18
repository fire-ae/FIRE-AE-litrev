## litrevlib.py
## Module to connect NASA ADS API and retrieve bibliography metadata in the .bibtex format

import ads
import random
import string

def query_ads(query_terms, pages=1):
    """Queries ADS for user-specified query_terms and number of pages, default 1 will return 50 entries.
       !!!This part requires internet connection!!!
    """
    sq = ads.SearchQuery(q=query_terms,
                         fl=['title', 'abstract', 'year', 'citation_count',
                             'bibcode', 'author', 'pub', 'doi'],
                         sort="year",
                         max_pages=pages)
    results = list(sq) # We will use this not only for printing but also picking entries to convert them .bibtex entries
    print("Query completed successfully, returning ",len(results),"results.")
    return results

def print_lit(results):
    """Prints title, year, number of citations, and abstract of papers on command panel."""
    for i, item in enumerate(results, 1):
        print(i, item.title, "Pub. year:", item.year, "# of cit.", item.citation_count, '\n', item.abstract, '\n')

def make_bibtex(item):
    """Crafts bibtex entries from query results."""
    key = item.author[0].split()[-1] + str(item.year) + ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    authors = ' and '.join(item.author)
    bibtex = f"@article{{{key},\n" \
             f"  author = {{{authors}}},\n" \
             f"  title = {{{item.title[0]}}},\n" \
             f"  year = {{{item.year}}},\n" \
             f"  journal = {{{item.pub}}},\n" \
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
