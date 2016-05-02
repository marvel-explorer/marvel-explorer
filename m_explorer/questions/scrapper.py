"""Scrapper to produce character information."""
from bs4 import BeautifulSoup
import requests
import io
import re
import sys
import os.path

MARVEL_UNIVERSE_DOMAIN = 'http://marvel.com/universe/'
CHARACTER = 'Black_Widow_(Natasha_Romanova)'


def get_page():
    "Return content and encoding of desired page."
    url = MARVEL_UNIVERSE_DOMAIN + CHARACTER
    resp = requests.get(url)
    if resp.status == "OK":
        return resp.content, resp.encoding
    resp.raise_for_status


def write_file(html, name):
    "Write the response html to file"
    file = open(name, "w")
    file.write(html)
    file.close()


def load_page(name):
    """Return html page from file."""
    if not os.path.isfile(name):
        content, encoding = get_page()
        write_file(content.decode(encoding), name)
    file = io.open(name, "r")
    return file


def parse_source(html):
    """Return parsed html."""
    parsed = BeautifulSoup(html, 'html5lib')
    return parsed


def extract_marvel_u_data(html):
    """Extract div of correct id from marvl u."""
    div_finder = html.find('div', id='powerbox')  # May need to invoke alternate search
    return div_finder


def p_components_marvelu(html):
    """Extract initial stats from powerbox."""
    p_tags = html.find_all('p')
    for p in p_tags:
        print(p.b.string)
        print(p.b.next_sibling.next_sibling)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        html = load_page(CHARACTER + '.html')
    else:
        html = get_page()
    doc = parse_source(html)
    doc = extract_marvel_u_data(doc)
    p_components_marvelu(doc)
