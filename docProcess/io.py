import re

import text


def load(filename: str):
    file_object2 = open(filename, 'r')
    try:
        lines = file_object2.readlines()
        dic = {}
        for line in lines:
            for word in re.split(r'''[,.'" ]+''', line):
                if not word:
                    continue
                num = dic.setdefault(word, 0)
                dic[word] = num+1
        text.calcTfidf(dic)
    finally:
        file_object2.close()
