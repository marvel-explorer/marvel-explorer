# -*-encoding:utf-8 -*-
"""Clean the scrapper and API results."""
from s_results import s_results
from api_results import api_results


def combine_results():
    """Combine two results lists."""
    results = []
    for index, value in enumerate(api_results):
        result = value
        result.update(s_results[index])
        results.append(result)
        print(result)
    combined = open("combined.py", "w")
    combined.write(str(results).encode('ascii', 'ignore'))
    combined.close()
    return results


def pob_clean(to_clean):
    """Clean pob."""
    if 'Place of Birth' in to_clean:
        to_clean['Place of Birth'] = to_clean['Place of Birth'][0]
    else:
        to_clean['Place of Birth'] = ''
    return to_clean


def occ_clean(to_clean):
    """Clean pob."""
    if 'Occupation' in to_clean:
        to_clean['Place of Birth'] = to_clean['Place of Birth'][0]
    else:
        to_clean['Place of Birth'] = ''
    return to_clean




def cleaning_dicts(to_clean):
    """Clean dicts to inject into database."""
    cleaned = []
    for d in to_clean:
        d['marvel_name'] = d['marvel_name'][0]
        d['marvel_id'] = d['marvel_id'][0]
        d['description'] = d['description'][0]
        d['thumbnail'] = d['thumbnail'][0]
        d = pob_clean(d)
        d = occ_clean(d)





if __name__ == '__main__':
    full_dict_list = combine_results()
