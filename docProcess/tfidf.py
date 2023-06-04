from math import log


class Tfidf:

    doc = None
    doc_list = []
    doc_num = 0
    doc_term_num = {}
    tf = {}
    idf = {}
    tfidf = {}
    keyword = ""

    @classmethod
    def update_idf(cls):
        for term in cls.idf.keys():
            cls.idf[term] = log((cls.doc_num + 1) / (cls.doc_term_num[term] + 1)) + 1

    @classmethod
    def update_tfidf(cls):
        for term in cls.tf.keys():
            cls.tfidf.setdefault(term, {})
            for i in range(cls.doc_num):
                cls.tfidf[term][i] = cls.tf[term].setdefault(i, 0) * cls.idf[term]

    @classmethod
    def update_tf(cls, dic, term_num):
        for term, num in dic.items():
            cls.tf.setdefault(term, {})
            cls.tf[term][cls.doc_num] = num / term_num
            doc_term_num = cls.doc_term_num.setdefault(term, 0)
            cls.doc_term_num[term] = doc_term_num + 1
            cls.idf.setdefault(term, 0)

