from google.cloud import storage
from app.modassembly.storage.get_gcs_bucket import get_gcs_bucket
from typing import Any

def store_data_in_gcs(data: Any, destination_blob_name: str) -> None:
    """
    Store the given data in a Google Cloud Storage bucket.

    :param data: The data to be stored. This can be any type that can be converted to bytes.
    :param destination_blob_name: The name of the blob in the bucket where the data will be stored.
    """
    bucket = get_gcs_bucket()
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(data)
