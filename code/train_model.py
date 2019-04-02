#coding=utf-8

import os
import pandas as pd 
import tensorflow as tf 

import linecache

# 读取原始文件
def read_origin_file():
	sentences = linecache.getlines('../data/train_data.txt')
	print len(sentences)

if __name__ == '__main__':
	read_origin_file()