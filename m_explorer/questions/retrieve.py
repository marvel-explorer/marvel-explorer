from marvel.marvel import Marvel
import os
from m_comics.models import Comic
from .model import Character


def get_comics_by_character(character_id):
    """Return requests from marvel API for comic information."""
    m = Marvel(os.enviorn.get("PUBLIC_KEY"), os.environ.get("PRIVATE_KEY"))
    offset = 0
    comics = m.get_comics(characters=character_id, limit="100", format="comic",
                          offset=offset)
    if comics.code != 200:
        comics = m.get_comics(characters=character_id, limit="20",
                              format="comic")
        return [comics]
    all_comics = [comics]
    if comics.data.total <= 100:
        while comics.data.total > offset:
            offset += 100
            comics = m.get_comics(characters=character_id, limit="100",
                                  format="comic", offset=offset)
            all_comics.append(comics)
    return all_comics


def attach_character(c_dict):
    """Attach associated characters to a comic book entry."""
    c_list = c_dict.characters.items
    for char in c_list:
        char = char.resourceURI.split('/')[-1]
    queryset = Character.objects.filter(marvel_id__in=c_list)
    return queryset


def prep_comics(all_comics):
    """Return preped comics for entry to db."""
    sorted_comics = []
    for batch in all_comics:
        for comic in batch.data.results:
            c_dict = {}
            c_dict['marvel_id'] = comic.id
            c_dict['title'] = comic.title
            c_dict['issue_number'] = comic.issueNumber
            c_dict['description'] = comic.description
            c_dict['upc'] = comic.upc
            c_dict['page_count'] = comic.pageCount
            for url in comic.urls:
                if url['type'] == 'detail':
                    c_dict['detail_url'] = url.url
                elif url['type'] == 'purchase':
                    c_dict['purchase_url'] = url.url
            for date in comic.dates:
                if date['type'] == 'onsaleDate':
                    c_dict['purchase_date'] = date.date
            c_dict['series'] = comic.series
            c_dict['characters'] = attach_character(c_dict)
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
            detail_url=c['detail_url'],
            purchase_url=c['purchase_url'],
            purchase_date=c['purchase_date'],
            series=c['series'],
        )
        comic.characters.add(*c['characters'])
        comic.save()


def api_call(character_id):
    """Api to db entry main function."""
    all_comics = get_comics_by_character("character_id")
    preped = prep_comics(all_comics)
    fill_the_db(preped)
