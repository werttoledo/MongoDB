from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Conectar a MongoDB (asegúrate de que tu servidor esté ejecutándose)
client = MongoClient('mongodb://localhost:27017/')
db = client['actividad']
collection = db['base']

# Obtener datos desde MongoDB y convertirlos a un DataFrame
data = pd.DataFrame(list(collection.find()))

# Verificar que los datos se cargaron correctamente
print("Primeras filas de los datos:")
print(data.head())

# Asegurarse de que el campo 'CANTIDAD' sea numérico
data['CANTIDAD'] = pd.to_numeric(data['CANTIDAD'], errors='coerce')

# Graficar la cantidad por clase de bien
plt.figure(figsize=(12, 6))
sns.barplot(x='CLASE BIEN', y='CANTIDAD', data=data)
plt.title('Cantidad por Clase de Bien')
plt.xticks(rotation=45)
plt.xlabel('Clase de Bien')
plt.ylabel('Cantidad')
plt.show()
