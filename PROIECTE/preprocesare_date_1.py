import pandas as pd

df = pd.read_csv('jocuri_horror.csv')

df['genuri'] = df['genuri'].apply(eval)

toate_genurile = set()

for lista in df['genuri']:
    toate_genurile.update(lista)

for gen in toate_genurile:         
    def verifica_gen(lista_genuri):
        if gen in lista_genuri:     
            return 1
        else:
            return 0
    df[gen] = df['genuri'].apply(verifica_gen)

print(df.head())

df.to_csv('preprocesare_jocuri_horror.csv', index = False, encoding='utf-8')
print("Salvat cu succes")