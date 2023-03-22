import sys

from docProcess import Tfidf, io


def search(keyword: str):
    terms = keyword.split(' ')
    for term in terms:
        result = sorted(Tfidf.tfidf[term].items(), key=lambda x: x[1], reverse=True)
        for i in range(0, 5):
            if i >= len(result) or abs(result[i][1]) < sys.float_info.epsilon:
                break
            print(result[i])


if __name__ == '__main__':

    io.get_data()

    keyword = input("请输入搜索关键词：")
    search(keyword)
