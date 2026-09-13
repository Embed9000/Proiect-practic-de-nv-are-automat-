import requests
import pandas as pd
import matplotlib.pyplot as plt

#response = requests.get("https://steamspy.com/api.php?request=genre&genre=Horror")
#data = response.json()

appids_horror = [
    739630,   # Phasmophobia
    381210,   # Dead by Daylight
    57300,    # Amnesia: The Dark Descent
    238320,   # Outlast
    282140,   # SOMA
    1721470,  # Poppy Playtime
    391720,   # Layers of Fear
    214490,   # Alien: Isolation
    1966720,  # Lethal Company
    3241660,  # R.E.P.O.
    883710,   # Resident Evil 2
    1196590,  # Resident Evil Village
    418370,   # Resident Evil 7 Biohazard
    952060,   # Resident Evil 3
    304240,   # Resident Evil
    221040,   # Resident Evil 6
    21690,    # Resident Evil 5
    339340,   # Resident Evil 0
    254700,   # Resident Evil 4 (2005)
    287290,   # Resident Evil Revelations 2
    698670,   # Doki Doki Literature Club!
    1943950,  # Escape the Backrooms
    1987080,  # Inside the Backrooms
    1929610,  # Demonologist
    967050,   # Pacify
    319510,   # Five Nights at Freddy's
    871720,   # Ultimate Custom Night
    747660,   # Five Nights at Freddy's: Security Breach
    738060,   # Freddy Fazbear's Pizzeria Simulator
    356670,   # Spooky's Jump Scare Mansion
    2835570,  # Buckshot Roulette
    343710,   # Kholat
    223710,   # Cry of Fear
    414700,   # Outlast 2
    1304930,  # The Outlast Trials
    238430,   # Contagion
    700330,   # SCP: Secret Laboratory
    493520,   # GTFO
    262060,   # Darkest Dungeon
    274520,   # Darkwood
    239200,   # Amnesia: A Machine for Pigs
    601430,   # The Evil Within 2
    268050,   # The Evil Within
    424840,   # Little Nightmares
    860510,   # Little Nightmares II
    2527500,  # MiSide
    1451940,  # NEEDY STREAMER OVERLOAD
    1150690,  # OMORI
]

#print(type(data))
#print(len(data))

rezultatele = []

for appid in appids_horror:
    url = f"https://store.steampowered.com/api/appdetails?appids={appid}&cc=us"

    response = requests.get(url)
    data = response.json()

    info = data[str(appid)]['data']

    nume = info['name']
    genuri = [g['description']for g in info['genres']]
    
    if 'price_overview' in info:
        pret = info['price_overview']['final'] / 100
    else:
        pret = 0

    if 'recommendations' in info:
        recenzii = info['recommendations']['total']
    else:
        recenzii = 0

    rezultatele.append({
        'nume': nume,
        'genuri': genuri,
        'pret': pret,
        'recenzii': recenzii
    })

    print(nume, genuri, pret, recenzii)

df = pd.DataFrame(rezultatele)
df.to_csv('jocuri_horror.csv', index = False, encoding='utf-8')

print("salvat cu succes")

df_verificare = pd.read_csv('jocuri_horror.csv')

print(df_verificare.shape)
print(df_verificare.isnull().sum())
print(df_verificare.duplicated().sum())

print(df_verificare.describe())

df_verificare['recenzii'].hist(bins=15)
plt.xlabel('Numar recenzii')
plt.ylabel('Numar jocuri')
plt.title('Distributia recenziilor')
plt.show()