from typing import List, Dict, Any
from app.models.Opportunity import Opportunity

def format_data_for_google_ads(salesforce_data: List[Opportunity]) -> List[Dict[str, Any]]:
    formatted_data = []

    for record in salesforce_data:
        formatted_record = {
            "id": record.Id.__str__(),
            "gclid": record.GCLID__c.__str__() if record.GCLID__c else None,
            "created_date": record.CreatedDate.isoformat(),
            "admission_date": record.Admission_Date__c.isoformat() if record.Admission_Date__c else None,
            "type": "Opportunity",
            "url": f"https://example.salesforce.com/{record.Id.__str__()}"
        }
        formatted_data.append(formatted_record)

    return formatted_data
