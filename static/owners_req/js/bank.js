// 三井住友銀行
document.getElementById("0009").onclick = function() {
	document.getElementById( "id_bank_code" ).value = "0009" ;
	document.getElementById("branch_code_l").innerHTML = "<label id=branch_code_l for=id_bank_account_number>支店コード:</label>";
	document.getElementById("bank_account_number_l").innerHTML = "<label id=bank_account_number_l for=id_bank_account_number>口座番号:</label>";
};
// 三菱ＵＦＪ銀行
document.getElementById("0005").onclick = function() {
	document.getElementById( "id_bank_code" ).value = "0005" ;
	document.getElementById("branch_code_l").innerHTML = "<label id=branch_code_l for=id_bank_account_number>支店コード:</label>";
	document.getElementById("bank_account_number_l").innerHTML = "<label id=bank_account_number_l for=id_bank_account_number>口座番号:</label>";
};
// みずほ銀行
document.getElementById("0001").onclick = function() {
	document.getElementById( "id_bank_code" ).value = "0001" ;
	document.getElementById("branch_code_l").innerHTML = "<label id=branch_code_l for=id_bank_account_number>支店コード:</label>";
	document.getElementById("bank_account_number_l").innerHTML = "<label id=bank_account_number_l for=id_bank_account_number>口座番号:</label>";
};
// ゆうちょ銀行
document.getElementById("9900").onclick = function() {
	document.getElementById( "id_bank_code" ).value = "9900" ;
	document.getElementById("branch_code_l").innerHTML = "<label id=branch_code_l for=id_bank_account_number>記号:</label>";
	document.getElementById("bank_account_number_l").innerHTML = "<label id=bank_account_number_l for=id_bank_account_number>番号:</label>";
};