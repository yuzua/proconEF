const changeCategory = (select) => {
    // 子カテゴリの選択欄を空にする。
    categoryElement.children().remove();

    // 選択した親カテゴリに紐づく子カテゴリの一覧を取得する。
    const parentId = parentCategoryElement.val();
    const categoryList = categories[parentId];

    // 子カテゴリの選択肢を作成・追加。
    for (const category of categoryList) {
        const option = $('<option>');
        option.val(category['pk']);
        option.text(category['name']);
        categoryElement.append(option);
    }

    // 指定があれば、そのカテゴリを選択する
    if (select !== undefined) {
        categoryElement.val(select);
    }
};


$('#id_parent_category').on('change', () => {
    changeCategory();
});


// 入力値に問題があって再表示された場合、ページ表示時点で小カテゴリが絞り込まれるようにする
if (parentCategoryElement.val()) {
    const selectedCategory = categoryElement.val();
    changeCategory(selectedCategory);
}



$(function() {
//セレクトボックスが切り替わったら発動
$('#id_category').change(function() {

//子要素の削除
let element = document.getElementById('parent-div');   
var clone = element.cloneNode( false ); //複製
element.parentNode.replaceChild( clone , element ); //全替え

var data = jsonData;
//選択したvalue値を変数に格納
var val = $(this).val();
console.log(data[val])
data = data[val]
for(key in data){
    items = data[key]
    console.log(items)

    var eleTabTr = document.createElement("tr");// tr要素作成
    eleTabTr.setAttribute("id","child-tr1"); // tr要素にidを設定
    var parentDiv = document.getElementById("parent-div");
    parentDiv.insertBefore(eleTabTr, parentDiv.firstChild);
    // ----------------------------
    // 追加する要素を作成します
    // ----------------------------

    // ID
    var newElementId = document.createElement("td"); // td要素作成
    var newContent = document.createTextNode(items.id); // テキストノードを作成
    newElementId.appendChild(newContent); // td要素にテキストノードを追加
    newElementId.setAttribute("id","child-td1"); // td要素にidを設定
    newElementId.setAttribute("scope","row");
    // 車両（メーカー）
    var newElementCategory = document.createElement("td"); // td要素作成
    var newContent = document.createTextNode(items.category__category+"（"+items.parent_category__parent_category+"）"); // テキストノードを作成
    newElementCategory.appendChild(newContent); // td要素にテキストノードを追加
    newElementCategory.setAttribute("id","child-td2"); // td要素にidを設定
    newElementCategory.setAttribute("scope","row");
    // 型番
    var newElementModelId = document.createElement("td"); // td要素作成
    var newContent = document.createTextNode(items.model_id); // テキストノードを作成
    newElementModelId.appendChild(newContent); // td要素にテキストノードを追加
    newElementModelId.setAttribute("id","child-td3"); // td要素にidを設定
    newElementModelId.setAttribute("scope","row");
    // 乗車人数
    var newElementPeople = document.createElement("td"); // td要素作成
    var newContent = document.createTextNode(items.people); // テキストノードを作成
    newElementPeople.appendChild(newContent); // td要素にテキストノードを追加
    newElementPeople.setAttribute("id","child-td4"); // td要素にidを設定
    newElementPeople.setAttribute("scope","row");
    // 乗車人数
    var newElementUsedYears = document.createElement("td"); // td要素作成
    var newContent = document.createTextNode(items.used_years); // テキストノードを作成
    newElementUsedYears.appendChild(newContent); // td要素にテキストノードを追加
    newElementUsedYears.setAttribute("id","child-td5"); // td要素にidを設定
    newElementUsedYears.setAttribute("scope","row");
    // リンク
    var newElementLink = document.createElement("td"); // td要素作成
    newElementLink.setAttribute("id","child-td6"); // td要素にidを設定
    newElementLink.setAttribute("scope","row");

    // ----------------------------
    // 親要素の最初の子要素を追加します
    // ----------------------------
    // 親要素（div）への参照を取得
    var parentDiv = document.getElementById("child-tr1");

    // 追加
    parentDiv.insertBefore(newElementLink, parentDiv.firstChild);
    parentDiv.insertBefore(newElementUsedYears, parentDiv.firstChild);
    parentDiv.insertBefore(newElementPeople, parentDiv.firstChild);
    parentDiv.insertBefore(newElementModelId, parentDiv.firstChild);
    parentDiv.insertBefore(newElementCategory, parentDiv.firstChild);
    parentDiv.insertBefore(newElementId, parentDiv.firstChild);

    var newElementLink = document.createElement("a"); // td要素作成
    var newContent = document.createTextNode('予約する'); // テキストノードを作成
    newElementLink.appendChild(newContent); // td要素にテキストノードを追加
    newElementLink.setAttribute("href","/carsharing_booking/car/"+items.id);
    var parentDivLink = document.getElementById("child-td6");
    parentDivLink.insertBefore(newElementLink, parentDivLink.firstChild);
    
    // 選択したvalue値をp要素に出力
    // $('#id_child-td1').text(items.parent_category__parent_category);
}
});
});
