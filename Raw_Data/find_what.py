import pandas as pd

def a():
    df = pd.read_csv('train.csv')
    df2 = pd.read_csv('dev.csv')

    train_name = []
    test_name = []

    train_name_real = []
    test_name_real = []

    for index, rows in df.iterrows():
        train_name_real.append(str(rows['VideoName']))
        Namelist = str(rows['VideoName']).split(sep = '.')
        Name = Namelist[0]
        train_name.append(Name)

    for index, rows in df2.iterrows():
        test_name_real.append(str(rows['VideoName']))
        Namelist = str(rows['VideoName']).split(sep = '.')
        Name = Namelist[0]
        test_name.append(Name)

    cross_name = []
    for index, i in enumerate(test_name):
        if i not in train_name:
            cross_name.append(test_name_real[index])

    with open('cross1.txt','w',encoding='utf-8') as f:
        for i in cross_name:
            f.write(i+'\n')

    print(len(cross_name))

if __name__ == '__main__':
    df = pd.read_csv('cross1.txt')
    df2 = pd.read_csv('predit_data.csv')

    NameList = []

    for index,rows in df.iterrows():
        NameList.append(rows['VideoName'])

    for index,rows in df2.iterrows():
        if rows['VideoName'] in NameList:
            df2.at[index, 'YES'] = 1

    df2.to_csv('predit_data.csv',index = 0)
    


    