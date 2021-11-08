// const csrftoken = getCookie('csrftoken');
//
// $(document).ready(function () {
//     //submit questionnaire when clicking submit button
//     var household_members = $('#household-options').find(":selected").text().toString();
//     // var obj = $('#quiz').serializeJSON();
//     console.log(household_members)
//     $('#submit-button').click(function () {
//         console.log("Submit button clicked!");
//         // Using the core $.ajax() method
//         $.ajax({
//             // The URL for the request
//             url: "/",
//             // The data to send (will be converted to a query string)
//             data: {
//                 member: household_members
//             },
//             type: "POST",
//             // The type of data we expect back
//             dataType: "json",
//             headers: {'X-CSRFToken': csrftoken, 'x-requested-with': XMLHttpRequest}
//         })
//             .done(function (json) {
//                 alert("Receive Ajax request");
//                 //console.log(JSON.stringify(obj));
//             })
//             .fail(function (xhr, status, errorThrown) {
//                 alert("Sorry, there was a problem!");
//                 console.log("Error: " + errorThrown);
//                 console.log("Status: " + status);
//                 console.dir(xhr);
//             })
//             // Code to run regardless of success or failure;
//             .always(function (xhr, status) {
//                 alert("The request is complete!");
//             });
//     });
// })
//
// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }

$(document).ready(function () {
    const monthlyOptions = document.getElementById('when-public-monthly');
    const onDemandOptions = document.getElementById('when-public-on-demand');

    const propertyPriceOptions = document.getElementById('property-price-options');
    const rentQuestions = document.getElementById('rent-questions')
    const buyQuestions = document.getElementById('buy-questions')

    monthlyOptions.style.display = 'none';
    onDemandOptions.style.display = 'none';

    propertyPriceOptions.style.display = 'none';
    rentQuestions.style.display = 'none';
    buyQuestions.style.display = 'none';

    $('#cities-checkboxes :checkbox').change(function () {
        var $cs = $(this).closest('#cities-checkboxes').find(':checkbox:checked');
        if ($cs.length > 3) {
            this.checked = false;
        }
    });

    $('#public-monthly').click(function () {
        console.log('monthly display')
        if (onDemandOptions) {
            onDemandOptions.style.display = 'none'
        }
        monthlyOptions.style.display = 'block'
    })
    $('#public-on-demand').click(function () {
        console.log('on demand display')
        if (monthlyOptions) {
            monthlyOptions.style.display = 'none'
        }
        onDemandOptions.style.display = 'block'
    })
    $('#public-no').click(function () {
        console.log('none display')
        if (onDemandOptions) {
            onDemandOptions.style.display = 'none'
        }
        if (monthlyOptions) {
            monthlyOptions.style.display = 'none'
        }
    })

    $('#property-price-checkbox').click(function () {
        console.log("clicked it!")
        if ($(this).is(":checked")) {
            console.log("it's checked now!")
            propertyPriceOptions.style.display = 'block'
        } else{
            console.log("it's not checked...")
            propertyPriceOptions.style.display = 'none'
        }
    })

    $('#rent').click(function () {
        console.log("selected rent!")
        if (buyQuestions) {
            buyQuestions.style.display = 'none'
        }
        rentQuestions.style.display = 'block'
    })
    $('#buy').click(function () {
        console.log("selected buy!")
        if (rentQuestions) {
            rentQuestions.style.display = 'none'
        }
        buyQuestions.style.display = 'block'
    })
})