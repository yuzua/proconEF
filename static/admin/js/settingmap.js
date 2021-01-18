var markers = [];
var infoWindows = [];
var markerData = data.markerData;
console.log(markerData);
function initMap() {
// マップの初期化
var map = new google.maps.Map(document.getElementById('map_canvas'), {
    zoom: 13,
    center: {lat: 35.89375928334494, lng: 139.63377508058397}
});
  // マーカー毎の処理
 for (var i = 0; i < markerData.length; i++) {
        markerLatLngs = new google.maps.LatLng({lat: Number(markerData[i]['lat']), lng: Number(markerData[i]['lng'])}); // 緯度経度のデータ作成        
        markers[i] = new google.maps.Marker({ // マーカーの追加
          position: markerLatLngs, // マーカーを立てる位置を指定
            map: map // マーカーを立てる地図を指定
        });
        infoWindows[i] = new google.maps.InfoWindow({ // 吹き出しの追加
          content: '<div class="sample">' + markerData[i]['id'] + '<input type="radio" name="car_id" value='+ markerData[i]['id'] +'>' // 吹き出しに表示する内容
        });
 
     markerEvent(i); // マーカーにクリックイベントを追加
 }
        // マーカーにクリックイベントを追加
        function markerEvent(i) {
            markers[i].addListener('click', function() { // マーカーをクリックしたとき
            infoWindows[i].open(map, markers[i]); // 吹き出しの表示
        });
        }

        //情報ウィンドウに表示するコンテンツを作成
        //urlが指定してあればリンクつきのタイトルと住所を表示（URLがない場合もあるため）
        var url = $("#url a").attr('href');
        var content;
        content = '<div id="map_content"><p><a href="' + url + '" target="_blank"> ' + title + '</a><br />' + address + '</p></div>';
 
        //情報ウィンドウのインスタンスを生成
        var infowindow = new google.maps.InfoWindow({
          content: content,
        });
 
        //marker をクリックすると情報ウィンドウを表示(リスナーの登録）
        google.maps.event.addListener(marker, 'click', function() {
          //第2引数にマーカーを指定して紐付け
          infowindow.open(map, marker);
        });
}
