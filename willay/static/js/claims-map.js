var map = L.map('map').setView([-12.0655, -77.0409], 11);
// centered in Perú

L.tileLayer('//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

$(document).ready(function () {
  $.getJSON('/map/data/', function (response) {
    function onEachFeature(feature, layer) {
      var template = '<a href="#url">#name</a>';
      template += '<p>#content</p>';
      var compiled = template.replace('#url', feature.properties.url);
      compiled = compiled.replace('#name', feature.properties.category_name);
      compiled = compiled.replace('#content', feature.properties.description);
      layer.bindPopup(compiled);
    }
    L.geoJSON(response, {
      onEachFeature: onEachFeature,
    }).addTo(map);
  });
});
