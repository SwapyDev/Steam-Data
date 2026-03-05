import pandas as pd 
def transform(data):
    df = pd.DataFrame(data)
    df['Original Price'] = (df['Original Price']
                            .str.replace('Mex$ ', '')
                            .str.replace(',','')
                            .astype('float'))
    df['Current Price'] = (df['Current Price']
                           .str.replace('Mex$ ', '')
                           .str.replace(',','')
                           .astype('float'))
    df['Discount'] = (((df['Original Price'] - df['Current Price']) / df['Original Price']) * 100).round().astype('int')

    return df

