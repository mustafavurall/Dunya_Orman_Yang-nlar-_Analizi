import pandas as pd
import plotly.express as px
from geopy.geocoders import Nominatim

# Veri setlerini yükle
df1 = pd.read_csv(r'C:\Users\1must\Documents\veriseti2002.csv')
df2 = pd.read_csv(r'C:\Users\1must\Documents\2012veriseti2.csv')
df3 = pd.read_csv(r'C:\Users\1must\Documents\2022veriseti.csv')

# Gereksiz sütunları kaldır
df1 = df1.drop(columns=['id'])
df2 = df2.drop(columns=['id'])
df3 = df3.drop(columns=['id'])

# Veri setlerini birleştir
df = pd.concat([df1, df2, df3])

# Aynı koordinatlara sahip satırları gruplayarak sayılarını bul
coord_counts = df.groupby(['longitude', 'latitude']).size().reset_index(name='count')

# 2 veya daha fazla tekrarlanan koordinatları filtrele
filtered_coords = coord_counts[coord_counts['count'] >= 2]

# Koordinatların hangi ülkeye ait olduğunu belirle
geolocator = Nominatim(user_agent="my_geocoder")
def get_country(row):
    location = geolocator.reverse((row['latitude'], row['longitude']), exactly_one=True)
    if location:
        return location.raw['address'].get('country', 'Unknown')
    else:
        return 'Unknown'

filtered_coords['country'] = filtered_coords.apply(get_country, axis=1)

# 3B pasta grafiği oluştur (Plotly kullanarak)
fig = px.pie(filtered_coords, values='count', names='country', title='2 veya Daha Fazla Tekrarlanan Koordinatların Ülkeleri',
             color_discrete_sequence=px.colors.sequential.Viridis)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(showlegend=False)

# Grafiği göster
fig.show()










