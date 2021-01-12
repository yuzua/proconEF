var prices_data = Object.values(data);
var days = Object.keys(data);

dataset = [{
    label: car_name,
    data: prices_data,
    backgroundColor: "rgba(25,153,0,0.4)"
}]


var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: days,
        datasets: dataset
    }
});