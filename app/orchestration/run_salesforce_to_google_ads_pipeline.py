from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any
from app.salesforce.query_salesforce_data import query_salesforce_data
from app.storage.store_data_in_gcs import store_data_in_gcs
from app.data_processing.format_data_for_google_ads import format_data_for_google_ads
from app.google_ads.upload_to_google_ads import upload_to_google_ads

router = APIRouter()

class SalesforceQueryInput(BaseModel):
    query: str

class PipelineOutput(BaseModel):
    success: bool
    message: str

@router.post("/run_pipeline", response_model=PipelineOutput)
def run_salesforce_to_google_ads_pipeline(input_data: SalesforceQueryInput) -> PipelineOutput:
    """
    Run the pipeline to transfer data from Salesforce to Google Ads.

    Steps:
    1) Retrieve data from Salesforce using the provided SOQL query.
    2) Store the raw Salesforce data in Google Cloud Storage.
    3) Format the data for Google Ads.
    4) Store the formatted data in Google Cloud Storage.
    5) Upload the formatted data to Google Ads.

    :param input_data: SalesforceQueryInput containing the SOQL query.
    :return: PipelineOutput indicating success or failure.
    """
    # Step 1: Retrieve data from Salesforce
    salesforce_data = query_salesforce_data(input_data.query)

    # Step 2: Store the raw Salesforce data in Google Cloud Storage
    store_data_in_gcs(str(salesforce_data), "raw_salesforce_data.json")

    # Step 3: Format the data for Google Ads
    formatted_data = format_data_for_google_ads(salesforce_data)

    # Step 4: Store the formatted data in Google Cloud Storage
    store_data_in_gcs(str(formatted_data), "formatted_google_ads_data.json")

    # Step 5: Upload the formatted data to Google Ads
    upload_to_google_ads(formatted_data)

    return PipelineOutput(success=True, message="Pipeline executed successfully.")
