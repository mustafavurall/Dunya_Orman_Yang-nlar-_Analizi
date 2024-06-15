import pandas as pd

# CSV dosyasını oku
df = pd.read_csv('C:/Users/1must/Downloads/TheTrailofFire_A20YearHistoryofWildfires (4).csv')

# Türkiye koordinat aralıklarını belirle
latitude_min, latitude_max = 36.0, 42.0
longitude_min, longitude_max = 26.0, 45.0

# Türkiye'ye ait konumları filtrele
turkey_data = df[(df['latitude'] >= latitude_min) & (df['latitude'] <= latitude_max) &
                 (df['longitude'] >= longitude_min) & (df['longitude'] <= longitude_max)]

# Sadece initialdat sütunu 2022 yılında başlayanları filtrele
turkey_data['initialdat'] = pd.to_datetime(turkey_data['initialdat'])  # Tarih formatına çevir
turkey_data_2002 = turkey_data[turkey_data['initialdat'].dt.year == 2002]

# Sadece 06, 07 ve 08 aylarındaki verileri filtrele
summer_months = [6, 7, 8]
turkey_data_summer_2002 = turkey_data_2002[turkey_data_2002['initialdat'].dt.month.isin(summer_months)]

# Sonuçları kontrol et
print(turkey_data_summer_2002)

# Türkiye'ye ait ve 2022 yılının 06-07-08 aylarına ait verileri yeni bir CSV dosyasına kaydet
turkey_data_summer_2002.to_csv('turkiye_summer_2002_verileri.csv', index=False)




