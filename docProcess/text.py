from docProcess.tfidf import Tfidf


# dic 单词:单词数
def add_doc(title: str, dic: dict, term_num: int, url: str = None, time=None):
    """
    :param time:
    :param url:
    :param title:
    :param dic:
    :param term_num:
    :return:
    """

    Tfidf.doc_num = Tfidf.doc_num + 1
    Tfidf.doc_list.append((title, url, time))
    Tfidf.update_tf(title, dic, term_num)

def add_query(keyword):
    terms = keyword.split(' ')
    dic = {}
    tot = 0
    for term in terms:
        tot = tot + 1
        num = dic.setdefault(term, 0)
        dic[term] = num + 1
    add_doc("query", dic, tot)