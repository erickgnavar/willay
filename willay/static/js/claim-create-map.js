var map = L.map('map').setView([-12.0655, -77.0409], 11);
// centered in Perú

L.tileLayer('//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

$(document).ready(function () {
  var marker = null;
  var coordsRegex = /\-?(\d+\.\-?\d+)/g;
  var $point = $('#id_point');

  map.on('click', function (event) {
    if (marker === null) {
      marker = L.marker(event.latlng, {draggable: true});
      marker.addTo(map);
    } else {
      marker.setLatLng(event.latlng);
    }
    $point.val('POINT(' + event.latlng.lng + ' ' + event.latlng.lat + ')');
  });

  if ($point.val()) {
    var res = $point.val().match(coordsRegex);
    if (res.length === 2) {
      marker = L.marker(res.reverse(), {draggable: true});
      marker.addTo(map);
    }
  }
});
