from bs4 import BeautifulSoup as Parser
import requests


def renew(links_input, allowed_suffixes=None):
    if allowed_suffixes is None:
        allowed_suffixes = [""]
    new_links = list({}.fromkeys(links_input).keys())
    new_links.remove("/")
    new_links = [link for link in new_links if link[-1] in allowed_suffixes or link.endswith("")]
    new_links = [link for link in new_links if link.startswith("/")]
    return new_links


def main():
    url = input("Enter URL: ")
    max_depth = int(input("Enter MAX Depth: "))
    suffixes = [".html", ".php"]

    response = requests.get(url)
    soup = Parser(response.content, features='html.parser')
    links = [link["href"] for link in soup.find_all("a", href=True)]
    print(renew(links, suffixes))


if __name__ == "__main__":
    main()
