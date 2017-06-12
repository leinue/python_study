#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
xxxx
"""

import jieba

jieba.load_userdict('dict.txt')

seg_list = jieba.cut('我来到北京清华大学', cut_all=True)
print 'full mode:' + '/'.join(seg_list)

seg_list = jieba.cut('我来到北京清华大学', cut_all=False)
print 'default mode:' + '/'.join(seg_list)

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print ", ".join(seg_list)

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print ", ".join(seg_list)

seg_list = jieba.cut("李小福是创新办主任也是云计算方面的专家")
print ", ".join(seg_list)

seg_list = jieba.cut("我们中出了一个叛徒")
print "// ".join(seg_list)

testlist = [
    ('今天天气不错', ('今天', '天气')),
    ('如果放到post中将出错。', ('中', '将')),
    ('我们中出了一个叛徒', ('中', '出')),
]

for sent, seg in testlist:
    print('// '.join(jieba.cut(sent, HMM=False)))
    word = ''.join(seg)
    print('%s Before: %s, After: %s' % (word, jieba.get_FREQ(word), jieba.suggest_freq(seg, True)))
    print('// '.join(jieba.cut(sent, HMM=False)))
    print("-"*40)
