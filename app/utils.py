import re
from urllib.parse import urlparse
from app.logger import logger

def extract_domain(url):
    """
    Extract and normalize the domain from various URL formats.
    
    Args:
    url (str): The URL or domain string to process.
    
    Returns:
    str: The extracted and normalized domain, or None if extraction fails.
    """
    logger.info(f"Attempting to extract domain from: {url}")
    
    # If the url doesn't start with a scheme, add 'https://' as a default
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    try:
        # Parse the URL
        parsed_url = urlparse(url)
        
        # Extract the domain (netloc)
        domain = parsed_url.netloc
        
        # Remove 'www.' if present
        domain = re.sub(r'^www\.', '', domain)
        
        # Ensure we have a domain
        if not domain:
            logger.warning(f"Failed to extract domain from: {url}")
            return None
        
        # Normalize to 'www.domain.com' format
        normalized_domain = f"www.{domain}"
        
        logger.info(f"Successfully extracted and normalized domain: {normalized_domain}")
        return normalized_domain
    
    except Exception as e:
        logger.error(f"Error extracting domain from {url}: {str(e)}")
        return None