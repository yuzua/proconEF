$('#test li').each(function(index) {
    var index = $(this).index() + 1;
    var outer = $(this).html();
    var text = $(this).text();
    outer = (outer.substr( 0, 86 ));
    if (index == 1){
        console.log($(this).html(outer+'<div>'+text+'<span>未利用に関わらず、月額500円頂戴します。</span></div>'));
    }else if(index == 2){
        console.log($(this).html(outer+'<div>'+text+'<span>未利用に関わらず、月額1,000円頂戴します。</span></div>'));
    }else if(index == 3){
        console.log($(this).html(outer+'<div>'+text+'<span>未利用に関わらず、月額2,000円頂戴します。</span></div>'));
    }else if(index == 4){
        console.log($(this).html(outer+'<div>'+text+'<span>未利用に関わらず、月額500円頂戴します。</span></div>'));
    }

});