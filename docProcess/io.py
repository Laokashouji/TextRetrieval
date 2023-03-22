import re
import shelve

from docProcess import text, Tfidf


def load(filename: str):
    file = open('./doc/' + filename, 'r')
    try:
        lines = file.readlines()
        dic = {}
        tot = 0
        for line in lines:
            for term in re.split(r'''[,.'" ]+''', line):
                if not term:
                    continue
                tot = tot + 1
                num = dic.setdefault(term, 0)
                dic[term] = num + 1
        text.add_doc(filename, dic, tot)

    finally:
        file.close()


def save():
    with shelve.open('./data/data.dat', flag='c') as file_to_write:
        file_to_write['tf'] = Tfidf.tf
        file_to_write['idf'] = Tfidf.idf
        file_to_write


def read(data_dict: dict):
    with shelve.open('./data/data.dat', flag='c') as file_to_write:
        for k, v in data_dict.items():
            file_to_write[k] = v


def get_data():
    load("1.txt")
    load("2.txt")
    Tfidf.update_idf()
    Tfidf.update_tfidf()
    save()
