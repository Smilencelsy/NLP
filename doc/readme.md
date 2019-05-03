# 游戏消极语言分析任务路线

## 数据预处理
+ 标注训练集（data_phase1.txt）
    + 筛选出 100 - 200 条具有代表性的语料
    + 对语料进行正确标注
+ 文本纠错（data_phase2.txt）
    + 有些玩家会使用错别字避开系统屏蔽词
    + 使用 pycorrector 进行文本纠错
+ 文本分词（data_phase3.txt）
    + 使用 HanLP 分词