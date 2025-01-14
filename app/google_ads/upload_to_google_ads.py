from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException
from typing import Any, Dict

def upload_to_google_ads(formatted_data: Dict[str, Any]) -> None:
    # Initialize the Google Ads client
    client = GoogleAdsClient.load_from_storage()

    # Assuming the formatted_data contains the necessary information to create a campaign
    # This is a simplified example and may need to be adjusted based on your actual data structure
    try:
        # Example: Uploading a campaign
        campaign_service = client.get_service("CampaignService", version="v11")
        campaign_operation = client.get_type("CampaignOperation", version="v11")
        campaign = campaign_operation.create

        # Set the campaign details from formatted_data
        campaign.name = formatted_data["name"]
        campaign.advertising_channel_type = formatted_data["advertising_channel_type"]
        campaign.status = formatted_data["status"]

        # Add more fields as necessary based on your data and requirements

        # Send the operation to the API
        response = campaign_service.mutate_campaigns(
            customer_id=formatted_data["customer_id"],
            operations=[campaign_operation]
        )

        print(f"Uploaded campaign with resource name: {response.results[0].resource_name}")

    except GoogleAdsException as ex:
        print(f"Request failed with status {ex.error.code().name} and includes the following errors:")
        for error in ex.failure.errors:
            print(f"\tError with message: {error.message}")
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print(f"\t\tOn field: {field_path_element.field_name}")
        raise

