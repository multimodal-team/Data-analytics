import pickle
import sys
import pandas as pd 
    
f = open('annotation_training.pkl','rb')
data = pickle.load(f,encoding='iso-8859-1')

# 先创建并打开一个文本文件
file1 = open('label1.txt', 'w', encoding='utf-8') 
file2 = open('label2.txt', 'w', encoding='utf-8') 
file3 = open('label3.txt', 'w', encoding='utf-8') 
file4 = open('label4.txt', 'w', encoding='utf-8') 
file5 = open('label5.txt', 'w', encoding='utf-8') 

file = [file1,file2,file3,file4,file5]

# 遍历字典的元素，将每项元素的key和value分拆组成字符串，注意添加分隔符和换行符
index = 0 
for k, v in data.items():
    file[index].write(str(k)+'\n')

    for key, value in v.items():
        file[index].write(str(key) + '\t' + str(value) + '\n')

    index = index + 1

# 注意关闭文件
file.close()
