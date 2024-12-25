# arXiv Literature Review Automation

This repository contains Python scripts designed to facilitate the retrieval of academic papers from the [arXiv API](https://arxiv.org/help/api/). It automates the process of querying specific topics, downloading BibTeX entries, and fetching PDFs for further research purposes. This tool is particularly useful for researchers conducting systematic literature reviews.

## Features

- **Custom Date Range Query**: Specify start and end dates to filter papers by submission date.
- **Flexible Search Queries**: Search papers using keywords and categories.
- **BibTeX Entry Generation**: Automatically save retrieved papers' metadata in `.bib` files for reference management.
- **PDF Downloads**: Download associated PDFs and organize them in topic-specific folders.
- **Configurable Download Delays**: Set delays between downloads to respect arXiv's server policies.

## Dependencies

Ensure the following Python libraries are installed:

- `requests` (for making API calls)
- `datetime` (for handling dates)
- `os` (for managing file operations)
- `time` (for delays between requests)
- `xml.etree.ElementTree` (for parsing XML responses)

Install the required libraries using:
```bash
pip install requests
```

## Usage

### Formatting Dates
Dates must be provided in the format `YYYY-MM-DD`. The `format_date()` function converts these to the `YYYYMMDD0000` format required by the ArXiv API.

### Writing BibTeX Entries
The `write_bibtex_entry()` function writes metadata for each retrieved paper to a `.bib` file. The following fields are included:
- `author`
- `title`
- `year`
- `journal` (set to `arXiv`)
- `url` (link to the paper)

### Downloading PDFs
The `download_pdf()` function fetches the PDF for a given paper using its ArXiv ID and saves it to a specified directory.

### Main Workflow
Use the `download_arxiv_papers()` function to:
1. Query the ArXiv API with specific search criteria.
2. Retrieve metadata for papers within a specified date range.
3. Save metadata to a BibTeX file.
4. Download PDFs for the retrieved papers.

#### Example:
```python
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
```

### Parameters
| Parameter     | Description                                    |
|---------------|------------------------------------------------|
| `query`       | Search query string.                          |
| `start_date`  | Start of the date range (format: `YYYY-MM-DD`).|
| `end_date`    | End of the date range (format: `YYYY-MM-DD`).  |
| `num_paper`   | Number of papers to retrieve.                 |
| `query_type`  | Topic category (e.g., `dec`, `astro`, `rs`).   |
| `delay`       | Delay (in seconds) between PDF downloads.      |

## Output

1. **BibTeX File**: A `.bib` file named as `{query_type}_{start_date}_{end_date}.bib`.
2. **PDF Directory**: A folder named `{query_type}_pdfs_{start_date}_{end_date}` containing downloaded PDFs.

## File Organization

```
repository/
|
|-- arxiv_preprint_download.py        # Main Python script for arXiv automation
|-- README.md                         # Project documentation
|-- outputs/
    |-- *.bib                         # BibTeX files
    |-- topic_pdfs/                   # Folders containing downloaded PDFs
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- Developed for managing systematic literature reviews efficiently.
- Utilizes the [arXiv API](https://arxiv.org/help/api/) for data retrieval.
