//本日、カレンダーの開始日、終了日と、曜日のテキストを用意
var date_now = new Date();
var date_start = new Date(date_now.getFullYear()-1, date_now.getMonth(), 1);
var date_end = new Date(date_now.getFullYear(), date_now.getMonth(), 1);
var days = ["日", "月", "火", "水", "木", "金", "土"];
date_end.setMonth(date_end.getMonth()+12);
 
document.addEventListener("DOMContentLoaded", function() {
 
  //FullCalendarを生成
  var calendar = new FullCalendar.Calendar(document.getElementById("calendar"), {
 
    //プラグインを読み込み
    plugins: ["dayGrid"],
 
    //ヘッダー内の配置を、左に前月ボタン、中央にタイトル、右に次月ボタンに設定
    header: {
      left: "prev",
      center: "title",
      right:" next"
    },
 
    //ボタンのテキスト書き換え
    buttonText: {
      prev: "前の月",
      next: "次の月"
    },
 
    //デフォルト日を本日に設定
    defaultDate: date_now,
 
    //有効期間を1年前の当月1日から12ヶ月後（1年後）に設定
		validRange: {
      start: date_start,
      end: date_end
    },
 
    //イベント情報をパースしたJSONデータから読み込み
		events: events,
    eventTimeFormat: { hour: 'numeric', minute: '2-digit' },
 
    //タイトルを書き換え
    titleFormat: function(obj) {
      return obj.date.year+"年"+(obj.date.month+1)+"月";
    },
 
    //曜日のテキストを書き換え（日〜土）
    columnHeaderText: function(obj) {
      return days[obj.getDay()];
    },
 
    //イベントのクリック時の処理追加（アラート）
    eventClick: function(obj) {
      alert('title:' + obj.event.title + '\nstart_time:' + obj.event.start + '\nend_time:' + obj.event.end);
    }
  });
  calendar.render();
});


console.log(events);