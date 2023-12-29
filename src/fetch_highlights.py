# fetch_highlights.py
import requests
import time
import config

# Function to fetch highlights from Readwise using their API.
def fetch_from_readwise_api(updated_after=None):
    token = config.READWISE_TOKEN  # Get the API token from the config file.
    if not token:
        raise ValueError("Readwise token not found in config file")

    full_data = []
    next_page_cursor = None

    # Loop to handle pagination in API response.
    while True:
        # Prepare parameters for API request.
        params = {'pageCursor': next_page_cursor} if next_page_cursor else {}
        if updated_after:
            params['updatedAfter'] = updated_after

        print("Making export API request with params " + str(params) + "...")
        response = requests.get(
            url="https://readwise.io/api/v2/export/",
            params=params,
            headers={"Authorization": f"Token {token}"}
        )

        # Handle unsuccessful requests.
        if response.status_code != 200:
            print(f"Error fetching data: {response.status_code}")
            time.sleep(10)  # Retry after a delay in case of error.
            continue

        # Process successful response.
        data = response.json()
        full_data.extend(data['results'])
        next_page_cursor = data.get('nextPageCursor')

        # Exit loop when no more pages are available.
        if not next_page_cursor:
            break

    return full_data
