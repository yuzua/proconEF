$(function(){
    //スクロールの数値を表示
    $('#scrollArea').scroll(function(){
        $('#out').text('scrollLeft: '+$(this).scrollLeft());
      });
    //ボタンを押すと右に0.3秒かけて500px移動
    $('#right').click(function () {
      $('#scrollArea').animate({
        scrollLeft: $('#scrollArea').scrollLeft() + 500
      }, 300);
      return false;
    });
    //ボタンを押すと左に0.3秒かけて500px移動
    $('#left').click(function () {
      $('#scrollArea').animate({
        scrollLeft: $('#scrollArea').scrollLeft() - 500
      }, 300);
      return false;
    });
  });