import requests
from bs4 import BeautifulSoup
from langchain.tools import tool
from urllib.parse import urlparse
from utils.text import clean_text

def is_valid_url(url: str) -> bool:
    """
    Validate URL.
    """

    parsed = urlparse(url)

    return bool(parsed.netloc) and bool(parsed.scheme)

@tool
def scrape_url(url: str) -> str:

    """
    Scrape webpage and return clean text.
    """

    if not is_valid_url(url):

        return "Invalid URL."

    try:

        response = requests.get(

            url,

            timeout=10,

            headers={

                "User-Agent":

                "Mozilla/5.0"

            }

        )

        response.raise_for_status()

        soup = BeautifulSoup(

            response.text,

            "lxml"

        )

        for tag in soup(

            [

                "script",

                "style",

                "nav",

                "footer",

                "header",

                "noscript",

                "svg",

                "img",

                "iframe",

                "aside"

            ]

        ):

            tag.decompose()

        text = soup.get_text(

            separator=" ",

            strip=True

        )

        text = clean_text(text)

        return text[:5000]

    except Exception as e:

        return f"Scraping Error : {e}"