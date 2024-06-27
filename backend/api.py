import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
import pytz
from llm_implementation.rag import analyze
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

app = Flask(__name__)

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
        
        for bill in data["bills"]:
            title = bill["number"]

            base, _ = test.split("?")
            new_url = base + "/text" 
            
            bill_content_params = {
                'api_key': api_key,
                'format': 'json'
            }

            content_resp = requests.get(new_url, params=bill_content_params)
            if content_resp.status_code == 200:
                data = content_resp.json()
                url = data["textVersions"][0]["formats"][1]["url"]

                resp = requests.get(url)
                
                os.mkdir("llm_implementation/data/" + title)
                file = open("llm_implementation/data/" + title + "/" + title + ".pdf", "wb")
                file.write(resp.content)
                file.close()

                # rag.analyze("llm_implementation/data/test/test.pdf")            

    else:
        print(f"Failed to fetch data: {response.status_code}")


scheduler = BackgroundScheduler()
scheduler.add_job(fetch_latest_bills, 'interval', hours=1)
scheduler.start()

if __name__ == '__main__':
    app.run()