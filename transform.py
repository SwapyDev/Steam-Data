import pandas as pd 
def transform(data):
    df = pd.DataFrame(data)
    df['original_price'] = (df['original_price']
                            .str.replace('Mex$ ', '')
                            .str.replace(',','')
                            .astype('float'))
    df['current_price'] = (df['current_price']
                           .str.replace('Mex$ ', '')
                           .str.replace(',','')
                           .astype('float'))
    df['discount'] = (((df['original_price'] - df['current_price']) / df['original_price']) * 100).round().astype('int')

    return df

