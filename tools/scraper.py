import requests

from bs4 import BeautifulSoup

from langchain.tools import tool

@tool
def scrape_url(url: str) -> str:
    """
    Scrape a webpage and return cleaned text.
    """

    headers = {

        "User-Agent":
        (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64)"
        )

    }

    response = requests.get(

        url,

        headers=headers,

        timeout=15,

    )

    response.raise_for_status()

    soup = BeautifulSoup(

        response.text,

        "html.parser",

    )

    remove_tags = [

        "script",

        "style",

        "header",

        "footer",

        "nav",

        "aside",

        "noscript",

        "svg",

        "form",

    ]

    for tag in soup(remove_tags):

        tag.decompose()

    text = soup.get_text(

        separator=" ",

        strip=True,

    )

    return text[:7000]