# beauty_soup.py

from bs4 import BeautifulSoup
import ssl
from urllib.request import Request, urlopen

def getContent(urlLink):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = Request(
        url=urlLink, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    try:
        page = urlopen(req, context=ctx)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        return soup.get_text();
    except Exception as e:
        print(f"An error occurred - Unable to fetch URL: {urlLink}, {e}")
        return ""
    
print(getContent("https://www.forbes.com/sites/digital-assets/2024/01/12/100-billion-bitcoin-and-crypto-etf-price-crash-suddenly-accelerates-after-serious-fed-warning-hitting-ethereum-xrp-and-solana/"))