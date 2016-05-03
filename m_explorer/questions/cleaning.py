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
        to_clean['Place of Birth'] = to_clean['Place of Birth'][0].replace('u2019', "'")
    else:
        to_clean['Place of Birth'] = ''
    return to_clean


def occ_clean(to_clean):
    """Clean occupation."""
    if 'Occupation' in to_clean:
        to_clean['Occupation'] = to_clean['Occupation'][0].replace('u2019', "'")
    else:
        to_clean['Occupation'] = ''
    return to_clean


def power_clean(to_clean):
    """Clean powers."""
    if 'Powers' in to_clean:
        to_clean['Powers'] = to_clean['Powers'][0].replace('u2019', "'")
    else:
        to_clean['Powers'] = ''
    return to_clean


def identity_clean(to_clean):
    """Clean powers."""
    if 'Identity' in to_clean:
        to_clean['Identity'] = to_clean['Identity'][0].replace('u2019', "'")
    else:
        to_clean['Identity'] = ''
    return to_clean


def real_name_clean(to_clean):
    """Clean powers."""
    if 'Real Name' in to_clean:
        to_clean['Real Name'] = to_clean['Real Name'][0].replace('u2019', "'")
    else:
        to_clean['Real Name'] = ''
    return to_clean


def group_aff_clean(to_clean):
    """Clean powers."""
    if 'Group Affiliation' in to_clean:
        to_clean['Group Affiliation'] = to_clean['Group Affiliation'][0].replace('u2019', "'")
    else:
        to_clean['Group Affiliation'] = ''
    return to_clean


def paraph_clean(to_clean):
    """Clean powers."""
    if 'Paraphernalia' in to_clean:
        to_clean['Paraphernalia'] = to_clean['Paraphernalia'][0].replace('u2019', "'")
    else:
        to_clean['Paraphernalia'] = ''
    return to_clean


def education_clean(to_clean):
    """Clean powers."""
    if 'Education' in to_clean:
        to_clean['Education'] = to_clean['Education'][0].replace('u2019', "'")
    else:
        to_clean['Education'] = ''
    return to_clean


def ability_clean(to_clean):
    """Clean powers."""
    if 'Abilities' in to_clean:
        to_clean['Abilities'] = to_clean['Abilities'][0].replace('u2019', "'")
    else:
        to_clean['Abilities'] = ''
    return to_clean


def weapons_clean(to_clean):
    """Clean powers."""
    if 'Weapons' in to_clean:
        to_clean['Weapons'] = to_clean['Weapons'][0].replace('u2019', "'")
    else:
        to_clean['Weapons'] = ''
    return to_clean


def origin_clean(to_clean):
    """Clean powers."""
    if 'Origin' in to_clean:
        to_clean['Origin'] = to_clean['Origin'][0].replace('u2019', "'")
    else:
        to_clean['Origin'] = ''
    return to_clean


def alias_clean(to_clean):
    """Clean aliases."""
    if 'Aliases' in to_clean:
        to_clean['Aliases'] = to_clean['Aliases'][0].replace('u2019', "'")
    else:
        to_clean['Aliases'] = ''
    return to_clean


def weight_clean(to_clean):
    """Clean aliases."""
    if 'Weight' in to_clean:
        if 0 < len(to_clean['Weight'][0]) < 9:
            new_weight = to_clean['Weight'][0][:3]
            to_clean['Weight'] = new_weight
        elif not len(to_clean['Weight'][0]):
            to_clean['Weight'] = ''
        else:
            to_clean['Weight'] = 'Fluctuates with form.'
    else:
        to_clean['Weight'] = ''
    return to_clean


def height_clean(to_clean):
    """Clean height."""
    if 'Height' in to_clean:
        if 'u2019' in to_clean['Height'][0]:
            to_clean['Height'][0].replace('u2019', "'")
        to_clean['Height'] = to_clean['Height'][0]
    else:
        to_clean['Height'] = ''
    return to_clean


def first_app_clean(to_clean):
    """Clean first appeance and get origin age."""
    if 'First Appearance' in to_clean:
        to_clean['First Appearance'] = to_clean['First Appearance'][0]
        date = to_clean['First Appearance'].split(" ")[-1]
        to_clean['golden'] = None
        to_clean['silver'] = None
        to_clean['bronze'] = None
        to_clean['dark'] = None
        to_clean['modern'] = None
        try:
            year = int(date[1:5])
            if 1920 < year <= 1955:
                to_clean['golden'] = True
            elif 1955 < year <= 1970:
                to_clean['silver'] = True
            elif 1971 < year <= 1985:
                to_clean['bronze'] = True
            elif 1985 < year <= 1995:
                to_clean['dark'] = True
            elif 1995 < year:
                to_clean['modern'] = True
        except ValueError:
            pass
    else:
        to_clean['First Appearance'] = ''
    return to_clean


