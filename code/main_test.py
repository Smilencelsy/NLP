#coding=utf-8

import os
from optparse import OptionParser

###################################
# arg_parser： 读取参数列表
###################################
def arg_parser():
    oparser = OptionParser()

    oparser.add_option("-m", "--model_file", dest="model_file", help="输入模型文件 \
            must be: negative.model", default = None)

    oparser.add_option("-d", "--data_file", dest="data_file", help="输入验证集文件 \
            must be: validation_data.txt", default = None)

    oparser.add_option("-o", "--out_put", dest="out_put_file", help="输出结果文件 \
			must be: result.txt", default = None)

    (options, args) = oparser.parse_args()
    global g_MODEL_FILE
    g_MODEL_FILE = str(options.model_file)

    global g_DATA_FILE
    g_DATA_FILE = str(options.data_file)

    global g_OUT_PUT_FILE
    g_OUT_PUT_FILE = str(options.out_put_file)

###################################
# load_model： 加载模型文件
###################################
def load_model(model_file_name):
	return None;

###################################
# predict： 根据模型预测结果并输出结果文件，文件内容格式为qid\t言语\t标签
###################################
def predict(model):
	print("predict start.......")
	###################################
	# 预测逻辑和结果输出，("%d\t%s\t%d", qid, content, predict_label)
	###################################
	print("predict end.......")

	return None;

###################################
# main： 主逻辑
###################################
def main():
	print("main start.....")
	
	if g_MODEL_FILE is not None:
		model = load_model(g_MODEL_FILE)
		predict(model)

	print("main end.....")

	return 0;

if __name__ == '__main__':
	arg_parser()
	main()
