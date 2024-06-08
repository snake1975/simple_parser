import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    """
    Fetches the content of a webpage.

    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: The content of the webpage.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    return response.text

def parse_links(html_content):
    """
    Parses the HTML content and extracts all links.

    Args:
        html_content (str): The HTML content of the webpage.

    Returns:
        list: A list of URLs found in the HTML content.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    links = []
    for link in soup.find_all('a', href=True):
        links.append(link['href'])
    return links

def main(url):
    """
    The main function that fetches a webpage and prints all links found on it.

    Args:
        url (str): The URL of the webpage to parse.
    """
    try:
        html_content = fetch_webpage(url)
        links = parse_links(html_content)
        print(f"Found {len(links)} links:")
        for link in links:
            print(link)
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example URL
    url = "https://www.web.de"
    main(url)

