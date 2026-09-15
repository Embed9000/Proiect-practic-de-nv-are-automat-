import requests as rq
import pandas as pd

extragere_api = rq.get("https://steamspy.com/api.php?request=genre&genre=Early+Access")
data = extragere_api.json()

print(len(data))

max_games = 100
my_games_api = []
my_list_of_games = []

toate_api_urile = []
toate_api_urile = list(data.keys())
my_games_api = toate_api_urile[0:max_games]

for api_game in my_games_api:
    name = data[api_game]['name']
    positive = data[api_game]['positive']
    negative = data[api_game]['negative']
    total = positive + negative
    pret = data[api_game]['price']

    my_list_of_games.append({
        'Name': name,
        'Positive': positive,
        'Negative': negative,
        'Total': total,
        'Price': pret,
    })

df = pd.DataFrame(my_list_of_games)
df.to_csv('jocuri_earlyAcces.csv', index = False, encoding='utf-8')
