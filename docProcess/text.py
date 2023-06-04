from docProcess.tfidf import Tfidf
from nltk.tokenize import sent_tokenize, word_tokenize


# dic 单词:单词数
def add_doc(index, dic, term_num, line):
    Tfidf.doc_list.append((index, line))
    Tfidf.update_tf(dic, term_num)
    Tfidf.doc_num = Tfidf.doc_num + 1


def load(index, row):
    line = 0
    for sentence in sent_tokenize(row["content"]):
        tot = 0
        dic = {}
        for word in word_tokenize(sentence):
            word = word.lower()
            tot = tot + 1
            num = dic.setdefault(word, 0)
            dic[word] = num + 1
        add_doc(index, dic, tot, line)
        line = line + 1
    """
    # 自己实现的分词
    for term in re.split(r'''['"\s]''', row["content"]):
        if not term:
            continue
        term = term.strip("\"\',.><?!*").lower()
        tot = tot + 1
        num = dic.setdefault(term, 0)
        dic[term] = num + 1
    """


def add_query(keyword):
    terms = []
    dic = {}
    tot = 0
    for word in word_tokenize(keyword):
        word = word.lower()
        terms.append(word)
        tot = tot + 1
        num = dic.setdefault(word, 0)
        dic[word] = num + 1
    add_doc(0, dic, tot, 0)
    return terms
