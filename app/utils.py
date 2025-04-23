import re
from urllib.parse import urlparse
from app.logger import logger

def extract_domain(url):
    # Define a regular expression pattern for extracting the domain
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url)
    pattern = r"(https?://)?(www\d?\.)?(?P<domain>[\w\.-]+\.\w+)(/\S*)?"
    
    if not urls:  # Check if any URLs were found
        logger.info(f"No URLs found in text: {url}")
        return None
        
    try:
        match = re.match(pattern, urls[0])
        if match:
            domain = match.group("domain")
            logger.info(f"Successfully extracted domain: {domain}")
            return domain
    except Exception as e:
        logger.error(f"Error extracting domain: {str(e)}")
    
    return None
