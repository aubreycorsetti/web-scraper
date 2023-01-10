import requests
import re
from bs4 import BeautifulSoup

user_input_url = input('> Input the URL you with to search for citations: ')
url_match = re.search(r"https://[^ ]+", user_input_url)
parsed_url = url_match.group(0)


def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    citations_needed = soup.find_all("a", title="Wikipedia:Citation needed")
    citation_count = len(citations_needed)

    print(citation_count)
    return citation_count


def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    citations_needed = soup.find_all("sup", class_="noprint Inline-Template Template-Fact")
    statements_needing_citations = 'The following statements need citations:`n'

    for element in citations_needed:
        statements_needing_citations += element.parent.get_text() + "\n"

    print(str(statements_needing_citations))
    return str(statements_needing_citations)


get_citations_needed_count(parsed_url)
get_citations_needed_report(parsed_url)


if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/History_of_Mexico"
    get_citations_needed_count(url)
    get_citations_needed_report(url)
