"""Scrapper to produce character information."""
from bs4 import BeautifulSoup
import requests
import io
import re
import sys
import os.path

MARVEL_UNIVERSE_DOMAIN = 'http://marvel.com/universe/'


def character_list(text_file):
    """Translate a text_file into a list of characters to search."""
    with open(text_file) as file:
        char_list = file.read().splitlines()
    return char_list

CHARACTER = character_list('characters.txt')


def get_page(character):
    "Return content and encoding of desired page."
    url = MARVEL_UNIVERSE_DOMAIN + character
    resp = requests.get(url)
    resp.raise_for_status
    return resp.content, resp.encoding


def write_file(html, name):
    "Write the response html to file"
    file = open(name, "w")
    file.write(html.encode('ascii', 'ignore'))
    file.close()


def load_page(name):
    """Return html page from file."""
    if not os.path.isfile(name):
        content, encoding = get_page(name[:-5])
        write_file(content.decode(encoding), name)
    file = io.open(name, "r")
    return file


def parse_source(html):
    """Return parsed html."""
    parsed = BeautifulSoup(html, 'html5lib')
    return parsed


def extract_marvel_u_data(html):
    """Extract div of correct id from marvl u."""
    log = open("search.log", "a")
    div_finder = html.find('div', id='powerbox')  # May need to invoke alternate search
    if div_finder:
        log.write("Found:{}.format\n".format(str(html.title)))
        return div_finder
    else:
        try:
            div_finder = html.find('div', {'class': 'gallerytext'})
            char_link = div_finder.a.get('href').split('/')[-1]
            log.write("Found:{}.format\n".format(str(html.title)))
            return marvel_u_call(char_link)
        except:
            log.write("Failed to find:{}\n".format(str(html.title)))


def marvel_u_call(character):
    """Initial controller for call before tag isolation."""
    # if len(sys.argv) > 1 and sys.argv[1] == 'test':
    #     html = load_page(character + '.html')
    # else:
    html, encoding = get_page(character)
    doc = parse_source(html.decode(encoding))
    doc = extract_marvel_u_data(doc)
    return doc


def clean_data(data):
    """Return data free of excess spaces and new lines."""
    try:
        return data.strip(" \n:-")
    except (AttributeError, TypeError):
        return u""


def p_components_marvelu(html):
    """Return extracted initial stats from powerbox."""
    p_tags = html.find_all('p')
    p_dict = {}
    for p in p_tags:
        try:
            label = clean_data(p.b.string)
            value = clean_data(p.b.next_sibling.next_sibling)
            p_dict.setdefault(label, []).append(value)
        except AttributeError:
            continue
    return p_dict  # Gives p value in dict form. :)


def div_components_marvelu(html):
    """Return extracted div stas from powerbox."""
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
    return div_dict

if __name__ == '__main__':
    for person in CHARACTER:
        doc = marvel_u_call(person.replace(" ", "_"))
        if doc:
            ps = p_components_marvelu(doc)
            ds = div_components_marvelu(doc)
            ps.update(ds)
            print(ps)
