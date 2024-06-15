// Haritayı oluştur
var map = L.map('map').setView([38.9637, 35.2433], 6); // Türkiye merkezli

// GeoJSON dosyasını yükle ve haritaya ekle
fetch('turkey.geojson')
    .then(response => response.json())
    .then(data => {
        L.geoJSON(data, {
            style: {
                color: "black", // Sınır rengi siyah
                weight: 2, // Sınır kalınlığı
                fillColor: "black", // İç dolgu rengi siyah
                fillOpacity: 0.1 // İç dolgu opaklığı
            }
        }).addTo(map);
        
        // Harita sınırlarını Türkiye'ye göre ayarla
        map.fitBounds([
            [36, 26],
            [42, 45]
        ]);
        
        // Kare şekilli markerlar oluştur
        var colorScale = d3.scaleSequential(d3.interpolateRgb("red", "black"))
            .domain(d3.extent(locations, function(d) { return d.days_between; }));

        locations.forEach(function(location) {
            var size = Math.sqrt(location.area_ha) / 300; // `area_ha` değerine göre boyut ayarlama
            var latlng = [location.latitude, location.longitude];
            var color = colorScale(location.days_between); // `days_between` değerine göre renk ayarlama

            var square = L.rectangle([
                [latlng[0] - size / 2, latlng[1] - size / 2],
                [latlng[0] + size / 2, latlng[1] + size / 2]
            ], {
                color: color, // Kenar rengi
                weight: 1, // Kenar kalınlığı
                fillColor: color, // Dolgu rengi
                fillOpacity: 0.5 // İç dolgu opaklığı
            }).addTo(map);

            square.bindPopup('<b>' + location.initialdat + '</b><br>' +
            'id: ' + location.id + '<br>' +
            'Alan (hektar): ' + location.area_ha + '<br>' +
            'Başlangıç: ' + location.initialdat + '<br>' +
            'Bitiş: ' + location.finaldate + '<br>' +
            'Günler Arası: ' + location.days_between + '<br>' );
        });
    });
