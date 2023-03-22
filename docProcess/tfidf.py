from math import log


class Tfidf:

    doc_list = []
    doc_num = 0
    doc_term_num = {}
    tf = {}
    idf = {}
    tfidf = {}

    @classmethod
    def update_idf(cls):
        for term in cls.idf.keys():
            cls.idf[term] = log((cls.doc_num + 1) / (cls.doc_term_num[term] + 1)) + 1

    @classmethod
    def update_tfidf(cls):
        for term in cls.tf.keys():
            cls.tfidf.setdefault(term, {})
            for filename in cls.doc_list:
                cls.tfidf[term][filename] = cls.tf[term].setdefault(filename, 0) * cls.idf[term]

    @classmethod
    def update_tf(cls, filename: str, dic: dict, term_num: int):
        """
        建立tf的倒排索引，以及更新包含单词的文档数用于计算idf
        :param filename:
        :param dic:
        :param term_num:
        :return:
        """
        for term, num in dic.items():
            cls.tf.setdefault(term, {})
            cls.tf[term][filename] = num / term_num
            doc_term_num = cls.doc_term_num.setdefault(term, 0)
            cls.doc_term_num[term] = doc_term_num + 1
            cls.idf.setdefault(term, 0)

