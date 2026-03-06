from bs4 import BeautifulSoup
import requests
import pandas as pd

data = []
def extract():
    for start in range(0,2000,50):
        url = f'https://store.steampowered.com/search/?sort_by=Reviews_DESC&specials=1&start={start}'
        try:
            response = requests.get(url)
            res_text = response.text
            soup = BeautifulSoup(res_text, 'html.parser')
            games = soup.find_all('a', class_ = 'search_result_row')

            for game in games:
                title = game.select_one('.title').text
                og_price = game.select_one('.discount_original_price').text
                current_price = game.select_one('.discount_final_price').text
                image_element = game.select_one('.search_capsule img')
                source_image = image_element.get('src')
                source_game = game.get('href')

                data.append({
                    'title':title,
                    'original_price':og_price,
                    'current_price': current_price,
                    'img_src': source_image,
                    'game_src': source_game
                })
        except Exception as e:
            print('Error:',e) 
    df =  pd.DataFrame(data)
    df.to_csv('caca.csv', index=False)
    return df
