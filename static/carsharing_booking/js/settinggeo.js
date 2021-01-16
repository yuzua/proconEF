var markers = [];
var infoWindows = [];
var markerData = data.markerData;
console.log(markerData);
if (typeof mylocation !== 'undefined'){
  var result = new Promise(function(resolve){
    end = reverseGeocoder(mylocation)
    resolve(end);
    
  })
  result.then(function(){
    initMap(end);
  });
}else{
  initMap();
}


function initMap(home) {
  console.log('start');
  jQuery(function($){
    
    //初期のズーム レベル（指定がなければ 16）
    var zoom = $("#zoom").text() ?  parseInt($("#zoom").text()): 16;
    //マーカーのタイトル
    var title = $('#venue').text();
 
    //マップ生成のオプション
    //center は Geolocation から取得して後で設定
    var opts = {
      zoom: zoom,
      mapTypeId: "roadmap"  //初期マップ タイプ  
    };
 
    var mapDiv = document.getElementById( "map_canvas" ) ;

    // Map
    var map = new google.maps.Map( mapDiv, {
      center: new google.maps.LatLng( mylat, mylng ) ,
      zoom: zoom ,
    } ) ;

    // LatLng
    var latLng = new google.maps.LatLng( mylat, mylng, false ) ;

    // Marker
    var marker = new google.maps.Marker( {
      map: map ,
      position: latLng ,
      animation: google.maps.Animation.DROP,  
      title: title,
    } ) ;


  // マーカー毎の処理
 for (var i = 0; i < markerData.length; i++) {
        markerLatLngs = new google.maps.LatLng({lat: Number(markerData[i]['lat']), lng: Number(markerData[i]['lng'])}); // 緯度経度のデータ作成        
        markers[i] = new google.maps.Marker({ // マーカーの追加
          position: markerLatLngs, // マーカーを立てる位置を指定
            map: map // マーカーを立てる地図を指定
        });
        infoWindows[i] = new google.maps.InfoWindow({ // 吹き出しの追加
          content: '<div class="sample">' + markerData[i]['address'] + '</div><a href="/carsharing_booking/booking/'+ markerData[i]['id'] +'">ここを予約</a>' // 吹き出しに表示する内容
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
        var home = $("#address").text();
        console.log(home);
        if (url) {
          content = '<div id="map_content"><span><a href="' + url + '" target="_blank">' + title + '</a><br /><p id="home">' + home + '</p></span></div>';
        }else {
          //urlが指定してなければ、リンクなしのタイトルと住所を表示
          content = '<div id="map_content"><p>' + title + '<br />' + home + '</p></div>';
        }
 
        //情報ウィンドウのインスタンスを生成
        var infowindow = new google.maps.InfoWindow({
          content: content,
        });
 
        //marker をクリックすると情報ウィンドウを表示(リスナーの登録）
        google.maps.event.addListener(marker, 'click', function() {
          //第2引数にマーカーを指定して紐付け
          infowindow.open(map, marker);
        });
    });
};

function reverseGeocoder(mylocation){
    console.log(mylocation);
    var requestAjax=function(endpoint,callback){
      var xhr = new XMLHttpRequest();
      xhr.onreadystatechange=function(){
        if(this.readyState==4&&this.status==200){
          callback(this.response);
        }
      };
      xhr.responseType='json';
      xhr.open('GET',endpoint,true);
      xhr.send();
    };
 
    // 東京駅の緯度経度
    var apiKey='AIzaSyA8qh0jtaDs4HXKs6HAqRxvqx2xhylSSGk';
    var requestURL='https://maps.googleapis.com/maps/api/geocode/json?language=ja&sensor=false';
    requestURL+='&latlng='+mylocation;
    requestURL+='&key='+apiKey;
    requestAjax(requestURL,function(response){
      if(response.error_message){
        console.log(response.error_message);
      }else{
        var formattedAddress=response.results[0]['formatted_address'];
        // 住所は「日本、〒100-0005 東京都千代田区丸の内一丁目」の形式
        var data=formattedAddress.split(' ');
        if(data[1]){
          // id=addressに住所を設定する
          console.log(data[1]);
          document.getElementById('address').innerHTML=data[1];
        }
      }
    });
};