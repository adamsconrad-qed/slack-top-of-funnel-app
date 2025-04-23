import requests
from app.config import PITCHBOOK_API_TOKEN, PITCHBOOK_API_BASE_URL, PITCHBOOK_API_BASE_URL_V2
from app.logger import logger

PITCHBOOK_HEADERS = {"Authorization": f"PB-Token {PITCHBOOK_API_TOKEN}"}

def search_company(domain):
    url = f"{PITCHBOOK_API_BASE_URL}companies/search"
    params = {"companyNames": domain}
    try:
        response = requests.get(url, headers=PITCHBOOK_HEADERS, params=params)
        logger.info(f"PitchBook API response status: {response.status_code}")
        logger.info(f"PitchBook API response: {response.text}")
        
        if response.status_code == 200:
            data = response.json()
            if data["stats"]["total"] > 0:
                company_id = data["items"][0]["companyId"]
                logger.info(f"Found company ID: {company_id}")
                return company_id
            else:
                logger.info(f"No companies found for domain: {domain}")
        else:
            logger.error(f"PitchBook API error: {response.status_code}")
    except Exception as e:
        logger.error(f"Error in search_company: {str(e)}")
    return None

def search_investors(company_id):
    url = f"{PITCHBOOK_API_BASE_URL}investors/search"
    params = {"companyNames": company_id}
    try:
        response = requests.get(url, headers=PITCHBOOK_HEADERS, params=params)
        logger.info(f"Investors API response status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            investors = [item["investorName"] for item in data["items"]]
            logger.info(f"Found {len(investors)} investors")
            return investors
        else:
            logger.error(f"Investors API error: {response.status_code}")
    except Exception as e:
        logger.error(f"Error in search_investors: {str(e)}")
    return []

def get_company_bio(company_id):
    url = f"{PITCHBOOK_API_BASE_URL_V2}companies/{company_id}/bio"
    try:
        response = requests.get(url, headers=PITCHBOOK_HEADERS)
        logger.info(f"Bio API response status: {response.status_code}")
        logger.info(f"Bio API response: {response.text}")
        
        if response.status_code == 200:
            data = response.json()
            if data:
                logger.info(f"Successfully retrieved bio for company: {company_id}")
                return data
            else:
                logger.error("Empty response from bio API")
        else:
            logger.error(f"Bio API error: {response.status_code}")
    except Exception as e:
        logger.error(f"Error in get_company_bio: {str(e)}")
    return None
