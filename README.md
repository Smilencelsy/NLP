# NLP
---
### 0x00.要求

+ 实现一个汉语自动分词系统(Chinese word segmentation)
本题目要求实现一个汉语自动分词系统，并在微博等非规范文本测试集上进行测试分析。如果在本题目中不考虑命名实体识别问题，歧义消解和集外词处理是汉语自动分词中的关键问题

+ 14. 设计实现一种基于文本内容/情感的文本自动分类方法(Text classification)
依据某种文本分类标准实现文本自动分类，并进行实验分析。针对汉语文本或英语文本均可

在当前流行的游戏中, 无论是MOBA、休闲还是FPS类游戏, 但凡是具有线上交流功能的游戏, 都会存在影响玩家体验的消极语言。其包括但不限于挂机、送人头、投降、辱骂等, 可以说, 消极语言很大程度上影响了游戏环境和风气。准确的识别发出消极语言的玩家, 并且对其进行惩罚, 具有净化游戏环境, 改善玩家体验等重大现实意义。

### 0x01.数据说明
此数据来源于腾讯某次游戏安全竞赛的自然语言处理方向赛题
train_data.txt 为训练集
validation_data_demo.txt 为输出集的格式

数据格式：qid \t言语数据\t标签（标签为0或者1）
		0代表非消极言语，1代表消极言语。


### 0x02.思路分析       
对于消极语言的识别可以归类为情感分析, 通过提取对话/文本中的情绪特征, 对玩家的语言进行情感评级, 以更高的分数表示正面的情感, 以较低的分数表示负面情绪, 可以通过设定阈值来调整提醒/警告/封禁的范围。     
基于百度AI开放平台的代码进行应用 (https://github.com/baidu/Senta)     
例: http://ai.baidu.com/tech/nlp/sentiment_classify (百度开放AI平台的情感计算接口 基于百度自己的深度学习框架PaddlePaddle)

注意: 数据中是按读音来划分的, 有很多生僻字体, 最好换成拼音再进行处理


### 0x03.具体实现         
+ 中文分词       
  用jieba测试了一下分词效果, 不是特别理想, 结果在all_model_segm.txt中, 主要是因为有些敏感字被屏蔽以后, 玩家用其他的字来替代, 导致分词识别不出来。      
  基于百度的LAC(https://github.com/baidu/lac) 再做一次


### 0x04.评价标准
score = 4PR / ( P + 3R ) * 100%    
P为验证集验证结果整体的准确度     
R表示验证集结果被判为消极语言在真实消极言语中的覆盖度      
 

---
# 参考文献
