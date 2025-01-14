from typing import Any, Dict
from simple_salesforce import Salesforce
from app.salesforce.get_salesforce_access_token import get_salesforce_access_token

def query_salesforce_data(query: str) -> Dict[str, Any]:
    # Step 1: Obtain Salesforce credentials
    credentials = get_salesforce_access_token()
    access_token = credentials['access_token']
    instance_url = credentials['instance_url']
    
    # Step 2: Connect to Salesforce API
    sf = Salesforce(instance_url=instance_url, session_id=access_token)
    
    # Step 3: Query the required data
    result = sf.query(query)
    
    # Step 4: Return the data
    return result
