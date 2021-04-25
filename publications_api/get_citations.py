from pathlib import Path
from typing import List
from urllib.parse import urlparse, parse_qs

import frontmatter
import requests
import bs4
from bs4 import BeautifulSoup

# Types:
Tag = bs4.element.Tag

"""
Example of PURE API endpoint
https://pure.itu.dk/ws/api/520/research-outputs?apiKey={the api key}&publication-status=/dk/atira/pure/researchoutput/status/published
"""

def parse_markdown(author: Path) -> dict:
    """
    Gets the frontmatter from {author}/_index.md.
    """
    with open(author / "_index.md") as fp:
        content = fp.read()
    
    content = frontmatter.loads(content)
    return content.to_dict()

def get_scholar_link(author: Path) -> str:
    """
    Gets the scholar link inside {author}/_index.md,
    and returns None if the author hasn't updated
    the default link
    (https://scholar.google.co.uk/citations?user=sIwtMXoAAAAJ)
    """
    author_metadata = parse_markdown(author)
    default_link = "https://scholar.google.co.uk/citations?user=sIwtMXoAAAAJ"
    
    social_links = author_metadata["social"]
    social_links = {
        l["icon"]: l["link"] for l in social_links
    }
    if "graduation-cap" not in social_links:
        return None
    
    if social_links["graduation-cap"] == default_link:
        return None
    
    return social_links["graduation-cap"]

def get_author_id(scholar_link: str) -> str:
    """
    scholar.google links are usually structured like this:
    https://scholar.google.com/citations?user={author_id}&{other stuff}

    This function parses the link and returns the author id.
    """
    # urlparse returns a named tuple
    # with the query at pos 4.
    parsed_url = urlparse(scholar_link)
    query = parse_qs(parsed_url[4])
    return query["user"]

def parse_row(tr: Tag) -> dict:
    """
    When parsing the Google Scholar site,
    we get a table full of our citations.
    This function parses each one of those rows.
    """
    title = tr.find("td", {"class": "gsc_a_t"})
    authors = title.div # TODO: This might not return the list of authors.
    year = tr.find("td", {"class": "gsc_a_y"})
    return {
        "title": title.a.text,
        "authors": authors.text,
        "year": year.text
    }

def get_publications(author: Path, limit=None) -> List[str]:
    """
    Gets the publications in Google Scholar
    for author in {author}/_index.md
    """
    res = requests.get(
        get_scholar_link(author) + "&view_op=list_works&sortby=pubdate"
    )
    page = res.content
    soup = BeautifulSoup(page, "html.parser")
    all_rows = soup.find_all("tr", {"class": "gsc_a_tr"}, limit=limit)
    publications = {
        parse_row(row) for row in all_rows
    }

    return publications


def main() -> None:
    base_path = Path("..")
    all_author_folders = base_path.glob("./content/authors/*/")
    all_author_folders = [author_folder for author_folder in all_author_folders if author_folder.is_dir()]

    for author in all_author_folders[:3]:
        print("="*50)
        print(author)
        scholar_link = get_scholar_link(author)
        print(scholar_link or "Hasn't updated scholar link.")
        if scholar_link is not None:
            print(get_publications(author))

if __name__ == "__main__":
    main()
