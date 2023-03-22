from docProcess.tfidf import Tfidf


# dic 单词:单词数
def add_doc(filename: str, dic: dict, term_num: int):
    """
    :param filename:
    :param dic:
    :param term_num:
    :return:
    """

    Tfidf.doc_num = Tfidf.doc_num + 1

    # 建立tf的倒排索引，以及更新包含单词的文档数用于计算idf
    for term, num in dic.items():
        Tfidf.tf.setdefault(term, {})
        Tfidf.tf[term][filename] = num / term_num
        doc_term_num = Tfidf.doc_term_num.setdefault(term, 0)
        Tfidf.doc_term_num[term] = doc_term_num + 1
        Tfidf.idf.setdefault(term, 0)

    Tfidf.update_idf()
    Tfidf.update_tfidf()

    # Tfidf.tf[filename] = {}
    # Tfidf.doc_num = Tfidf.doc_num + 1
    # Tfidf.doc_list.append(filename)
    # Tfidf.tfidf[filename] = {}
    #
    # for term, num in dic.items():
    #     Tfidf.tf[filename][term] = num / term_num
    #     doc_term_num = Tfidf.doc_term_num.setdefault(term, 0)
    #     Tfidf.doc_term_num[term] = doc_term_num + 1
    #     Tfidf.idf.setdefault(term, 0)
    #
    # for term in Tfidf.idf.keys():
    #     Tfidf.idf[term] = log((Tfidf.doc_num + 1) / (Tfidf.doc_term_num[term] + 1)) + 1
    #
    # for filename in Tfidf.doc_list:
    #     for term in Tfidf.tf[filename].keys():
    #         Tfidf.tfidf[filename][term] = Tfidf.tf[filename][term] * Tfidf.idf[term]

    return None
