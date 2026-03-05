from bs4 import BeautifulSoup
import requests
import pandas as pd

data = []
def extract():
    for start in range(0,250,50):
        url = f'https://store.steampowered.com/search/?specials=1&start={start}'
        try:
            response = requests.get(url)
            res_text = response.text
            soup = BeautifulSoup(res_text, 'html.parser')
            games = soup.find_all('a', class_ = 'search_result_row')

            for game in games:
                title = game.select_one('.title').text
                og_price = game.select_one('.discount_original_price').text
                current_price = game.select_one('.discount_final_price').text

                data.append({
                    'Game Title':title,
                    'Original Price':og_price,
                    'Current Price': current_price
                })
        except Exception as e:
            print('Error:',e) 
    df =  pd.DataFrame(data)
    return df
