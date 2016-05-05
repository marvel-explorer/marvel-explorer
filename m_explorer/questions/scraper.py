"""Scrapper to produce character information."""
from bs4 import BeautifulSoup
from marvel.marvel import Marvel
from api_results import api_results
import requests
import io
import os
import os.path
import string

MARVEL_UNIVERSE_DOMAIN = 'http://marvel.com/universe/'


def character_list(text_file):
    """Translate a text_file into a list of characters to search."""
    with open(text_file) as file:
        char_list = file.read().splitlines()
    return char_list

CHARACTER = character_list('api_characters.txt')


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


def api_character_calls():
    """Call character lists from marvel."""
    m = Marvel(os.environ.get('PUBLIC_KEY'), os.environ.get('PRIVATE_KEY'))
    log = open("api.log", "a")
    api = open("api_characters.txt", "a")
    calls = string.letters[26:]
    dict_list = []
    for letter in calls:
        try:
            call = m.get_characters(nameStartsWith=letter, limit="100")
            log.write("{}:\n".format(letter))
            log.write("Code Status:{}:\n".format(call.code))
            log.write("Total:{}:\n".format(call.data.total))
            for char in call.data.results:
                individual = {}
                if char.comics.available != 0:
                    api.write("{}\n".format(char.name.encode('ascii', 'ignore')))
                    individual.setdefault('marvel_name', []).append(char.name)
                    individual.setdefault('marvel_id', []).append(char.id)
                    individual.setdefault('total_comics', []).append(char.comics.available)
                    individual.setdefault('description', []).append(char.description)
                    individual.setdefault('thumbnail', []).append(char.thumbnail)
                    dict_list.append(individual)
        except KeyError:
            log.write("failed:{} - SERVER ERROR\n".format(letter))
            offset = 0
            trip = False
            while not trip:
                call = m.get_characters(nameStartsWith=letter, limit="5", offset=offset)
                try:
                    for char in call.data.results:
                        individual = {}
                        if char.comics.available != 0:
                            api.write("{}\n".format(char.name.encode('ascii', 'ignore')))
                            individual.setdefault('marvel_name', []).append(char.name)
                            individual.setdefault('marvel_id', []).append(char.id)
                            individual.setdefault('total_comics', []).append(char.comics.available)
                            individual.setdefault('description', []).append(char.description)
                            individual.setdefault('thumbnail', []).append(char.thumbnail)
                            dict_list.append(individual)
                    if offset > call.data.total:
                        trip = True
                except KeyError:
                    pass
                offset += 5
    results = open("api_results.txt", "w")
    results.write("{}\n".format(str(dict_list).encode('ascii', 'ignore')))
    results.close()
    return dict_list


def marvel_u_dict_production():
    """Create attribute dicts from maruvel U."""
    dict_list = []
    for person in CHARACTER:
        doc = marvel_u_call(person.replace(" ", "_"))
        if not doc:
            name_reverse = person.split(" ")
            if len(name_reverse) == 2:
                doc = marvel_u_call(name_reverse[1] + ',_' + name_reverse[0])
        if doc:
            ps = p_components_marvelu(doc)
            ds = div_components_marvelu(doc)
            ps.update(ds)
            dict_list.append(ps)
            print(ps)
        else:
            ps = {}
            dict_list.append(ps)
            print(ps)
    results = open("s_results.txt", "w")
    results.write(str(dict_list).encode('ascii', 'ignore'))
    results.close()
    return dict_list


def combine_dicts():
    """Combine API dicts with marvelU dicts."""
    api_dict_list = api_results
    sc_dict_list = marvel_u_dict_production()
    results = []
    for index, value in enumerate(api_dict_list):
        combo = api_dict_list[index].update(sc_dict_list[index])
        results.append(combo)
    combined = open("combined.py", "w")
    combined.write(str(results).encode('ascii', 'ignore'))
    combined.close()
    return results


if __name__ == '__main__':
    full_dict_list = combine_dicts()
