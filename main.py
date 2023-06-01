import sys
from math import sqrt

from docProcess import Tfidf, io, text


def search(keyword: str):
    terms = keyword.split(' ')
    cosRes = []
    res = [0 for i in range(3)]
    for (title, url, time) in Tfidf.doc_list:
        res = [0 for i in range(3)]
        for term in terms:
            res[0] += Tfidf.tfidf[term][title] * Tfidf.tfidf[term]["query"]
            res[1] += Tfidf.tfidf[term]["query"] * Tfidf.tfidf[term]["query"]
            res[2] += Tfidf.tfidf[term][title] * Tfidf.tfidf[term][title]
        cosRes.append(((title, url, time), (res[0] / (sqrt(res[1]) * sqrt(res[2]))) if res[2] else 0))

    cosRes = sorted(cosRes, key=lambda x: x[1], reverse=True)
    i = 0
    for result in cosRes:
        if i == 5:
            break
        if result[0][0] == "query":
            continue
        i += 1
        print(str(result[0]) + ", " + str(result[1]))


if __name__ == '__main__':
    io.get_data()
    keyword = input("请输入搜索关键词：").lower()
    text.add_query(keyword)
    Tfidf.update_idf()
    Tfidf.update_tfidf()
    search(keyword)
