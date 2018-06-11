var map = L.map('map').setView([-12.0655, -77.0409], 11);
// centered in Perú
var markers = L.markerClusterGroup();

L.tileLayer('//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);


$(document).ready(function () {
  $.getJSON('/map/data/', function (response) {
    function onEachFeature(feature, layer) {
      var template = '<a href="#url">#name</a>';
      template += '<p>#address</p>';
      template += '<p>#content</p>';
      var compiled = template.replace('#url', feature.properties.url);
      compiled = compiled.replace('#name', feature.properties.category_name);
      compiled = compiled.replace('#address', feature.properties.address);
      compiled = compiled.replace('#content', feature.properties.description);
      layer.bindPopup(compiled);
    }

    function pointToLayer(feature, latlng) {
      var icon = L.icon({
        iconUrl: feature.properties.marker_icon,
      });
      return L.marker(latlng, {
        icon: icon,
      });
    }

    L.geoJSON(response, {
      onEachFeature: onEachFeature,
      pointToLayer: pointToLayer,
    }).addTo(markers);
    map.addLayer(markers);
    map.fitBounds(markers.getBounds());
  });
});
