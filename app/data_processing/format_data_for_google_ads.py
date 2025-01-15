from typing import List, Dict, Any
from app.models.Opportunity import Opportunity

def format_data_for_google_ads(salesforce_data: List[Opportunity]) -> List[Dict[str, Any]]:
    formatted_data = []

    for record in salesforce_data:
        formatted_record = {
            "id": record.Id.__str__(),
            "gclid": record.GCLID.__str__() if record.GCLID else None,
            "created_date": record.CreatedDate.isoformat(),
            "admission_date": record.Admission_Date.isoformat() if record.Admission_Date else None,
            "type": record.type.__str__(),
            "url": record.url.__str__()
        }
        formatted_data.append(formatted_record)

    return formatted_data
