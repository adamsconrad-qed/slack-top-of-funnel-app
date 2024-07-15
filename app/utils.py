import re
from urllib.parse import urlparse
from app.logger import logger

def extract_domain(url):
  # Define a regular expression pattern for extracting the domain
  urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url)
  pattern = r"(https?://)?(www\d?\.)?(?P<domain>[\w\.-]+\.\w+)(/\S*)?"
  # Use re.match to search for the pattern at the beginning of the URL
  if urls[0]:
    match = re.match(pattern, urls[0])
  # Check if a match is found
    if match:
  # Extract the domain from the named group "domain"
      domain = match.group("domain")
      return domain
  else:
    return None
