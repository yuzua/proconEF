var key = Object.keys(car_name);

var id_0_name = car_name.id_0;
var days = Object.keys(id_0);
var id_0_prices = Object.values(id_0);

var id_2_name = car_name.id_2;
var id_2_prices = Object.values(id_2);

var id_3_name = car_name.id_3;
var id_3_prices = Object.values(id_3);

var id_5_name = car_name.id_5;
var id_5_prices = Object.values(id_5);

var id_9_name = car_name.id_9;
var id_9_prices = Object.values(id_9);

var id_10_name = car_name.id_10;
var id_10_prices = Object.values(id_10);

var id_11_name = car_name.id_11;
var id_11_prices = Object.values(id_11);

var id_22_name = car_name.id_22;
var id_22_prices = Object.values(id_22);

var id_23_name = car_name.id_23;
var id_23_prices = Object.values(id_23);

var id_24_name = car_name.id_24;
var id_24_prices = Object.values(id_24);

var id_27_name = car_name.id_27;
var id_27_prices = Object.values(id_27);

var id_32_name = car_name.id_32;
var id_32_prices = Object.values(id_32);

var id_35_name = car_name.id_35;
var id_35_prices = Object.values(id_35);

var id_49_name = car_name.id_49;
var id_49_prices = Object.values(id_49);

var id_50_name = car_name.id_50;
var id_50_prices = Object.values(id_50);

var id_56_name = car_name.id_56;
var id_56_prices = Object.values(id_56);

var id_57_name = car_name.id_57;
var id_57_prices = Object.values(id_57);

var id_58_name = car_name.id_58;
var id_58_prices = Object.values(id_58);

var id_59_name = car_name.id_59;
var id_59_prices = Object.values(id_59);

var id_60_name = car_name.id_60;
var id_60_prices = Object.values(id_60);

var id_61_name = car_name.id_61;
var id_61_prices = Object.values(id_61);

var id_62_name = car_name.id_62;
var id_62_prices = Object.values(id_62);

var id_63_name = car_name.id_63;
var id_63_prices = Object.values(id_63);  

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
    if (item == "id_0"){
      dataset.push(id_0);
    }else if(item == "id_2"){
      dataset.push(id_2);
    }else if(item == "id_3"){
      dataset.push(id_3);
    }else if(item == "id_5"){
      dataset.push(id_5);
    }
    else if(item == "id_9"){
      dataset.push(id_9);
    }
    else if(item == "id_10"){
      dataset.push(id_10);
    }
    else if(item == "id_11"){
      dataset.push(id_11);
    }
    else if(item == "id_22"){
      dataset.push(id_22);
    }
    else if(item == "id_23"){
      dataset.push(id_23);
    }
    else if(item == "id_24"){
      dataset.push(id_24);
    }
    else if(item == "id_27"){
      dataset.push(id_27);
    }
    else if(item == "id_32"){
      dataset.push(id_32);
    }
    else if(item == "id_35"){
      dataset.push(id_35);
    }
    else if(item == "id_49"){
      dataset.push(id_49);
    }
    else if(item == "id_50"){
      dataset.push(id_50);
    }
    else if(item == "id_56"){
      dataset.push(id_56);
    }
    else if(item == "id_57"){
      dataset.push(id_57);
    }
    else if(item == "id_58"){
      dataset.push(id_58);
    }
    else if(item == "id_59"){
      dataset.push(id_59);
    }
    else if(item == "id_60"){
      dataset.push(id_60);
    }
    else if(item == "id_61"){
      dataset.push(id_61);
    }
    else if(item == "id_62"){
      dataset.push(id_62);
    }
    else if(item == "id_63"){
      dataset.push(id_63);
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
id_0 = {
  label: id_0_name,
  data: id_0_prices,
  backgroundColor: "rgba(255,153,0,0.4)"
}
id_2 = {
  label: id_2_name,
  data: id_2_prices,
  backgroundColor: "rgba(125,145,0,0.4)"
}
id_3 = {
  label: id_3_name,
  data: id_3_prices,
  backgroundColor: "rgba(315,315,0,0.4)"
}
id_5 = {
  label: id_5_name,
  data: id_5_prices,
  backgroundColor: "rgba(415,145,0,0.4)"
}
id_9 = {
  label: id_9_name,
  data: id_9_prices,
  backgroundColor: "rgba(15,15,0,0.4)"
}
id_10 = {
  label: id_10_name,
  data: id_10_prices,
  backgroundColor: "rgba(15,15,0,0.4)"
}
id_11 = {
  label: id_11_name,
  data: id_11_prices,
  backgroundColor: "rgba(15,15,0,0.4)"
}
id_22 = {
  label: id_22_name,
  data: id_22_prices,
  backgroundColor: "rgba(15,15,0,0.4)"
}
id_23 = {
  label: id_23_name,
  data: id_23_prices,
  backgroundColor: "rgba(15,15,0,0.4)"
}
id_24 = {
  label: id_24_name,
  data: id_24_prices,
  backgroundColor: "rgba(15,15,0,0.4)"
}
id_27 = {
  label: id_27_name,
  data: id_27_prices,
  backgroundColor: "rgba(15,15,0,0.4)"
}
id_32 = {
  label: id_32_name,
  data: id_32_prices,
  backgroundColor: "rgba(15,15,0,0.4)"
}
id_35 = {
  label: id_35_name,
  data: id_35_prices,
  backgroundColor: "rgba(15,15,0,0.4)"
}
id_49 = {
  label: id_49_name,
  data: id_49_prices,
  backgroundColor: "rgba(15,15,0,0.4)"
}
id_50 = {
  label: id_50_name,
  data: id_50_prices,
  backgroundColor: "rgba(15,15,0,0.4)"
}
id_56 = {
  label: id_56_name,
  data: id_56_prices,
  backgroundColor: "rgba(15,15,0,0.4)"
}
id_57 = {
  label: id_57_name,
  data: id_57_prices,
  backgroundColor: "rgba(15,15,0,0.4)"
}
id_58 = {
  label: id_58_name,
  data: id_58_prices,
  backgroundColor: "rgba(15,15,0,0.4)"
}
id_59 = {
  label: id_59_name,
  data: id_59_prices,
  backgroundColor: "rgba(15,15,0,0.4)"
}
id_60 = {
  label: id_60_name,
  data: id_60_prices,
  backgroundColor: "rgba(15,15,0,0.4)"
}
id_61 = {
  label: id_61_name,
  data: id_61_prices,
  backgroundColor: "rgba(15,15,0,0.4)"
}
id_62 = {
  label: id_62_name,
  data: id_62_prices,
  backgroundColor: "rgba(15,15,0,0.4)"
}
id_63 = {
  label: id_63_name,
  data: id_63_prices,
  backgroundColor: "rgba(15,15,0,0.4)"
}
// 必要データ

dataset = [];


var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: days,
      datasets: dataset,
    }
});


//チェックボックスをクリックするとイベント発火
$("input[type=checkbox]").click(function(){
    var $count = $("input[type=checkbox]:checked").length;
    var $not = $('input[type=checkbox]').not(':checked')

        //チェックが3つ付いたら、チェックされてないチェックボックスにdisabledを加える
    if($count >= 3) {
        $not.attr("disabled",true);
    }else{
        //3つ以下ならisabledを外す
        $not.attr("disabled",false);
    }
});
