var map;
function initMap() {
    for (let i = 1; i <= count; i++) {
        lat = latList[i-1];
        lng = lngList[i-1];
        latlng = new google.maps.LatLng(lat,lng);
        console.log(lat);
        console.log(lng);
        var myOptions = {
            zoom: 18,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
            
        var map = new google.maps.Map(
            document.getElementById("map"+i),
            myOptions
        );
    
        var marker = new google.maps.Marker({
            map: map,
            position: new google.maps.LatLng(lat, lng),
            animation: google.maps.Animation.DROP
        });
    }
}
