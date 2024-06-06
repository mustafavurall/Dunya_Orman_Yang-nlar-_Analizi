// map.js
var map = L.map('map').setView([38.6395833500249, 39.7548455289002], 6); // Konumun merkezi

// OpenStreetMap taban katmanı ekle
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Her konum için marker ve popup ekle
locations.forEach(function(location) {
    // Her konum için marker oluştur
    var marker = L.marker([location.latitude, location.longitude]).addTo(map);

    // Marker'a popup içeriğini bağla
    marker.bindPopup('<b>' + location.initialdat + '</b><br>' +
                        'id: ' + location.id + '<br>' +
                     'Alan (hektar): ' + location.area_ha + '<br>' +
                     'Başlangıç: ' + location.initialdat + '<br>' +
                     'Bitiş: ' + location.finaldate + '<br>' +
                     'Günler Arası: ' + location.days_between + '<br>' +
                     '<button onclick="showSatelliteView(' + location.latitude + ', ' + location.longitude + ')">Konum Görseli</button>');
});

// Aynı days_between değerine sahip konumlar arasında çokgen oluştur
function drawPolygons() {
    var groupedLocations = {};

    // Locations verilerini days_between değerine göre grupla
    locations.forEach(function(location) {
        if (!groupedLocations[location.days_between]) {
            groupedLocations[location.days_between] = [];
        }
        groupedLocations[location.days_between].push(location);
    });

    // Her grup için çokgen oluştur
    for (var key in groupedLocations) {
        var group = groupedLocations[key];
        if (group.length > 2) {  // Çokgen oluşturmak için en az 3 nokta gerekli
            var latlngs = group.map(function(loc) {
                return [loc.latitude, loc.longitude];
            });

            // Latlngs dizisini düzgün bir çokgen oluşturacak şekilde sıraya koymak
            latlngs.sort(function(a, b) {
                return a[1] - b[1] || a[0] - b[0];
            });

            // Renkleri rastgele seçmek için bir renk dizisi
            var colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF'];
            var color = colors[key % colors.length];

            var polygon = L.polygon(latlngs, { color: color }).addTo(map);
        }
    }
}

// Uydu görüntüsünü göster
function showSatelliteView(lat, lon) {
    var url = 'https://www.google.com/maps/@' + lat + ',' + lon + ',15z/data=!3m1!1e3'; // Google Maps uydu görüntüsü URL'si
    window.open(url, '_blank'); // Uydu görüntüsünü yeni bir sekmede aç
}

// Çizgileri çiz
drawPolygons();


