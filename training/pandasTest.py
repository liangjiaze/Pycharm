import numpy as np
import pandas as pd

def main():
 s = pd.Series([i*2 for i in range(1,11)])
 print(type(s))
dates = pd.date_range('20170301',periods=8)
df = pd.DataFrame(np.random.randn(8,5), index=dates,columns=list('ABCDE'))
print(df)

#Basic
print(df.head(3))
print(df.tail(3))
print(df.index)
print(df.values)
print(df.T)
print(df.sort_index(axis=1,ascending=False))
print(df.sort_values('C'))
print(df.describe())

#Select
print(type(df['A']))
print(df[1:3])
print(df['20170301':'20170304'])
print(df.loc[dates[0]])
print(df.loc['20170301':'20170304',['B','D']])
print(df.at[dates[0],'C'])
print(df.iloc[1:3,2:4])
print(df.iloc[1,3])
print(df.iat[1,4])



if __name__ == '__main__':
    main()





