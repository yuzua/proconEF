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
            var answerdate = enddate.getDate() - startdate.getDate();
            var charge = 0;
            var times = '';

            if (answerdate <= 0){

            }else{
                charge = answerdate * 20000;
                times = answerdate.toString() + '日 ';
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