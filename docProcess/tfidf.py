from cmath import log


class Tfidf:

    doc_list = []
    doc_num = 0
    doc_term_num = {}
    tf = {}
    idf = {}
    tfidf = {}

    @classmethod
    def update_idf(cls):
        for term in Tfidf.idf.keys():
            Tfidf.idf[term] = log((Tfidf.doc_num + 1) / (Tfidf.doc_term_num[term] + 1)) + 1

    @classmethod
    def update_tfidf(cls):
        for term in Tfidf.tf.keys():
            Tfidf.tfidf.setdefault(term, {})
            for filename in Tfidf.doc_list:
                Tfidf.tfidf[term][filename] = Tfidf.tf[term].setdefault(filename, 0) * Tfidf.idf[term]

