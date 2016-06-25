# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import os
import jieba
import pandas as pd
from utils import myutils
import gensim
import numpy as np
from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import multiprocessing
import random


#myutils.set_ipython_encoding_utf8()

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
    try:
        zh_stop_words = open('../data/stop-words/zh_cn.txt').read().splitlines()

        stop_words = [ line.strip().decode('utf-8') for line in zh_stop_words ]

        #jieba.enable_parallel(8)
        zh_line = zh_line.decode('utf8')
        zh_line = zh_line.strip()

        seg_list = jieba.cut(zh_line, cut_all=False)
        res = " ".join(set(seg_list) - set(stop_words))

        return res
    except AttributeError, attr:
        print zh_line
        return ""

def train_word2vec_model(doc_list):
    """
    doc_list:
    each doc is a word list

    method:
    method to calc word embedding

    Returns:
    word embedding model

    """
    inp = '../data/wordlist'
    model_path = "../data/word2vec_model"
    vector_path = "../data/word2vec_vector"

    model = Word2Vec(LineSentence(inp), size=400, window=5, min_count=5,
                     workers=multiprocessing.cpu_count())

    model.save(model_path, ignore=[])
    model.save_word2vec_format(vector_path, binary=True)
    return model


def load_word2vec_model(model):
    """

    """
    embed_data_path = "../data/embed_dat"
    embed_vocab_path = "../data/embed_vocab"
    vector_model_path = "../data/user_vector"

    if os.path.exists(embed_data_path):
        os.remove(embed_data_path)

    if os.path.exists(embed_vocab_path):
        os.remove(embed_vocab_path)

    if not os.path.exists(embed_data_path):
        print("Caching word embeddings in memmapped format...")

        wv = Word2Vec.load_word2vec_format(vector_model_path,  binary=True)

        print "wv syn0norm shape : " + str(wv.syn0norm.shape)
        fp = np.memmap(embed_data_path, dtype= np.double, mode='w+', shape=wv.syn0norm.shape)
        fp[:] = wv.syn0norm[:]
        with open(embed_vocab_path, "w") as f:
            for _, w in sorted((voc.index, word) for word, voc in wv.vocab.items()):
                f.write(w + "\n")

        del fp, wv


def get_sim_words(word, model):

    try:
        ret = model.most_similar(word.decode('utf8'))

    except Exception, e:

        print e
        return ret

    res = []
    for item in ret:
        res.append(item[0].encode('utf8'))

    return res

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



def write_comment():

    greeting_list = open("../data/en/greeting").read().splitlines()
    person_list = open("../data/en/person").read().splitlines()
    adjective_list = open("../data/en/adjective").read().splitlines()
    product_list = open("../data/en/product").read().splitlines()
    ending_list = open("../data/en/ending").read().splitlines()
    #person = open("../data/person").read().splitlines()
    en_comment_format = "{greeting} {person} ! Look at this {adjective} {product}, {ending}"

    for i in xrange(10):
        print en_comment_format.format(greeting=random.choice(greeting_list),
                                       person=random.choice(person_list),
                                       adjective=random.choice(adjective_list),
                                       product=random.choice(product_list),
                                       ending=random.choice(ending_list))





def get_words_by_nominal(nominal, nominal_dict, words):

    words.columns = ["word", "nominal", "freq"]
    res = words.loc[words.nominal == nominal]
    return res



def load_nominal_dict(nominal_path):

    nominal_dict = {}
    fd = open(nominal_path, 'r')
    for line in fd:
        line = line.strip()
        arr = line.split()
        if len(arr) < 2: continue
        nominal = arr[0]
        mean = " ".join(arr[1:])
        nominal_dict[nominal] = mean

    return nominal_dict


if __name__ == '__main__':

    seed_word = ""

    #url_path = get_url()
    #title_list = scrapy_title(url_path)

    # seg_list = []
    # for title in title_list:
    #     seg_list.append(seg_zh_line(title))

    crawled_title_json_list = myutils.parse_json_file("../data/out.json")
    # filte all item where title is None 
    title_json_list = [ title_json for title_json in crawled_title_json_list if title_json['title'] is not None ]

    for index, crawled_title in enumerate(title_json_list):
        crawled_title.update({'seg': seg_zh_line(crawled_title['title'])})

    #embed_model = train_word2vec_model(seg_list)
    vector_file = "../data/all_vector"
    model = gensim.models.Word2Vec.load_word2vec_format(vector_file, binary=False)

    sim_words = get_sim_words(seed_word, model)

    nominal_freq_words = "../data/360W词性词频词库.txt"
    words = pd.read_csv(nominal_freq_words,
                        header=None,
                        sep="\t")

    nominal_path = "../data/nominal_dict"
    get_words_by_nominal()
