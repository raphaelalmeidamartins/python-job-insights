import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",", quotechar='"')
        docs_list = list(reader)

    return docs_list
