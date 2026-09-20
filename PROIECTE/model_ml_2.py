import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv('preprocesare_jocuri_horror.csv')
print(df.columns)

X = df[['pret', 'Strategy', 'Simulation', 'Early Access', 'Action', 
        'Adventure', 'Free To Play', 'RPG', 'Casual', 'Indie']]
y = df['recenzii']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.shape)
print(X_test.shape)

model1 = LinearRegression()
model1.fit(X_train, y_train)

predictii1 = model1.predict(X_test)
print(predictii1)
print(y_test.values)

rmse1 = mean_squared_error(y_test, predictii1) ** 0.5
r2_1 = r2_score(y_test, predictii1)

print("RMSE:", rmse1)
print("R²:", r2_1)

model2 = RandomForestRegressor(random_state=42)
model2.fit(X_train, y_train)

predictii2 = model2.predict(X_test)

rmse2 = mean_squared_error(y_test, predictii2) ** 0.5
r2_2 = r2_score(y_test, predictii2)

print("RMSE:", rmse2)
print("R²:", r2_2)

joc_nou = pd.DataFrame({
    'pret': [19.99],
    'Strategy': [0], 'Simulation': [0], 'Early Access': [0],
    'Action': [1], 'Adventure': [1], 'Free To Play': [0],
    'RPG': [0], 'Casual': [0], 'Indie': [1]
})

predictie_noua = model2.predict(joc_nou)
print("Recenzii estimate:", predictie_noua)