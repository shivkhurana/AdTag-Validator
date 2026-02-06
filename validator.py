import requests
from bs4 import BeautifulSoup
import time

def validate_url(url):
    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        latency = (time.time() - start) * 1000

        # Check 1: HTTP Status
        if response.status_code != 200:
            return {"status": "FAIL", "reason": f"HTTP {response.status_code}"}

        # Check 2: Ad Tag Presence
        soup = BeautifulSoup(response.text, 'html.parser')
        ad_tag = soup.find('script', src=lambda s: s and 'googletagservices' in s)
        
        if not ad_tag:
            return {"status": "FAIL", "reason": "Missing Ad Tag"}
            
        return {"status": "PASS", "latency_ms": round(latency, 2)}

    except Exception as e:
        return {"status": "ERROR", "reason": str(e)}