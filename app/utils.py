import re
from urllib.parse import urlparse
from app.logger import logger

def extract_domain(url):
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url)
    return urls[0]
