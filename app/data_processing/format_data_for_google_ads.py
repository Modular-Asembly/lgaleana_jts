from typing import Any, Dict
from app.storage.store_data_in_gcs import store_data_in_gcs

def format_data_for_google_ads(salesforce_data: Dict[str, Any]) -> Dict[str, Any]:
    # Step 2: Transform the data into the format required by Google Ads
    # This is a simple transformation example. Adjust according to your needs.
    formatted_data = {
        "name": salesforce_data.get("Name", ""),
        "advertising_channel_type": "SEARCH",  # Example static value
        "status": "ENABLED"  # Example static value
    }

    # Step 3: Store the formatted data in a Google Cloud Storage bucket
    # Convert formatted data to a string or JSON format for storage
    formatted_data_str = str(formatted_data)
    store_data_in_gcs(formatted_data_str, "formatted_data.json")

    # Step 4: Return the formatted data
    return formatted_data