def hair_clean(to_clean):
    """Clean height."""
    if 'Hair' in to_clean:
        if '(' in to_clean['Hair'][0]:
            to_clean['Hair'] = 'Varies'
        to_clean['Hair'] = to_clean['Hair'][0]
    else:
        to_clean['Hair'] = ''
    return to_clean


def eyes_clean(to_clean):
    """Clean eyes."""
    if 'Eyes' in to_clean:
        if '(' in to_clean['Eyes'][0]:
            to_clean['Eyes'] = 'Varies'
        to_clean['Eyes'] = to_clean['Eyes'][0]
    else:
        to_clean['Eyes'] = ''
    return to_clean


def citizenship(to_clean):
    """Clean eyes."""
    if 'Citizenship' in to_clean:
        c = to_clean['Citizenship'][0].split(" ")
        if c[0] == "U.S.A." or c[0] == "U.S.":
            c = "U.S.A."
        elif c[0] == "United" and c[1] == "States":
            c = "U.S.A."
        else:
            c = to_clean['Citizenship'][0]
        to_clean['Citizenship'] = c
    else:
        to_clean['Citizenship'] = 'unknown'
    return to_clean


def name_clean(to_clean):
    """Clean name."""
    name = to_clean['marvel_name']
    if "(" in name:
        name = name.split('(')
        to_clean['name'] = name[0]
    else:
        to_clean['name'] = name
    return to_clean


def gender(to_clean):
    """Extract genders from filters."""
    if to_clean['Powers'] != '':
        if ' her ' in to_clean['Powers'] or ' she ' in to_clean['Powers']:
            to_clean['gender'] = 'Female'
            return to_clean
        elif ' his ' in to_clean['Powers'] or ' he ' in to_clean['Powers']:
            to_clean['gender'] = 'Male'
            return to_clean
    if to_clean['Abilities'] != '':
        if ' her ' in to_clean['Abilities'] or ' she ' in to_clean['Abilities']:
            to_clean['gender'] = 'Female'
            return to_clean
        elif ' his ' in to_clean['Abilities'] or ' he ' in to_clean['Abilities']:
            to_clean['gender'] = 'Male'
            return to_clean
    if to_clean['Weapons'] != '':
        if ' her ' in to_clean['Weapons'] or ' she ' in to_clean['Weapons']:
            to_clean['gender'] = 'Female'
            return to_clean
        elif ' his ' in to_clean['Weapons'] or ' he ' in to_clean['Weapons']:
            to_clean['gender'] = 'Male'
            return to_clean
    if to_clean['Paraphernalia'] != '':
        if ' her ' in to_clean['Paraphernalia'] or ' she ' in to_clean['Paraphernalia']:
            to_clean['gender'] = 'Female'
            return to_clean
        elif ' his ' in to_clean['Paraphernalia'] or ' he ' in to_clean['Paraphernalia']:
            to_clean['gender'] = 'Male'
            return to_clean
    to_clean['gender'] = 'Unknown'
    return to_clean



def cleaning_dicts(to_clean):
    """Clean dicts to inject into database."""
    cleaned = []
    for d in to_clean:
        d['marvel_name'] = d['marvel_name'][0].replace('u2019', "'")
        d['marvel_id'] = d['marvel_id'][0].replace('u2019', "'")
        d['description'] = d['description'][0].replace('u2019', "'")
        d['thumbnail'] = d['thumbnail'][0].replace('u2019', "'")
        d = pob_clean(d)
        d = occ_clean(d)
        d = power_clean(d)
        d = ability_clean(d)
        d = identity_clean(d)
        d = real_name_clean(d)
        d = group_aff_clean(d)
        d = paraph_clean(d)
        d = education_clean(d)
        d = weapons_clean(d)
        d = origin_clean(d)
        d = alias_clean(d)
        d = weight_clean(d)
        d = height_clean(d)
        d = first_app_clean(d)
        d = hair_clean(d)
        d = eyes_clean(d)
        d = citizenship(d)
        d = name_clean(d)
        d = gender(d)
        cleaned.append(d)
    clean_log = open("cleaned.py", "w")
    clean_log.write(str(cleaned).encode('ascii', 'ignore'))
    clean_log.close()
    return cleaned






if __name__ == '__main__':
    full_dict_list = combine_results()
