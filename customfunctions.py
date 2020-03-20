import pandas as pd
import numpy as np

def deleteSomeColumns(listColumns,df):
    for i in listColumns:
        df= df.drop(columns=i)
    return df

def categoryOnly(df, key):
    category = []
    for i in df['Category']:
        if type(i) != float: #not NaN
            if (key in i.upper() ) and (i not in category):
                category.append(i)
    return category

def dfOnly(dfALL,categories):
    column_names = list(dfALL.columns)
    dfOnly = pd.DataFrame(columns = column_names)
    for i in categories:
        df = dfALL.loc[dfALL['Category'] == i] ## loc overwrite
        dfOnly = dfOnly.append(df, ignore_index = True) 
    return dfOnly

def FreeGames(dfG):
    df = dfG.loc[dfG['Price'] == '0']
    return df

def popularOrder(df):

    df["Installs_clean"] = df["Installs"].str.replace("+","")     # df.Installs = df.Installs.apply(lambda x: x.strip("+"))
    df["Installs_clean"] = df["Installs_clean"].str.replace(",","")     # df.Installs = df.Installs.apply(lambda x: x.replace(",",""))

    # df = df.drop(['Installs'], axis=1)

    df.Installs = pd.to_numeric(df.Installs_clean)

    df = df.drop(['Installs_clean'], axis=1)

    dfSort = df.sort_values(by=['Installs'], ascending=False, ignore_index = True)

    return(dfSort)

def sizeRows(df):
    size = df.size / df.columns.size
    return(size)

def mostPopular100(df):
    df50 = df.iloc[0:100]
    return df50