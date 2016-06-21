#coding=utf-8
import sys
sys.path.append('..')
import os
import jieba
from utils import myutils

#greeting_path = "../data/greeting"
#greeting_list = myutils.read_line_to_list(greeting_path)
#comment = "{greeting}"

def get_url():
    """

    Returns:
    urls file path
    """

    pass


def scrapy_title(url_path):
    """
    url_path:
    url file path

    Returns:
    title_file_path
    """
    pass



def seg_zh_line(zh_line, method='jieba'):
    """
    zh_line:
    Chinese string line

    method:
    seg method , default using jieba

    Returns:
    segged Chinese word list
    """

    zh_stop_words = 'stop-words/zh_cn.txt'
    stop_words = [ line.strip().decode('utf-8') for line in open(zh_stop_words).readlines() ]
    jieba.enable_parallel(8)

    zh_line = zh_line.decode('utf8')
    zh_line = zh_line.strip()

    seg_list = jieba.cut(zh_line, cut_all=False)
    res = " ".join(set(seg_list) - set(stop_words))

    return res


def train_word_embedding_model(doc_list, method='word2vec'):
    """
    doc_list:
    each doc is a word list

    method:
    method to calc word embedding

    Returns:
    word embedding model

    """
    pass


def mapping_word_class(word, class_dict):
    """
    word:
    chinese word

    class_dict:
    word class dict

    Returns:
    word class

    """
    pass


if __name__ == '__main__':

    url_path = get_url()
    title_list = scrapy_title(url_path)

    seg_list = []
    for title in title_list:
        seg_list.append(seg_zh_line(title))


    embedding_model = train_word_embedding_model(seg_list)


