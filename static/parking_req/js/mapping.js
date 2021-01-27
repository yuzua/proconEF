function initMap() {

      // マップの初期化
      var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
        center: {lat: 35.89375928334494, lng: 139.63377508058397}
      });

      // クリックイベントを追加
      map.addListener('click', function(e) {
        getClickLatLng(e.latLng, map);
      });
    }

    function getClickLatLng(lat_lng, map) {

      // 座標を表示
      document.getElementById('lat').textContent = lat_lng.lat();
      document.getElementById('lng').textContent = lat_lng.lng();
      document.forms[0].elements['name_input_lat'].value = lat_lng.lat();
      document.forms[0].elements['name_input_lng'].value = lat_lng.lng();
    // マーカーを設置  
	var marker = new google.maps.Marker({
        position: lat_lng,
        map: map
      });
    console.log(marker);
    // 座標の中心をずらす
    // http://syncer.jp/google-maps-javascript-api-matome/map/method/panTo/
    map.panTo(lat_lng);
    }

        $("#myform").submit( function(event) {
        event.preventDefault();
        var form = $(this);
        console.log(form);
        $.ajax({
          url: form.prop("action"),
          method: form.prop("method"),
          data: form.serializeArray(),
          timeout: 10000,
          dataType: "text",
        })
        .done( function(data) {
          alert(data);
          $("#id_div_ajax_response").text(data);
          $("#id_div_ajax_response").html("<a href='/parking_req/create' class='btn'>create</a>");
        })
      });
