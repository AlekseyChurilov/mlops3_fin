import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/m6129/UrFU_2022_python/main/Dolganov/2_%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/train.csv')
df.to_csv('/home/data1/lab1/df.csv')
print('data_creation исполнен')
