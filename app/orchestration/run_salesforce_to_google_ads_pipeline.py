from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from app.salesforce.query_salesforce_data import query_salesforce_data
from app.data_processing.format_data_for_google_ads import format_data_for_google_ads
from app.google_ads.upload_to_google_ads import upload_to_google_ads
from app.models.Opportunity import Opportunity
from app.modassembly.database.sql.get_sql_session import get_sql_session

router = APIRouter()

class PipelineOutput(BaseModel):
    success: bool
    message: str

@router.post("/run_pipeline", response_model=PipelineOutput)
def run_salesforce_to_google_ads_pipeline() -> PipelineOutput:
    try:
        # Step 1: Retrieve data from Salesforce
        salesforce_data = query_salesforce_data()

        # Step 2: Check if each record exists in the Opportunity dbmodel
        with get_sql_session() as session:
            for record in salesforce_data:
                opportunity = session.query(Opportunity).filter_by(Id=record['Id'].__str__()).first()
                if not opportunity:
                    # Step 3: Store it in the Opportunity dbmodel if it doesn't exist
                    new_opportunity = Opportunity(
                        Id=record['Id'].__str__(),
                        GCLID=record['GCLID__c'].__str__(),
                        CreatedDate=record['CreatedDate'],
                        Admission_Date=record['Admission_Date__c'],
                        type=record['attributes']['type'].__str__(),
                        url=record['attributes']['url'].__str__()
                    )
                    session.add(new_opportunity)
                    session.commit()

        # Step 4: Format the data for Google Ads
        formatted_data = format_data_for_google_ads(salesforce_data)

        # Step 5: Upload the formatted data to Google Ads
        for data in formatted_data:
            upload_to_google_ads(data)

        # Step 6: Return a PipelineOutput indicating success
        return PipelineOutput(success=True, message="Pipeline executed successfully.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
