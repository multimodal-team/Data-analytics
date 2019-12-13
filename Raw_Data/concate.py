import pandas as pd
df1 = pd.read_csv('dev.txt',sep = '\t')
df2 = pd.read_csv('dev.csv')

df_new = df1.merge(df2, on = 'VideoName', how = 'left')

df_new.to_csv('test_new.csv',index = 0)