## litrevlib.py
## Module to connect NASA ADS API and retrieve bibliography metadata in the .bibtex format

import ads # Necessary to use ADS API

def ret(query_terms: list | str, page_num: int = 1, list_int: list | int = [], cite: bool = False, loca: str = ""):
    """
    Retrieves titles, publication years, citation counts, and abstracts based on query terms.
    Optionally retrieves BibTeX-formatted citations.

    :param query_terms: Search query terms to look up in NASA ADS.
    :param list_int: List of integers or a single integer specifying items for detailed information.
    :param cite: Flag to print BibTeX-formatted citations of the selected items.
    :param loca: File location to append selected titles' BibTeX entries.
    """
    sq = ads.SearchQuery(
        q=query_terms,
        fl=['title', 'abstract', 'year', 'citation_count', 'bibcode'],
        sort="year",
        max_pages=page_num
    )
    sq.execute()

    for i, item in enumerate(sq, start=1):
        if not list_int:  # Quick look without abstracts
            print(f"{i}. {item.title}\nPub. year: {item.year}, # of cit.: {item.citation_count}\n")
        elif isinstance(list_int, list) and i in list_int:
            print(f"{i}. {item.title}\nPub. year: {item.year}, # of cit.: {item.citation_count}\n\n{item.abstract}\n")
            if cite:
                _export_citation(item.bibcode, loca)
        elif isinstance(list_int, int) and i == list_int:
            print(f"{i}. {item.title}\nPub. year: {item.year}, # of cit.: {item.citation_count}\n\n{item.abstract}\n")
            if cite:
                _export_citation(item.bibcode, loca)
            break

def _export_citation(bibcode: str, loca: str):
    """Helper function to export BibTeX citation."""
    citation = ads.ExportQuery(bibcode, format='bibtex').execute()
    print("Citations\n---------\n", citation)
    if loca:
        with open(loca, 'a', encoding="utf-8") as file:
            file.write(citation + "\n")
