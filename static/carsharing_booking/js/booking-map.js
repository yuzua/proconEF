var map;
function initMap() {
    
    spot = new google.maps.LatLng(lat,lng);

    var opts = {
      zoom: 19,
      center: spot
    };
    
    map = new google.maps.Map(document.getElementById("map"), opts);
  
    var marker = new google.maps.Marker({
        map: map,
        position: new google.maps.LatLng(lat, lng),
        animation: google.maps.Animation.DROP
    });
}