$('#form').ready(function(){
    $("input").hover(
    function () {

    }, 
    function () {

        var start_day = $('#id_start_day').val();

        var start_time = $('#id_start_time').val();

        var end_day = $('#id_end_day').val();

        var end_time = $('#id_end_time').val();

        if (start_day != "" && start_time != "" && end_day != "" && end_time != "") {

            var startdate = new Date(start_day.replace(/-/g,"/") + ' ' + start_time + ':00');
            var enddate = new Date(end_day.replace(/-/g,"/") + ' ' + end_time + ':00');
            var answertime = (enddate.getTime() - startdate.getTime())/1000/60;
            // var answerdate = enddate.getDate() - startdate.getDate();
            var answerdate = Math.floor(answertime/60/24);
            var charge = 0;
            var times = '';

            if (answerdate <= 0){

            }else{
                charge = answerdate * 20000;
                times = answerdate.toString() + '日 ';
                answertime -= 1440 * answerdate;
            }
            if(start_time < end_time){
                charge += answertime / 15 * 225;
                var result_h = Math.floor(answertime / 60);
                if (result_h >= 24){
                    result_h -= 24;
                }
                var result_m = answertime % 60;
                var x = result_h.toString() + '時間 ' + result_m.toString() + '分';
                times += x;
            }else{
                charge += answertime / 15 * 225;
                var result_h = Math.floor(answertime / 60);
                if (result_h >= 24){
                    result_h -= 24;
                }
                var result_m = answertime % 60;
                var x = result_h.toString() + '時間 ' + result_m.toString() + '分';
                times += x;
            }
            if (answerdate <= 0 && result_h <= 0 && answertime <= 15){
                console.log('15分未満は利用できません')
                $('#jquery').html('<p>15分未満は利用できません</p>');
            }else{
                charge = changeYen(Math.floor(charge));
                function changeYen(num){
                    return　'¥' + String(num).replace(/(\d)(?=(\d\d\d)+(?!\d))/g, '$1,')
                }
                $('#jquery').html('<p>ご利用時間： ' + times + '</p><p>お支払い金額： ' + charge + '</p>');
                console.log(times);
                console.log(charge);
            }
        }
    }
    );

});

$('#form').ready(function(){
    $("label").hover(
    function () {

    }, 
    function () {

        var start_day = $('#id_start_day').val();

        var start_time = $('#id_start_time').val();

        var end_day = $('#id_end_day').val();

        var end_time = $('#id_end_time').val();

        if (start_day != "" && start_time != "" && end_day != "" && end_time != "") {

            var startdate = new Date(start_day.replace(/-/g,"/") + ' ' + start_time + ':00');
            var enddate = new Date(end_day.replace(/-/g,"/") + ' ' + end_time + ':00');
            var answertime = (enddate.getTime() - startdate.getTime())/1000/60;
            // var answerdate = enddate.getDate() - startdate.getDate();
            var answerdate = Math.floor(answertime/60/24);
            var charge = 0;
            var times = '';

            if (answerdate <= 0){

            }else{
                charge = answerdate * 20000;
                times = answerdate.toString() + '日 ';
                answertime -= 1440 * answerdate;
            }
            if(start_time < end_time){
                charge += answertime / 15 * 225;
                var result_h = Math.floor(answertime / 60);
                if (result_h >= 24){
                    result_h -= 24;
                }
                var result_m = answertime % 60;
                var x = result_h.toString() + '時間 ' + result_m.toString() + '分';
                times += x;
            }else{
                charge += answertime / 15 * 225;
                var result_h = Math.floor(answertime / 60);
                if (result_h >= 24){
                    result_h -= 24;
                }
                var result_m = answertime % 60;
                var x = result_h.toString() + '時間 ' + result_m.toString() + '分';
                times += x;
            }
            if (answerdate <= 0 && result_h <= 0 && answertime <= 15){
                console.log('15分未満は利用できません')
                $('#jquery').html('<p>15分未満は利用できません</p>');
            }else{
                charge = changeYen(Math.floor(charge));
                function changeYen(num){
                    return　'¥' + String(num).replace(/(\d)(?=(\d\d\d)+(?!\d))/g, '$1,')
                }
                $('#jquery').html('<p>ご利用時間： ' + times + '</p><p>お支払い金額： ' + charge + '</p>');
                console.log(times);
                console.log(charge);
            }
        }
    }
    );

});


$(function() {
    
    $('[name="hour"]:radio').change( function() {

        var start_day = $('#id_start_day').val();

        var start_time = $('#id_start_time').val();

        $('#hour-box').ready(function(){

            if (start_day != "" && start_time != ""){
                for (var i=0; i<3; i++) {

                    var flag = $('input[name=hour]:eq('+i+')').prop('checked');
                    if (flag===true){
                        console.log(i);
                        if ( i == 0 ){
                            setAfterHourTime(1, start_day, start_time);
                        }else if ( i == 1 ){
                            setAfterHourTime(3, start_day, start_time);
                        }else{
                            setAfterHourTime(6, start_day, start_time);
                        }
                    }
                }
             
            }

        });

    });

});

function setAfterHourTime(time, start_day, start_time) {

    var startdate = new Date(start_day.replace(/-/g,"/") + ' ' + start_time + ':00');
    var addition_time = time * 60 * 60 * 1000;
    var enddate = startdate.getTime() + addition_time;
    enddate = new Date(enddate);
    enddate = getStringFromDate(enddate);
    $('#id_end_day').val(enddate.substring(0,10));
    $('#id_end_time').val(enddate.substring(11,16));

};

function getStringFromDate(date) {

	var year_str = date.getFullYear();
	//月だけ+1すること
	var month_str = 1 + date.getMonth();
	var day_str = date.getDate();
	var hour_str = date.getHours();
	var minute_str = date.getMinutes();
	var second_str = date.getSeconds();

	month_str = ('0' + month_str).slice(-2);
	day_str = ('0' + day_str).slice(-2);
	hour_str = ('0' + hour_str).slice(-2);
	minute_str = ('0' + minute_str).slice(-2);
	second_str = ('0' + second_str).slice(-2);

	format_str = 'YYYY-MM-DD hh:mm:ss';
	format_str = format_str.replace(/YYYY/g, year_str);
	format_str = format_str.replace(/MM/g, month_str);
	format_str = format_str.replace(/DD/g, day_str);
	format_str = format_str.replace(/hh/g, hour_str);
	format_str = format_str.replace(/mm/g, minute_str);
	format_str = format_str.replace(/ss/g, second_str);

	return format_str;
};

