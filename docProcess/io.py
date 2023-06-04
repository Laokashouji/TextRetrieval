import sys

from nltk import sent_tokenize
import pandas as pd
from docProcess import text, Tfidf


def get_data():
    df = pd.read_csv("data/data.csv", header=0, usecols=["title", "url", "content", "date"])
    Tfidf.doc = df
    for index, row in df.iterrows():
        if not isinstance(row["content"], str):
            continue
        text.load(index, row)


def print_result(cosRes):
    cosRes = sorted(cosRes, key=lambda x: x[1], reverse=True)
    i = 0
    for result in cosRes:
        if i == 5:
            break
        j = 0
        res_line = ""
        for line in sent_tokenize(Tfidf.doc.loc[result[0][0], "content"]):
            if j == result[0][1]:
                res_line = line
                break
            j = j + 1
        print(str(i + 1) + ": ")
        print("\t标题: " + str(Tfidf.doc.loc[result[0][0], "title"]))
        print("\t主要匹配内容: " + res_line)
        print("\t余弦相关度: " + str(result[1]))
        print("\turl: " + str(Tfidf.doc.loc[result[0][0], "url"]))
        print("\t时间: " + str(Tfidf.doc.loc[result[0][0], "date"] + '\n'))
        i = i + 1


def log(cosRes):
    print_result(cosRes)
    ans = input("您是否满意本次搜索结果?(Y/N)")
    ft = sys.stdout
    if ans.lower() == 'y':
        with open("./log/good_ans.txt", "a", encoding="utf-8") as f:
            sys.stdout = f
            print("搜索词: " + Tfidf.keyword)
            print_result(cosRes)
            print("**************************************************")
            sys.stdout = ft
    else:
        with open("./log/bad_ans.txt", "a", encoding="utf-8") as f:
            sys.stdout = f
            print("搜索词: " + Tfidf.keyword)
            print_result(cosRes)
            print("**************************************************")
            sys.stdout = ft
