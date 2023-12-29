# Readwise Highlights to Markdown Script

## Introduction
This Python script automates the syncing of Readwise highlights into markdown files, ideal for markdown-based systems like Noteplan and Obsidian. It fetches highlights via the Readwise API and then converts them into structured markdown files.

## Setup
Follow these steps to set up the script:

1. **Clone the Repository**: Download or clone this repository to your local machine.

2. **Install Required Libraries**: The script requires the `requests` library, which can be installed via pip:
   ```
   pip install requests
   ```

3. **Configure the API Token**:
   - Obtain your Readwise API token from [here](https://readwise.io/access_token).
   - Rename `config_sample.py` to `config.py`.
   - In `config.py`, replace `"YOUR_READWISE_API_TOKEN"` with your actual Readwise API token.

4. **Set File Paths in config.py**:
   - Set `JSON_FILE_PATH` to the path where you want the Readwise highlights saved in JSON format (e.g., `'./output/readwise_highlights.json'`).
   - Set `MARKDOWN_OUTPUT_DIR` to the directory where the markdown files will be saved (e.g., `'./output/markdown_files'`).

## Usage
To run the script and generate markdown files from your Readwise highlights, simply execute `main.py`:

```
python main.py
```

This will perform the following actions:

- **Fetch Highlights**: The script calls `fetch_from_readwise_api`, which retrieves your highlights from Readwise and saves them as a JSON file at the location specified in `config.JSON_FILE_PATH`.

- **Generate Markdown Files**: It then processes this JSON file, converting each highlight into a markdown file stored in the directory specified in `config.MARKDOWN_OUTPUT_DIR`.

## How It Works
- **fetch_from_readwise_api**: This module handles the communication with the Readwise API, fetching all the highlights and returning them in JSON format.

- **generate_markdown**: This module loads the JSON data and converts each highlight into a well-structured markdown file.

- **main.py**: The main script that orchestrates the fetching and conversion processes.

## Customization
The script is designed to be modular and adaptable. Feel free to modify it to suit your needs, whether it's changing the markdown format or adding additional data processing steps.