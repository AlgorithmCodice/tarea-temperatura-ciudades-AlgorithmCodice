import pandas as pd

#Convertir de kelvin a celsius
def kelvin_to_celsius(k):
    return k - 273.15

#cargamos el archivo csv
df = pd.read_csv("data.csv")

#aplicaremos la conversion a las columnas de temperatura
df_celsius = df.copy()
df_celsius["San Diego"] = df["San Diego"].apply(kelvin_to_celsius)
df_celsius["Phoenix"] = df["Phoenix"].apply(kelvin_to_celsius)
df_celsius["Toronto"] = df["Toronto"].apply(kelvin_to_celsius)

print("Primeras filas convertidas a Celsius:")
print(df_celsius.head())

phoenix = df_celsius["Phoenix"]
print("-------------------------------------")
print("Analisis de Phoenix (C°)")

print("Temperatura máxima:", round(phoenix.max(), 2))
print("Temperatura mínima:", round(phoenix.min(), 2))
print("Temperatura promedio:", round(phoenix.mean(), 2))
print("Desviación estándar:", round(phoenix.std(), 2))

toronto = df_celsius["Toronto"]
print("-------------------------------------")
print("Analisis de Toronto (C°)")

print("Temperatura máxima:", round(toronto.max(), 2))
print("Temperatura mínima:", round(toronto.min(), 2))
print("Temperatura promedio:", round(toronto.mean(), 2))
print("Desviación estándar:", round(toronto.std(), 2))

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))

plt.plot(df_celsius["San Diego"], label= "San Diego")
plt.plot(df_celsius["Phoenix"], label ="Phoenix")
plt.plot(df_celsius["Toronto"], label="Toronto")

plt.title("Temperaturas en °C")
plt.xlabel("Índice (día)")
plt.ylabel("Temperatura (C°)")
plt.legend()

plt.show()

df_celsius.to_csv("data_celsius.csv", index=False)
