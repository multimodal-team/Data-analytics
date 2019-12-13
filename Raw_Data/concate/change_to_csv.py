import pandas as pd
df1 = pd.read_csv('concated_test.txt',sep = '\t')
#df2 = pd.read_csv('dev.csv')

#df_new = df1.merge(df2, on = 'VideoName', how = 'left')

df1.to_csv('dev.csv',index = 0)