const selectElement = document.querySelector('#id_parking_type');

selectElement.addEventListener('change', (event) => {
    if (event.target.value == '立体駐車場'){
        // 高さ:を入力可能に変更
        document.getElementById("id_height").removeAttribute("readonly","");
        // 土地タイプ:をコンクリートのみに変更
        const id_ground_type =　document.getElementById("id_ground_type")
        while (id_ground_type.firstChild) {
            id_ground_type.removeChild(id_ground_type.firstChild);
        }
        var select = document.getElementById("id_ground_type");
        var option = document.createElement("option");
        option.text = "コンクリート";
        option.value = "コンクリート";
        select.appendChild(option);
    }else{
        // 高さ:を0m、入力不可能に変更
        document.getElementById("id_height").value = "0" ;
        document.getElementById("id_height").setAttribute("readonly","");
        // 土地タイプ:をデフォルトに変更
        var select = document.getElementById("id_ground_type");
        var option = document.createElement("option");
        option.text = "平地";
        option.value = "平地";
        select.appendChild(option);
        var option = document.createElement("option");
        option.text = "砂利";
        option.value = "砂利";
        select.appendChild(option);
        var option = document.createElement("option");
        option.text = "砂地";
        option.value = "砂地";
        select.appendChild(option);
    }
});