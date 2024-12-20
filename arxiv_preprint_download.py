# module to manage arXiv API for my literaturing reviewing

import requests # to retrieve data/pages from the URLs
import time # to format day-month-year for temporal filter
import os # to automatize file saving
from datetime import datetime # for datetime operations
from xml.etree import ElementTree as ET # checking response status

def format_date(date):
    """Convert datetime to ArXiv API date format YYYYMMDD0000."""
    return date.strftime('%Y%m%d0000')

def write_bibtex_entry(bib_file, arxiv_id, title, authors, published, summary=None):
    """Write an individual BibTeX entry to the provided file.
    bib_file: the related .bib extended bibliography file
    arxiv_id, title, authors: preprint metadata
    published: year of publication    
    """
    bib_file.write(f"@article{{{arxiv_id},\n")
    bib_file.write(f"  author = {{{' and '.join(authors)}}},\n")
    bib_file.write(f"  title = {{{title}}},\n")
    bib_file.write(f"  year = {{{published.split('-')[0]}}},\n")
    bib_file.write(f"  journal = {{arXiv}},\n")
    bib_file.write(f"  url = {{https://arxiv.org/abs/{arxiv_id}}},\n")
    bib_file.write("}\n\n")

def download_pdf(pdf_url, pdf_path):
    """Download a PDF from a given URL and save it to the specified path."""
    try:
        response = requests.get(pdf_url, timeout=18)
        if response.status_code == 200:
            with open(pdf_path, 'wb') as pdf_file:
                pdf_file.write(response.content)
            print(f"Downloaded PDF: {pdf_path}")
            return True
        else:
            print(f"Failed to download PDF from {pdf_url}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading PDF: {e}")
    return False

def download_arxiv_papers(start_date, end_date, num_paper, query_type, query, delay=40):
    """
    Download papers matching a query from ArXiv, save BibTeX entries, and download PDFs.

    Parameters:
    - query: Search query for ArXiv.
    - start_date: Start date (YYYY-MM-DD) for the query.
    - end_date: End date (YYYY-MM-DD) for the query.
    - bib_filename: Name of the output BibTeX file.
    - pdf_folder: Directory where PDFs will be saved.
    - delay: Delay between PDF downloads to avoid overwhelming the server.
    """
    
    bib_filename = f'{query_type}_{start_date}_{end_date}.bib'
    pdf_folder = f'{query_type}_pdfs_{start_date}_{end_date}'
    os.makedirs(pdf_folder, exist_ok=True)
    formatted_start_date = format_date(datetime.strptime(start_date, '%Y-%m-%d'))
    formatted_end_date = format_date(datetime.strptime(end_date, '%Y-%m-%d'))
    base_url = 'http://export.arxiv.org/api/query?'
    search_query = f'search_query={query}+AND+submittedDate:[{formatted_start_date}+TO+{formatted_end_date}]&max_results={num_paper}'
    response = requests.get(base_url + search_query)
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        total_results = root.find('{http://a9.com/-/spec/opensearch/1.1/}totalResults').text
        print(f"Total results found: {total_results}")
        with open(bib_filename, 'w', encoding='utf-8') as bib_file:
            paper_count = 0
            for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
                title = entry.find('{http://www.w3.org/2005/Atom}title').text
                authors = [author.find('{http://www.w3.org/2005/Atom}name').text for author in entry.findall('{http://www.w3.org/2005/Atom}author')]
                published = entry.find('{http://www.w3.org/2005/Atom}published').text
                arxiv_id = entry.find('{http://www.w3.org/2005/Atom}id').text.split('/')[-1]
                summary = entry.find('{http://www.w3.org/2005/Atom}summary').text if query_type == "dec" else None
                write_bibtex_entry(bib_file, arxiv_id, title, authors, published, summary)
                pdf_path = os.path.join(pdf_folder, f"{arxiv_id}.pdf")
                pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
                if os.path.exists(pdf_path):
                    print(f"File already exists, skipping: {pdf_path}")
                else:
                    success = download_pdf(pdf_url, pdf_path)
                    if success:
                        time.sleep(delay)  # Delay only if a new download happens
                    else:
                        print(f"Failed to download PDF for {arxiv_id}")
                paper_count += 1
            print(f"{paper_count} papers processed.")
    else:
        print(f"Error with request. Status code: {response.status_code}")



### The part that manages arXiv

# For decomposition papers
download_arxiv_papers('2024-11-05', '2024-11-11', 40, "dec", "cat:stat.ML OR cat:stat.ME AND (all:decomposition OR all:singular OR all:Fourier OR all:component OR all:factorization)")

# For astro-ph.EP papers
download_arxiv_papers('2024-11-05', '2024-11-11', 60, "astro", "cat:astro-ph.EP")

# For remote sensing papers
download_arxiv_papers(
    start_date="2024-11-05",
    end_date="2024-11-11",
    num_paper=50,
    query_type="rs",
    query="(cat:eess.SP OR cat:cs.CV OR cat:stat.ML OR cat:stat.AP) AND all:\"remote sensing\""
)
