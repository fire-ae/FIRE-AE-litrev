# FIRE-AE-LitRev

## Overview
The `FIRE-AE-LitRev` repository is designed to streamline literature reviews for researchers by providing tools for querying and managing academic articles. It organizes tools into two sub-repositories focused on specific platforms:

- **NASA-ADS**: Tools for querying and managing articles from NASA's Astrophysics Data System (ADS).
- **arXiv**: Scripts for retrieving and processing preprints from arXiv.

## Repository Structure
```
FIRE-AE-litrev/
├── README.md # Main documentation (this file)
├── NASA-ADS/ # Tools for interacting with NASA ADS │
    ├── README.md # Documentation specific to NASA ADS tools │
    ├── litrevmain.py # Main script for querying NASA ADS │
    ├── litrevlib.py # Core library for NASA ADS interactions │
├── arXiv/ # Tools for interacting with arXiv │
    ├── README.md # Documentation specific to arXiv tools │
    ├── arxiv_preprint_download.py # Script for querying arXiv │
        └── output/ # Directory for storing downloaded files

```
## Sub-Repositories

### NASA-ADS

>[!WARNING]
>Problems can arise in BibTex retrieval parts (not yet for abstracts), so stay tuned for an update.

This sub-repository contains tools for interacting with the NASA ADS API. It enables users to:
- Search for articles based on specific keywords.
- Retrieve metadata such as titles, publication years, citation counts, and abstracts.
- Export BibTeX-formatted citations for selected articles.

Refer to the [NASA-ADS README](NASA-ADS/README.md) for detailed instructions.

### arXiv
The arXiv sub-repository provides scripts for querying and downloading preprints from arXiv. It allows users to:
- Search for papers using specific keywords or categories.
- Download PDFs and manage bibliographic data.
- Automate the creation of BibTeX files for selected entries.

Refer to the [arXiv README](arXiv/README.md) for detailed instructions.

## Contribution
Contributions are welcome! If you'd like to contribute, open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See `LICENSE` for details.
