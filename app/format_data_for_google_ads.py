from typing import List, Dict, Any
from app.Opportunity import Opportunity

def format_data_for_google_ads(salesforce_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Transforms Salesforce data into the format required by Google Ads.

    Args:
        salesforce_data (List[Dict[str, Any]]): The list of Salesforce data records.

    Returns:
        List[Dict[str, Any]]: The formatted data for Google Ads.
    """
    formatted_data = []

    for record in salesforce_data:
        formatted_record = {
            "id": record["Id"].__str__(),
            "gclid": record["GCLID__c"].__str__() if record["GCLID__c"] else None,
            "created_date": record["CreatedDate"].isoformat() if record["CreatedDate"] else None,
            "admission_date": record["Admission_Date__c"].isoformat() if record["Admission_Date__c"] else None
        }
        formatted_data.append(formatted_record)

    return formatted_data
