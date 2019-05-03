#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pycorrector


# In[22]:


f = open('data_phase1.txt','r')
lines = f.readlines()
for line in lines:
    block = line.split(" ")
    corrected_sent, detail = pycorrector.correct(block[1])
    with open("data_phase2.txt","a") as f:
        f.write(block[0]+" "+corrected_sent+" "+block[2])

