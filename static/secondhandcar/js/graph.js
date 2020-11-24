check_list = [];
function myfunc(value) {
var flag = document.getElementById(value).checked;
  if(flag == true){
    
    check_list.push(value);
    console.log(check_list);
  }else{
    
    check_list = check_list.filter(function(a) {
      return a !== value;
    });
    console.log(check_list);
  }
  for (item of check_list){
    console.log(item);
    if (item == "purius"){
      dataset.push(purius_data);
    }else if(item == "minimini"){
      dataset.push(minimini_data);
    }
  }
  console.log(dataset);
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: days,
      datasets: dataset,
    }
  });
  
  dataset = [];
}

// 必要データ(車種名、グラフ色)
purius_data = {
  label: 'プリウス(トヨタ)',
  data: purius_prices,
  backgroundColor: "rgba(255,153,0,0.4)"
}
minimini_data = {
  label: 'ミニ(ミニ)',
  data: minimini_prices,
  backgroundColor: "rgba(125,145,0,0.4)"
}
// 必要データ
data_list = [purius, minimini];
dataset = [];


var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: days,
      datasets: dataset,
    }
});
