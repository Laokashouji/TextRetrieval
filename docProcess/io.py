import re
import shelve
import pandas as pd

from docProcess import text, Tfidf


def load(row):
    dic = {}
    tot = 0
    for term in re.split(r'''['"\s]''', row["content"]):
        if not term:
            continue
        term = term.strip("\"\',.><?!*").lower()
        tot = tot + 1
        num = dic.setdefault(term, 0)
        dic[term] = num + 1
    text.add_doc(row["title"], dic, tot, row["url"], row["date"])


def get_data():
    df = pd.read_csv("data/data.csv", header=0, usecols=["title", "url", "content", "date"])
    for index, row in df.iterrows():
        if not isinstance(row["content"], str):
            continue
        load(row)

