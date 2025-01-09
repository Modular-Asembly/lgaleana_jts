from typing import Any, Dict, List
from app.storage.store_data_in_gcs import store_data_in_gcs

def format_data_for_google_ads(salesforce_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    # Transform the Salesforce data into the format required by Google Ads
    formatted_data = [
        {
            "google_ads_id": record["Id"],
            "name": record["Name"],
            # Add more transformations as needed
        }
        for record in salesforce_data
    ]
    
    # Store the formatted data in Google Cloud Storage
    store_data_in_gcs(formatted_data, "formatted_google_ads_data.json")
    
    # Return the formatted data
    return formatted_data
