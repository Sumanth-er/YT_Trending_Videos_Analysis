import pandas as pd
import numpy as np


train_df=pd.read_csv('C:\\Users\\satya\\Desktop\\PFSD_project\\dataset\\train.csv')

print('**pre-processing of detaset**')
print('**data redundancy**')
print(train_df.columns)
print(train_df.isnull().sum())
train_df.description =train_df.description.fillna("unknown")
print(train_df.isnull().sum())

print('**dataset format**')
print(train_df.shape)
print('\n')
print(train_df.dtypes)

print('**dataset info**')
print(train_df.info)
print(train_df.isna)