from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.salesforce.query_salesforce_data import query_salesforce_data
from app.pipeline.filter_unsaved_conversions import filter_unsaved_conversions
from app.google_ads.upload_conversions import upload_conversions
from app.modassembly.database.sql.get_sql_session import get_sql_session


router = APIRouter()


@router.post("/run")
def run_upload_pipeline(
    session: Session = Depends(get_sql_session),
) -> str:
    """
    Run the pipeline to transfer data from Salesforce to Google Ads.

    This endpoint retrieves data from Salesforce, checks for existing records
    in the Opportunity database model, formats the data for Google Ads, and
    uploads it to Google Ads.

    Returns:
        PipelineOutput: A response model indicating the success or failure of the pipeline.
    """
    records = query_salesforce_data()
    formatted_data = filter_unsaved_conversions(session, records)
    upload_conversions(formatted_data)
    return "Pipeline executed successfully."
