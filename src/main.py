# main.py

import datetime
import json
import os
import config
from fetch_highlights import fetch_from_export_api
from generate_markdown import generate_markdown_files

def main():
    # Fetch all highlights data.
    all_data = fetch_from_export_api()
    last_fetch_was_at = datetime.datetime.now() - datetime.timedelta(days=1)
    new_data = fetch_from_export_api(last_fetch_was_at.isoformat())

    # Ensure the output directory for JSON exists.
    json_output_dir = os.path.dirname(config.JSON_FILE_PATH)
    os.makedirs(json_output_dir, exist_ok=True)

    # Save the fetched data to a JSON file.
    with open(config.JSON_FILE_PATH, 'w') as file:
        json.dump(all_data, file, indent=4)

    print(f"Data saved to {config.JSON_FILE_PATH}")

    # Generate markdown files from the fetched data.
    generate_markdown_files()

if __name__ == "__main__":
    main()
