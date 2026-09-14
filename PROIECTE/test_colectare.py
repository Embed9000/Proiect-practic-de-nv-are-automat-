import requests as rq
import pandas as pd

raspuns = rq.get("https://steamspy.com/api.php?request=genre&genre=RPG")
data = raspuns.json()

print(type(data))
print(len(data))

primul_id = list(data.keys())[0]
#print(data[primul_id])

games_ip = []
games_list = []

max_games = 200
toate_ip_urile = list(data.keys())
games_ip = toate_ip_urile[0:max_games]

for ip in games_ip:
    #break
    info = data[str(ip)]

    nume = info['name']
    pret = int(info['price']) / 100
    positive = info['positive']
    negative = info['negative']
    total_reviews = int(positive) + int(negative)

    print("-------------------------------------------------------------------------")
    print(nume, pret, positive, negative)

    games_list.append({
        'nume': nume,
        'pret': pret,
        'positive': positive,
        'negative': negative,
        'total_reviews': total_reviews
    })

df = pd.DataFrame(games_list)
df.to_csv('jocuri_rpg.csv', index = False, encoding='utf-8')

print("SalvatCuSucces!")

df_verificare = pd.read_csv('jocuri_rpg.csv')

print(df_verificare.shape)
print(df_verificare.isnull().sum())
print(df_verificare.duplicated().sum())
print(df_verificare.describe())