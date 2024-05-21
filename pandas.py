import pandas as pd
data = pd.read_csv('/content/1k-sample-products.csv')
type(data)
data.info()
data.describe()
data=data.drop_duplicates()
data
data.isnull()
data.isnull().sum()
data.notnull()
data.notnull().sum()
data2=data.fillna(value=0)
data2
data2.isnull().sum().sum()
data3=data.fillna(method='pad')#forward filling
data3
data4=data.fillna(method='bfill')
data4
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
# data4.drop(['ID'],axis=1,inplace=True)
data4.columns
data
numeric_data = data.select_dtypes(include=[np.number])
Q1= numeric_data.quantile(0.25)
Q3= numeric_data.quantile(0.75)
IQR=Q3-Q1
print(IQR)
data2.columns
Next steps:
numeric_data=numeric_data[~((numeric_data<(Q1-1.5*IQR)) |(numeric_data>(Q3+1.5*IQR))).any(axis=1)]
numeric_data
Show hidden output