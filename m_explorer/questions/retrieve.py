from marvel.marvel import Marvel
import os
from m_comics.models import Comic


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


def prep_comics(all_comics):
    """Return preped comics for entry to db."""
    sorted_comics =
    for batch in all_comics:
        for comic in batch.data.results:






    characters = models.ManyToManyField('questions.Character',
                                        related_name='comics')
    marvel_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    issue_number = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=1000, default='')
    isbn = models.CharField(max_length=50, null=True)
    page_count = models.IntegerField(null=True)
    url = models.URLField(max_length=255, null=True)
    series = models.IntegerField(null=True)
    purchase = models.URLField(max_length=255, null=True)
    read = models.BooleanField(default=False)
    purchase_date = models.CharField(max_length=50)











if __name__ == '__main__':
    get_comics_by_character("1009546")