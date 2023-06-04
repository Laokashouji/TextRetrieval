from math import sqrt
from docProcess import Tfidf, io, text


def search(keyword: str):
    cosRes = []
    res = [0 for i in range(3)]
    for i in range(Tfidf.doc_num - 1):
        res = [0 for j in range(3)]
        for term in keyword:
            res[0] += Tfidf.tfidf[term][i] * Tfidf.tfidf[term][Tfidf.doc_num - 1]
            res[1] += Tfidf.tfidf[term][Tfidf.doc_num - 1] * Tfidf.tfidf[term][Tfidf.doc_num - 1]
            res[2] += Tfidf.tfidf[term][i] * Tfidf.tfidf[term][i]
        cosRes.append((Tfidf.doc_list[i], (res[0] / (sqrt(res[1]) * sqrt(res[2]))) if res[2] else 0))

    io.log(cosRes)


if __name__ == '__main__':
    io.get_data()
    while True:
        Tfidf.keyword = input("请输入搜索关键词(输入##结束搜索)：")
        if Tfidf.keyword == "##":
            break
        keyword = text.add_query(Tfidf.keyword)
        Tfidf.update_idf()
        Tfidf.update_tfidf()
        search(keyword)

