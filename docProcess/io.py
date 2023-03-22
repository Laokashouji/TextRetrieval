import re
import shelve

from docProcess import text


def load(filename: str):
    file_object2 = open('./doc/' + filename, 'r')
    try:
        lines = file_object2.readlines()
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
        file_object2.close()


def save(data_dict: dict):
    with shelve.open('file_name', flag='c') as file_to_write:
        for k, v in data_dict.items():
            file_to_write[k] = v
