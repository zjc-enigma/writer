#coding=utf-8
import sys
sys.path.append('..')
import os
from utils import myutils

#greeting_path = "../data/greeting"
#greeting_list = myutils.read_line_to_list(greeting_path)
#comment = "{greeting}"

def get_url():
    """
    zh_doc:
    string in Chinese

    Returns:
    segged Chinese word list
    """

    pass


def seg_zh_doc(zh_doc):
    """
    zh_doc:
    string in Chinese

    Returns:
    segged Chinese word list
    """

    pass



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
    pass
