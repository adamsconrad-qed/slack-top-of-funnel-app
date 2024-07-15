import requests
from app.config import PITCHBOOK_API_TOKEN, PITCHBOOK_API_BASE_URL, PITCHBOOK_API_BASE_URL_V2

PITCHBOOK_HEADERS = {"Authorization": f"PB-Token {PITCHBOOK_API_TOKEN}"}

def search_company(domain):
    url = f"{PITCHBOOK_API_BASE_URL}companies/search"
    params = {"companyNames": domain}
    response = requests.get(url, headers=PITCHBOOK_HEADERS, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["stats"]["total"] > 0:
            return data["items"][0]["companyId"]
    return None

def search_investors(company_id):
    url = f"{PITCHBOOK_API_BASE_URL}investors/search"
    params = {"companyNames": company_id}
    response = requests.get(url, headers=PITCHBOOK_HEADERS, params=params)
    if response.status_code == 200:
        data = response.json()
        return [item["investorName"] for item in data["items"]]
    return []

def get_company_bio(company_id):
    url = f"{PITCHBOOK_API_BASE_URL_V2}companies/{company_id}/bio"
    response = requests.get(url, headers=PITCHBOOK_HEADERS)
    if response.status_code == 200:
        return response.json()
    return None
