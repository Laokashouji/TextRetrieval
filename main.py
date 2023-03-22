from docProcess import Tfidf, io


def search(keyword: str):
    terms = keyword.split(' ')
    for term in terms:
        doc_list = []
        doc_list.append(Tfidf.tfidf[term])
        result = sorted(Tfidf.tfidf[term].items(), key=lambda x: x[1], reverse=True)
        for i in range(0, 5):
            if i >= len(result) or result[i] == 0:
                break
            print(result[i])


if __name__ == '__main__':

    io.load("1.txt")
    io.load("2.txt")

    keyword = input("请输入搜索关键词：")
    search(keyword)
