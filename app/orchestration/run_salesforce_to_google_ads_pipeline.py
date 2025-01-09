from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, List

from app.salesforce.query_salesforce_data import query_salesforce_data
from app.storage.store_data_in_gcs import store_data_in_gcs
from app.data_processing.format_data_for_google_ads import format_data_for_google_ads
from app.google_ads.upload_to_google_ads import upload_to_google_ads

router = APIRouter()

class PipelineResponse(BaseModel):
    message: str
    salesforce_records: int
    formatted_records: int

@router.post("/run_pipeline", response_model=PipelineResponse)
def run_salesforce_to_google_ads_pipeline() -> PipelineResponse:
    """
    Orchestrates the pipeline to transfer data from Salesforce to Google Ads.

    Steps:
    1) Retrieve data from Salesforce.
    2) Store the raw data in Google Cloud Storage.
    3) Format the data for Google Ads.
    4) Store the formatted data in Google Cloud Storage.
    5) Upload the formatted data to Google Ads.

    Returns:
        PipelineResponse: A summary of the pipeline execution.
    """
    # Step 1: Retrieve data from Salesforce
    salesforce_data = query_salesforce_data()
    
    # Step 2: Store the raw Salesforce data in Google Cloud Storage
    store_data_in_gcs(salesforce_data, "raw_salesforce_data.json")
    
    # Step 3: Format the data for Google Ads
    formatted_data = format_data_for_google_ads(salesforce_data)
    
    # Step 4: Store the formatted data in Google Cloud Storage
    store_data_in_gcs(formatted_data, "formatted_google_ads_data.json")
    
    # Step 5: Upload the formatted data to Google Ads
    upload_to_google_ads(formatted_data)
    
    # Return a summary of the pipeline execution
    return PipelineResponse(
        message="Pipeline executed successfully.",
        salesforce_records=len(salesforce_data),
        formatted_records=len(formatted_data)
    )
