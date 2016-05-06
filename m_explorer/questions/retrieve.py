from marvel.marvel import Marvel
from dateutil import parser
import os
from m_comics.models import Comic
from questions.models import Character


def get_comics_by_character(character_id):
    """Return requests from marvel API for comic information."""
    m = Marvel(os.environ.get("PUBLIC_KEY"), os.environ.get("PRIVATE_KEY"))
    offset = 0
    all_comics = []
    print('fetching comics data')
    comics = m.get_comics(characters=character_id, limit="100", offset=offset)
    print('api call completed')
    if comics.code != 200:
        print('backing off to 20 at a time')
        comics = m.get_comics(characters=character_id, limit="20")
        print('stopping fetching now')
        if comics.code == 200:
            all_comics.extend(comics.data.results)
        return all_comics
    all_comics.extend(comics.data.results)
    if comics.data.total >= 100:
        print('more to go')
        while comics.data.total > offset:
            print('processed {} of {}'.format(offset, comics.data.total))
            offset += 100
            comics = m.get_comics(characters=character_id, limit="100",
                                  offset=offset)
            if comics.code == 200:
                all_comics.extend(comics.data.results)
    return all_comics


def attach_character(comic):
    """Attach associated characters to a comic book entry."""
    c_list = comic.characters.items
    for char in c_list:
        char = char.resourceURI.split('/')[-1]
    queryset = Character.objects.filter(marvel_id__in=c_list)
    return queryset


def convert_date(date):
    """Create and apply the date from the database."""
    strdate = date.dict['date']
    dt = parser.parse(strdate)
    dtstring = str(dt.year) + '-' + str(dt.month) + '-' + str(dt.day)
    return dt, dtstring


def set_blanks():
    """Create an empty dictionary to catch holes."""
    c_dict = {}
    c_dict['title'] = ''
    c_dict['issue_number'] = ''
    c_dict['description'] = ''
    c_dict['thumbnail'] = ''
    c_dict['upc'] = ''
    c_dict['page_count'] = ''
    c_dict['format'] = ''
    c_dict['purchase_url'] = ''
    c_dict['detail_url'] = ''
    c_dict['purchase_url'] = ''
    c_dict['purchase_date'] = None
    c_dict['str_pur_date'] = ''
    c_dict['series'] = ''
    return c_dict


def prep_comics(all_comics):
    """Return preped comics for entry to db."""
    sorted_comics = []
    for comic in all_comics:
        c_dict = set_blanks()
        c_dict['marvel_id'] = comic.id
        c_dict['title'] = comic.title
        c_dict['issue_number'] = comic.issueNumber
        c_dict['description'] = comic.description
        c_dict['thumbnail'] = comic.thumbnail
        c_dict['upc'] = comic.upc
        c_dict['page_count'] = comic.pageCount
        c_dict['format'] = comic.format
        for url in comic.urls:
            if url['type'] == 'detail':
                c_dict['detail_url'] = url['url']
            elif url['type'] == 'purchase':
                c_dict['purchase_url'] = url['url']
        for date in comic.dates:
            if date.type == 'onsaleDate':
                dt, dtstring = convert_date(date)
                c_dict['purchase_date'] = dt
                c_dict['str_pur_date'] = dtstring
        if 'purchase_date' not in c_dict:
            c_dict['purchase_date'] = None
            c_dict['str_pur_date'] = ''
        c_dict['series'] = comic.series
        c_dict['characters'] = attach_character(comic)
        sorted_comics.append(c_dict)
    return sorted_comics


def fill_the_db(cleaned):
    """Create and save characters to the database."""
    for c in cleaned:
        comic = Comic(
            marvel_id=c['marvel_id'],
            description=c['description'],
            thumbnail=c['thumbnail'],
            title=c['title'],
            issue_number=c['issue_number'],
            page_count=c['page_count'],
            upc=c['upc'],
            _format=c['format'],
            detail_url=c['detail_url'],
            purchase_url=c['purchase_url'],
            purchase_date=c['purchase_date'],
            str_pur_date=c['str_pur_date'],
            series=c['series'],
        )
        # comic.characters.add(*c['characters'])
        import pdb; pdb.set_trace()
        comic.save()


def api_call(character_id):
    """Api to db entry main function."""
    # import pdb; pdb.set_trace()
    all_comics = get_comics_by_character(character_id)
    preped = prep_comics(all_comics)
    fill_the_db(preped)
