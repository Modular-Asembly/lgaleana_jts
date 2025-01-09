import json
from typing import Any, Dict, List
from google.cloud import storage
from app.modassembly.storage.get_gcs_bucket import get_gcs_bucket

def store_data_in_gcs(data: List[Dict[str, Any]], filename: str) -> None:
    # Get the Google Cloud Storage bucket
    bucket = get_gcs_bucket()
    
    # Create a new blob (file) in the bucket
    blob = bucket.blob(filename)
    
    # Convert the data to a JSON string
    data_json = json.dumps(data)
    
    # Upload the JSON string to the blob
    blob.upload_from_string(data_json, content_type='application/json')
