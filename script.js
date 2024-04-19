// JavaScript dosyası: script.js

// Buton 1 için haritayı açan fonksiyon
function openMap1() {
    window.open('Orman_Yangınları_Ocak_Days.html');
}

// Buton 2 için haritayı açan fonksiyon
function openMap2() {
    window.open('Orman_Yangınları_Ocak_2Days.html');
}

// Buton 3 için haritayı açan fonksiyon
function openMap3() {
    window.open('Orman_Yangınları_Ocak_3Days.html');
}

// Buton öğelerini bulma ve tıklama olaylarına ilgili fonksiyonları bağlama
document.getElementById('openMapButton1').addEventListener('click', openMap1);
document.getElementById('openMapButton2').addEventListener('click', openMap2);
document.getElementById('openMapButton3').addEventListener('click', openMap3);
