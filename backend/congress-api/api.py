import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
import pytz

def fetch_latest_bills():
    load_dotenv()
    
    base_url = os.getenv("CONGRESS_API_URL")
    congress_number = os.getenv("CURRENT_CONGRESS_NUMBER")

    api_key = os.getenv("CONGRESS_API_KEY")
    api_url = base_url + "/" + congress_number + "?"

    if not api_key:
        raise ValueError("API Key not found. Please check your .en")
    
    utc_now = datetime.now(tz=pytz.UTC)
    one_hour_ago = utc_now - timedelta(hours=1)

    fromDateTime = one_hour_ago.strftime("%Y-%m-%dT%H:%M:%SZ")
    toDateTime = utc_now.strftime("%Y-%m-%dT%H:%M:%SZ")

    params = {
        'api_key': api_key,
        'fromDateTime': fromDateTime,
        'toDateTime': toDateTime,
        'sort': 'updateDate+asc',
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()

        if "bills" not in data:
            return 
        
        test = data["bills"][0]["url"]
        base, _ = test.split("?")
        new_url = base + "/text" 
        
        bill_content_params = {
            'api_key': api_key,
            'format': 'json'
        }

        content_resp = requests.get(new_url, params=bill_content_params)
        if content_resp.status_code == 200:
            data = content_resp.json()
            print(data["textVersions"][0]["formats"][1])

    else:
        print(f"Failed to fetch data: {response.status_code}")


fetch_latest_bills()