import pandas as pd 
df1 = pd.read_csv('train.txt',sep = '\t')
df2 = pd.read_csv('dev.txt',sep = '\t')

df1 = df1.loc[:,['context', 'extraversion']]
df2 = df2.loc[:,['context', 'extraversion']]

#平均映射
for index,rows in df1.iterrows():
    if 0 < rows[1] <= 0.2:
        df1.at[index, 'ValueExtraversion'] = '0'
    elif 0.2 < rows[1] <= 0.4:
        df1.at[index, 'ValueExtraversion'] = '1'
    elif 0.4 < rows[1] <= 0.55:
        df1.at[index, 'ValueExtraversion'] = '2'
    elif 0.55 < rows[1] <= 0.7:
        df1.at[index, 'ValueExtraversion'] = '3'
    elif 0.7 < rows[1] <= 1:
        df1.at[index, 'ValueExtraversion'] = '4'

for index, rows in df2.iterrows():
    if 0 < rows[1] <= 0.2:
        df2.at[index, 'ValueExtraversion'] = '0'
    elif 0.2 < rows[1] <= 0.4:
        df2.at[index, 'ValueExtraversion'] = '1'
    elif 0.4 < rows[1] <= 0.55:
        df2.at[index, 'ValueExtraversion'] = '2'    
    elif 0.55 < rows[1] <= 0.7:
        df2.at[index, 'ValueExtraversion'] = '3'
    elif 0.7 < rows[1] <= 1:
        df2.at[index, 'ValueExtraversion'] = '4'

df1 = df1.loc[:,['context','ValueExtraversion']]
df2 = df2.loc[:,['context','ValueExtraversion']]

df1.to_csv('train_Unavg.tsv', sep = '\t', index = 0)
df2.to_csv('test_Unavg.tsv', sep = '\t', index = 0)
