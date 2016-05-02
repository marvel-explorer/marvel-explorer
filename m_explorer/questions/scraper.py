"""Scrapper to produce character information."""
from bs4 import BeautifulSoup
import requests
import io
import re
import sys
import os.path

MARVEL_UNIVERSE_DOMAIN = 'http://marvel.com/universe/'
CHARACTER = 'She-Hulk'


def get_page(character=CHARACTER):
    "Return content and encoding of desired page."
    url = MARVEL_UNIVERSE_DOMAIN + character
    resp = requests.get(url)
    resp.raise_for_status
    return resp.content, resp.encoding


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


def marvel_u_correct_page():
    """Search page for correct content or redirects to correct page."""


def extract_marvel_u_data(html):
    """Extract div of correct id from marvl u."""
    div_finder = html.find('div', id='powerbox')  # May need to invoke alternate search
    if div_finder:
        return div_finder
    else:
        # log = open("fail.log", "w")
        # try:
        div_finder = html.find('div', {'class': 'gallerytext'})
        char_link = div_finder.a.get('href').split('/')[-1]
        return marvel_u_call(char_link)
#         except:

# logf = open("download.log", "w")
# for download in download_list:
#     try:
#         # code to process download here
#     except Exception as e:     # most generic exception you can catch
#         logf.write("Failed to download {0}: {1}\n".format(str(download), str(e)))
#         # optional: delete local version of failed download
#     finally:
#         # optional clean up code
#         pass


def marvel_u_call(charcter=CHARACTER):
    """Initial controller for call before tag isolation."""
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        html = load_page(charcter + '.html')
    else:
        html = get_page()
    doc = parse_source(html)
    doc = extract_marvel_u_data(doc)
    return doc


def clean_data(data):
    """Return data free of excess spaces and new lines."""
    try:
        return data.strip(" \n:-")
    except (AttributeError, TypeError):
        return u""


def p_components_marvelu(html):
    """Extract initial stats from powerbox."""
    p_tags = html.find_all('p')
    p_dict = {}
    for p in p_tags:
        try:
            label = clean_data(p.b.string)
            value = clean_data(p.b.next_sibling.next_sibling)
            p_dict.setdefault(label, []).append(value)
        except AttributeError:
            continue
    print(p_dict)  # Gives p value in dict form. :)


def div_components_marvelu(html):
    divs = html.find_all('div', {'class': 'myLink'})
    div_dict = {}
    for div in divs:
        try:
            contents = div.contents
            label = clean_data(contents[0].string)
            value = clean_data(contents[1].text)
            div_dict.setdefault(label, []).append(value)
        except IndexError:
            continue
    print(div_dict)

if __name__ == '__main__':
    # if len(sys.argv) > 1 and sys.argv[1] == 'test':
    #     html = load_page(CHARACTER + '.html')
    # else:
    #     html = get_page()
    # doc = parse_source(html)
    # doc = extract_marvel_u_data(doc)
    doc = marvel_u_call()
    if doc:
        p_components_marvelu(doc)
        div_components_marvelu(doc)
