# FIRE-AE-LitRev NASA/ADS literature review tools

## Overview
This repository provides tools to streamline literature reviews using the NASA ADS API. It includes scripts to query, retrieve, and manage scientific articles efficiently.

### Key Features
- Query NASA ADS for research articles based on keywords.
- Retrieve titles, publication years, citation counts, and abstracts.
- Export BibTeX-formatted citations to a specified file.

## Repository Structure

```
FIRE-AE-litrev/NASA-ADS/
|
|-- litrevmain.py                     # Main Python script for NASA/ADS literature review
|-- README.md                         # Project documentation
|-- litrevlib.py                      # Library and functions to run litrevmain.py
```

## Prerequisites
- **Python 3.8+**
- **NASA ADS Python API**
  - Install via pip: `pip install ads`
- A valid NASA ADS API token (available at [NASA ADS](https://ui.adsabs.harvard.edu/user/settings/token)).

## Setup
1. Clone the repository:
   ```
   bash
   git clone https://github.com/your_username/FIRE-AE-litrev/NASA-ADS/.git
   cd FIRE-AE-litrev/NASA-ADS
   ```
2. Install the required libraries:
   ```
   pip install ads
   ```
3. Configure your NASA/ADS token:
    - Open litrev.py and replace the placeholder with your token:
      ```
      ads.config.token = 'your_ads_api_token
      ```
## Usage
### Running the Main Script
- Update the `query` variable in `litrev.py` with your desired keywords.
- 1. First, only retrieve titles
```
litrevlib.ret(['keyword1', 'keyword2'])
```
  2. Second, retrieve abstracts of the interesting titles for you
```
litrevlib.ret(['keyword1', 'keyword2'], 3) # This retrieves the abstract for the 3rd entry
```

  3. Retrieve .bibtex entries of relevant articles and export them to their desired .bib file
```
litrevlib.ret(['keyword1', 'keyword2'], [2, 5], cite=True, loca='output/citations.bib')
```

