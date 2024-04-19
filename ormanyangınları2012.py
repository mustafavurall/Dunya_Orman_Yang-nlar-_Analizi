import pandas as pd
import folium
from branca.colormap import linear

# CSV dosyasını okuma
df = pd.read_csv(r'C:\Users\1must\Documents\2012veriseti2.csv')

# 'id' ve 'finaldate' sütunlarını çıkarma
df.drop(['id', 'finaldate'], axis=1, inplace=True)

# 'initialdat' sütununu datetime formatına dönüştürme
df['initialdat'] = pd.to_datetime(df['initialdat'])

# Sadece 2004 yılının Ocak ayına ait verileri filtreleme
filtered_df = df[df['initialdat'].dt.strftime('%Y-%m').eq('2012-01')]

print(filtered_df.head())

# Renk skalası oluşturma (days_between sütunu için)
colormap_days = linear.Reds_09.scale(df['days_between'].min(), df['days_between'].max())
colormap_days.caption = 'Günler Arası Fark'

# Haritayı oluşturma ve siyah arka plan ekleyerek görselleştirme
m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=3, tiles='cartodb dark_matter')

# Her bir yangın noktasını haritaya ekleyerek görselleştirme
for i in range(len(df)):
    days = df.loc[i, 'days_between']
    color_days = colormap_days(days)
    area = df.loc[i, 'area_ha']
    
    folium.CircleMarker(
        location=[df.loc[i, 'latitude'], df.loc[i, 'longitude']],
        radius=area / 70000,  # area_ha sütununa göre boyutu ayarla
        color=color_days,  # İçi dolu dairenin rengi
        fill=True,
        fill_color=color_days,
    ).add_to(m)

# Renk skalasını haritaya ekleme (sadece days_between sütunu için)
colormap_days.add_to(m)

# Haritayı kaydetme veya görüntüleme
m.save('Orman_Yangınları_Ocak_2Days.html')  # Haritayı HTML olarak kaydetme

# Haritayı tarayıcıda açma
import webbrowser
webbrowser.open('Orman_Yangınları_Ocak_2Days.html')

