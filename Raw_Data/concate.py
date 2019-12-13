import pandas as pd
df1 = pd.read_csv('concated_dev.txt',sep = '\t')
df2 = pd.read_csv('dev.txt', sep = '\t')

df_new = df2.merge(df1, on = 'VideoName')

df_new.to_csv('dev_combined.txt',sep = '\t', index = 0)