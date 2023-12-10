let initialLat = 53.55155259920567;
let initialLng = -2.784862739435006;

var map = L.map('map').setView([53.55155259920567, -2.784862739435006], 10);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.marker(L.marker([initialLat, initialLng]).addTo(map));


