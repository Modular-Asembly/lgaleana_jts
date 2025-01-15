import requests
from typing import List, Dict, Any
from datetime import datetime, timedelta
from app.salesforce.get_auth_data import get_auth_data

def query_salesforce_data() -> List[Dict[str, Any]]:
    # Retrieve Salesforce authentication data
    auth_data = get_auth_data()
    instance_url = auth_data['instance_url']
    access_token = auth_data['access_token']

    # Calculate the date 90 days ago from today
    ninety_days_ago = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Construct the SOQL query
    soql_query = (
        "SELECT Id, GCLID__c, CreatedDate, Admission_Date__c "
        "FROM Opportunity "
        "WHERE StageName IN ('Admitted', 'Alumni') "
        f"AND CreatedDate >= {ninety_days_ago}"
    )

    # Construct the query URL
    query_url = f"{instance_url}/services/data/vXX.X/query?q={soql_query}"

    # Send a GET request to the query URL with the appropriate headers
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(query_url, headers=headers)
    response.raise_for_status()

    # Filter the results to include only records where GCLID__c is not None
    records = response.json().get('records', [])
    filtered_records = [record for record in records if record.get('GCLID__c') is not None]

    return filtered_records
