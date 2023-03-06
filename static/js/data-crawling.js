var stateText = $(".crawling__state");
var keywordInput = $("#crawling-keyword")
var submitButton = $("#crawling-submit");

$(document).ready(function () {
    stateText.text("");
    enableSubmitButton(isKeywordInputValid(keywordInput.val()));
});

function enableSubmitButton(isEnable) {
    submitButton.prop("disabled", !isEnable);
}

function isKeywordInputValid(value) {
    return value.trim() !== '';
}

keywordInput.on('input', function () {
    const value = $(this).val()
    enableSubmitButton(isKeywordInputValid(value));
});

submitButton.click(async function () {
    submitButton.prop("disabled", true);
    enableSubmitButton(false);

    const formData = $('#crawling-form').serialize();

    const requestProgress = setInterval(() => {
        fetch('/crawling')
            .then(response => response.json())
            .then(data => {
                stateText.text(data.progress);
            });
    }, 1000);


    await $.ajax({
        url: "/crawling",
        type: "POST",
        data: formData,
        success: function (response) {
            console.log(response)
        },
        error: function (xhr) {
            console.log(xhr.statusText);
        }
    }).catch((error) => {
        console.log(error);
    })

    clearInterval(requestProgress);
    enableSubmitButton(true);
});