function displayswitch() {
    var radio = document.getElementsByName("accessible-radio");
    const div1 = document.getElementById("div1");
    const div2 = document.getElementById("div2");
    for(var i = 0; i < radio.length; i++){
      if(radio[0].checked) {
        div1.style.display ="block";
        div2.style.display ="none";
      }else if(radio[1].checked){
        div1.style.display ="none";
        div2.style.display ="block";
      }else{
        div1.style.display ="block";
        div2.style.display ="block";
      }
    }
  }
  window.onload = function() {
    displayswitch();
  };