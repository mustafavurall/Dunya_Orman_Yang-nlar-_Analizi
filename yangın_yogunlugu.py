import pandas as pd
import numpy as np

# Verisetlerini yükle
df1 = pd.read_csv(r'C:\Users\1must\Documents\veriseti2002.csv')
df2 = pd.read_csv(r'C:\Users\1must\Documents\2012veriseti2.csv')
df3 = pd.read_csv(r'C:\Users\1must\Documents\2022veriseti.csv')

# Gereksiz sütunları kaldır
df1 = df1.drop(columns=['id', 'finaldate'])
df2 = df2.drop(columns=['id', 'finaldate'])
df3 = df3.drop(columns=['id', 'finaldate'])

# Tarih sütununu düzelt (gerekiyorsa)
# Örnek: df1['initialdat'] = pd.to_datetime(df1['initialdat'])

# Verisetlerini birleştir
df = pd.concat([df1, df2, df3])

# Örneğin, yangınların yoğun olduğu bölgeleri temsil eden bir özellik oluşturalım
df['yangin_yogunlugu'] = np.sqrt(df['area_ha'] * df['days_between'])

import matplotlib.pyplot as plt

# Örnek bir görselleştirme (isteğe bağlı)
plt.scatter(df['longitude'], df['latitude'], c=df['yangin_yogunlugu'], cmap='viridis', alpha=0.5)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.colorbar(label='Yangın Yoğunluğu')
plt.title('Yangın Yoğunluğu Haritası')
plt.show()

# Verileri analiz etmek için istatistiksel analizler yapabilirsiniz
# Örnek: df.describe(), df.corr() gibi



