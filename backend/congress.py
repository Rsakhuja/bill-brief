import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from app import process_file

app = Flask(__name__)

'''
1. Get all bills within hour long timeframe
2. For each bill, get text content
3. Convert content into some kind of form that's readable for llm
4. Post the llm response to twitter
'''

def get_all_bills_hour_timeframe(base_url, congress_number, api_key):
    url = base_url + "/" + congress_number + "?"
    
    if not api_key:
        raise ValueError("API Key not found. Please check your .env file")
    
    utc_now = datetime.now(tz=pytz.UTC)
    one_hour_ago = utc_now - timedelta(hours=1)

    fromDateTime = one_hour_ago.strftime("%Y-%m-%dT%H:%M:%SZ")
    toDateTime = utc_now.strftime("%Y-%m-%dT%H:%M:%SZ")

    params = {
        'api_key': api_key,
        'fromDateTime': fromDateTime,
        'toDateTime': toDateTime,
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return {"error": "Error fetching latest bills"}

    return response.json()

def get_pdf_url_and_number(base_url, congress_number, api_key, bill):
     base_url = os.getenv("CONGRESS_API_URL")
     congress_number = os.getenv("CURRENT_CONGRESS_NUMBER")
     api_key = os.getenv("CONGRESS_API_KEY")
    
     bill_number = bill["number"]
     api_url = base_url + "/" + congress_number + "/" + bill_number + "/text"

     params = {
          "format": "json",
          "api_key": api_key,
     }

     content = requests.get(api_url, params)
     data = content.json()
     url = data["textVersions"][0]["formats"][1]["url"]
     return url, bill_number

def process_content(url, bill_number):
    bill = requests.get(url)
    file = open("llm_implementation/data/" + bill_number)
    file.write(bill.content)
    file.close()

def fetch_latest_bills():
    load_dotenv()
    
    base_url = os.getenv("CONGRESS_API_URL")
    congress_number = os.getenv("CURRENT_CONGRESS_NUMBER")
    api_key = os.getenv("CONGRESS_API_KEY")

    '''1. Get all bills within hour long timeframe'''
    fetched_bills_response = get_all_bills_hour_timeframe(base_url=base_url, congress_number=congress_number, api_key=api_key)
    if "bills" not in fetched_bills_response:
        return
    
    '''2. For each bill, get text content and put it through llm'''
    for bill in fetched_bills_response["bills"]:
         content_url, bill_number = get_pdf_url_and_number(base_url, congress_number, api_key, bill=bill)
         process_content(content_url, bill_number)


fetch_latest_bills()
# scheduler = BackgroundScheduler()
# scheduler.add_job(fetch_latest_bills, 'interval', hours=1)
# scheduler.start()

# if __name__ == '__main__':
#     app.run()