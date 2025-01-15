from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from app.query_salesforce_data import query_salesforce_data
from app.format_data_for_google_ads import format_data_for_google_ads
from app.upload_to_google_ads import upload_to_google_ads
from app.Opportunity import Opportunity
from app.get_sql_session import get_sql_session

router = APIRouter()

class PipelineOutput(BaseModel):
    success: bool
    message: str

@router.post("/run_pipeline", response_model=PipelineOutput)
def run_salesforce_to_google_ads_pipeline() -> PipelineOutput:
    """
    Run the pipeline to transfer data from Salesforce to Google Ads.

    This endpoint retrieves data from Salesforce, checks for existing records
    in the Opportunity database model, formats the data for Google Ads, and
    uploads it to Google Ads.

    Returns:
        PipelineOutput: A response model indicating the success or failure of the pipeline.
    """
    try:
        # Retrieve data from Salesforce
        salesforce_data = query_salesforce_data()

        # Open a new SQL session
        with get_sql_session() as session:
            # Check and store new records in the Opportunity dbmodel
            for record in salesforce_data:
                if not session.query(Opportunity).filter(Opportunity.Id == record['Id'].__str__()).first():
                    new_opportunity = Opportunity(
                        Id=record['Id'].__str__(),
                        GCLID__c=record['GCLID__c'].__str__(),
                        CreatedDate=record['CreatedDate'],
                        Admission_Date__c=record['Admission_Date__c']
                    )
                    session.add(new_opportunity)
            session.commit()

        # Format the data for Google Ads
        formatted_data = format_data_for_google_ads(salesforce_data)

        # Upload the formatted data to Google Ads
        for data in formatted_data:
            upload_to_google_ads(data)

        return PipelineOutput(success=True, message="Pipeline executed successfully.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Pipeline execution failed: {str(e)}")
