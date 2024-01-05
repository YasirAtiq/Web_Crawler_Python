from bs4 import BeautifulSoup as Parser
from urllib.parse import urljoin
import requests
import time


def renew(links_input, allowed_suffixes=None):
    if allowed_suffixes is None:
        allowed_suffixes = [""]
    new_links = list(dict.fromkeys(links_input).keys())
    if "/" in new_links:
        new_links.remove("/")
    new_links = [link for link in new_links if link[-1] in allowed_suffixes or link.endswith("")]
    new_links = [link for link in new_links if link.startswith("/")]
    return new_links


def fetch_links(rate_limit, url, depth, max_depth, suffixes):
    if depth > max_depth:
        return []
    try:
        response = requests.get(url, verify=False)
    except requests.exceptions.SSLError:
        print(f"SSL error for URL: {url}")
        return []
    soup = Parser(response.content, features='html.parser')
    links = [link["href"] for link in soup.find_all("a", href=True)]
    links = renew(links, suffixes)

    depth_links = []
    for link in links:
        time.sleep(rate_limit)
        full_link = urljoin(url, link)
        depth_links.extend(fetch_links(rate_limit, full_link, depth + 1, max_depth, suffixes))

    return [(url, links)] + depth_links


def main():
    rate_limit = 2.5  # In Seconds
    url = input("Enter URL: ")
    try:
        max_depth = int(input("Enter MAX Depth: "))
    except ValueError:
        max_depth = 1

    suffixes = [".html", ".php"]

    result = fetch_links(rate_limit, url, 1, max_depth, suffixes)
    print(result)


if __name__ == "__main__":
    main()
