const csrftoken = getCookie('csrftoken');

$(document).ready(function () {
    //submit questionnaire when clicking submit button
    var household_members = $('#household-options').find(":selected").text().toString();
   // var obj = $('#quiz').serializeJSON();
    console.log(household_members)
    $('#submit-button').click(function () {
        console.log("Submit button clicked!");
        // Using the core $.ajax() method
        $.ajax({
            // The URL for the request
            url: "/",
            // The data to send (will be converted to a query string)
           data: {
                member:household_members
           },
            type: "POST",
            // The type of data we expect back
            dataType: "json",
            headers: {'X-CSRFToken': csrftoken,'x-requested-with':XMLHttpRequest}
        })
            .done(function (json) {
                alert("Receive Ajax request");
               // console.log(JSON.stringify(obj));
            })
            .fail(function (xhr, status, errorThrown) {
                alert("Sorry, there was a problem!");
                console.log("Error: " + errorThrown);
                console.log("Status: " + status);
                console.dir(xhr);
                console.log(JSON.stringify(obj));
            })
            .always(function (xhr, status) {
                alert("The request is complete!");
            });
    });
})

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

