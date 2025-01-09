import os
from simple_salesforce import Salesforce
from typing import Any, Dict, List

def query_salesforce_data() -> List[Dict[str, Any]]:
    # Connect to Salesforce using environment variables for credentials
    sf = Salesforce(
        username=os.environ['SALESFORCE_USERNAME'],
        password=os.environ['SALESFORCE_PASSWORD'],
        security_token=os.environ['SALESFORCE_SECURITY_TOKEN']
    )
    
    # Example SOQL query to retrieve data
    query = "SELECT Id, Name FROM Account LIMIT 10"
    
    # Execute the query
    result = sf.query(query)
    
    # Return the records from the query result
    return result['records']
