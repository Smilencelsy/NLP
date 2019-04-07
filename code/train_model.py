#encoding=utf-8

import os
import pandas as pd 
import tensorflow as tf 
import jieba

import linecache
import time

# 读取原始文件 分词
def word_segment(filename,n,new_filename):
	sentences = linecache.getlines(filename)
	if n >= len(sentences):
		sentences = sentences[1:]
	else:
		sentences = sentences[1:n]

	f = open(new_filename,'w')  #覆盖写
	for line in sentences:
		line = line.split('\t')
		tmp = jieba.cut(line[1])
		line[1] = "/".join(tmp)
		f.write((line[0] + '\t' + line[1] + '\t' + line[2]).encode('utf-8'))
	f.close()



if __name__ == '__main__':

	# 读取原始文件 分词
	# author@Smilence
	print 'word segmentation ...\n'
	time1 = time.clock()

	orgin_file_path = '../data/train_data.txt'
	new_file_path = '../data/all_model_segm.txt'
	orgin_file_lines = 800000 #选择要读取的文件行数 最大为80000
	word_segment(orgin_file_path,orgin_file_lines,new_file_path)

	time2 = time.clock()
	print 'word segmentation complete !\n' + str(time2-time1)

	#
