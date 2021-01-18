//Element取得

//form
const form = document.getElementById("form");
console.log(form);
//form element
const birthdayYear = document.getElementById("id_birthday_year");
console.log(birthdayYear);
// {% comment %} const email = document.getElementById("email");
// const gender = document.getElementsByName("gender"); {% endcomment %}
//error message
const birthdayYear_error_message = document.getElementById("birthday-year-error-message")
console.log(birthdayYear_error_message);
// {% comment %} const email_error_message = document.getElementById("email-error-message")
// const gender_error_message = document.getElementById("gender-error-message") {% endcomment %}
//button
// {% comment %} const btn = document.getElementById("btn"); {% endcomment %}

//バリデーションパターン
const birthdayYearExp = /^\d{4}$/;
// {% comment %} const emailExp = /^[a-z]+@[a-z]+\.[a-z]+$/; {% endcomment %}

//初期状態設定
// {% comment %} btn.disabled = true; {% endcomment %}

//event

//birthday_year
birthdayYear.addEventListener("keyup", e => {
    if (birthdayYearExp.test(birthdayYear.value)) {
        birthdayYear.setAttribute("class", "success");
        birthdayYear_error_message.style.display = "none";
    } else {
        birthdayYear.setAttribute("class", "error");
        birthdayYear_error_message.style.display = "inline";
    }
        console.log(birthdayYear.getAttribute("class").includes("success"));
        checkSuccess();
})