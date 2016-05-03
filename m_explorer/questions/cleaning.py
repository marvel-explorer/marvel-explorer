# -*-encoding:utf-8 -*-
"""Clean the scrapper and API results."""
from s_results import s_results
from api_results import api_results


def combine_results():
    """Combine two results lists"""
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


if __name__ == '__main__':
    full_dict_list = combine_results()
