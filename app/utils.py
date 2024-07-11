import re

def extract_domain(url):
    pattern = r"(?:https?:\/\/)?(?:www\.)?([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
    match = re.search(pattern, url)
    return f"www.{match.group(1)}" if match else None