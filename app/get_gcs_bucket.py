import os
from google.cloud import storage
from google.cloud.storage.bucket import Bucket

def get_gcs_bucket() -> Bucket:
    """Initializes the GCS client, creates a bucket if it doesn't exist, and returns it."""
    storage_client = storage.Client()
    bucket_name = os.environ["GCS_BUCKET"]
    
    bucket = storage_client.bucket(bucket_name)
    
    if not bucket.exists():
        bucket = storage_client.create_bucket(bucket_name)
    
    return bucket
