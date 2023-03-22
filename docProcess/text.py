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
    Tfidf.doc_list.append(filename)
    Tfidf.update_tf()


    return None
