var options = {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0
};
  
function success(pos) {
    var crd = pos.coords;
  
    console.log('Your current position is:');
    console.log(`Latitude : ${crd.latitude}`);
    console.log(`Longitude: ${crd.longitude}`);
    console.log(`More or less ${crd.accuracy} meters.`);
  
    var ele = document.createElement('input');
      // データを設定
    ele.setAttribute('type', 'hidden');
    ele.setAttribute('name', 'latlng');
    ele.setAttribute('value', crd.latitude+','+crd.longitude);
      // 要素を追加
    document.myForm.appendChild(ele);
    var ele = document.createElement('input');
      // データを設定
    ele.setAttribute('type', 'hidden');
    ele.setAttribute('name', 'lat');
    ele.setAttribute('value', crd.latitude);
      // 要素を追加
    document.myForm.appendChild(ele);
    var ele = document.createElement('input');
      // データを設定
    ele.setAttribute('type', 'hidden');
    ele.setAttribute('name', 'lng');
    ele.setAttribute('value', crd.longitude);
      // 要素を追加
    document.myForm.appendChild(ele);
}
  
function error(err) {
    console.warn(`ERROR(${err.code}): ${err.message}`);
    var ele = document.createElement('input');
      // データを設定
    ele.setAttribute('type', 'hidden');
    ele.setAttribute('name', 'error');
    ele.setAttribute('value', err.code);
      // 要素を追加
    document.myForm.appendChild(ele);
}
  

navigator.geolocation.getCurrentPosition(success, error, options);