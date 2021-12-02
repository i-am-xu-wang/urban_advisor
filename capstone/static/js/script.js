$(document).ready(function () {
    const driveDistance = document.getElementById('when-driving')

    const monthlyOptions = document.getElementById('when-public-monthly');
    const onDemandOptions = document.getElementById('when-public-on-demand');

    const propertyPriceOptions = document.getElementById('property-price-options');
    const rentQuestions = document.getElementById('rent-questions')
    const buyQuestions = document.getElementById('buy-questions')

    const childcareOptions = document.getElementById('childcare-options')

    toggleDrivingOptions = function() {
        if ($('#driving-options').val() === '0') {
            driveDistance.style.display = 'none';
        } else{
            driveDistance.style.display = 'block';
        }
    }

    togglePublicTransport = function() {
        if ($('#public-monthly').is(":checked")) {
            monthlyOptions.style.display = 'block';
            onDemandOptions.style.display = 'none';
        } else if ($('#public-on-demand').is(":checked")) {
            monthlyOptions.style.display = 'none';
            onDemandOptions.style.display = 'block';
        } else {
            monthlyOptions.style.display = 'none';
            onDemandOptions.style.display = 'none';
        }
    }

    toggleProperty = function() {
        if ($('#property-price-checkbox').is(":checked")) {
            propertyPriceOptions.style.display = 'block'
        } else{
            propertyPriceOptions.style.display = 'none'
        }
    }

    toggleRentOrBuy = function() {
        if ($('#rent').is(":checked")) {
            rentQuestions.style.display = 'block';
            buyQuestions.style.display = 'none';
        } else if ($('#buy').is(":checked")) {
            rentQuestions.style.display = 'none';
            buyQuestions.style.display = 'block';
        } else {
            rentQuestions.style.display = 'none';
            buyQuestions.style.display = 'none';
        }
    }

    toggleChildcare = function() {
        if ($('#childcare-checkbox').is(":checked")) {
            childcareOptions.style.display = 'block'
        } else{
            childcareOptions.style.display = 'none'
        }
    }

    toggleDrivingOptions();
    togglePublicTransport();
    toggleProperty();
    toggleRentOrBuy();
    toggleChildcare();

    $('#cities-checkboxes :checkbox').change(function () {
        var $cs = $(this).closest('#cities-checkboxes').find(':checkbox:checked');
        if ($cs.length > 3) {
            this.checked = false;
        }
    });

    $('#driving-options').change(function () {
        toggleDrivingOptions();
    })

    $('#public-monthly').click(function () {
        togglePublicTransport();
    })

    $('#public-on-demand').click(function () {
        togglePublicTransport();
    })

    $('#public-no').click(function () {
        togglePublicTransport();
    })

    $('#property-price-checkbox').click(function () {
        toggleProperty();
    })

    $('#rent').click(function () {
        toggleRentOrBuy();
    })

    $('#buy').click(function () {
        toggleRentOrBuy();
    })

    $('#childcare-checkbox').click(function () {
        toggleChildcare();
    })

    submitForms = function() {
        let valid = true;
        console.log("submit clicked")
        $(".alert-danger").removeClass("alert-danger");
        $(".alert").removeClass("alert");
        $(".alert-dismissible").remove();

        // cost of living quiz validation
        cities_checkboxes=document.getElementsByClassName("cities-checkbox");
        var cities_checked = false;

        for (i = 0; i < cities_checkboxes.length; i++) {
            if (cities_checkboxes[i].checked === true) {
                cities_checked = true;
            }
        }

        if (!cities_checked) {
            $('#cities-checkboxes').addClass('alert alert-danger')
            valid = false;
            message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                '    <strong>Error!</strong> Please select at least one city to evaluate\n' +
                '</div>')
            $('#submit-button').after(message)
        } else if ($('input[name="salary"]').val() === "") {
            $('#salary-question').addClass('alert alert-danger');
            valid = false;
            message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                '    <strong>Error!</strong> Please enter anticipated annual salary\n' +
                '</div>')
            $('#submit-button').after(message)
        } else if ($('input[name="vacation-spending"]').val() === "") {
            $('#vacation-spending-question').addClass('alert alert-danger');
            valid = false;
            message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                '    <strong>Error!</strong> Please enter vacation spending\n' +
                '</div>')
            $('#submit-button').after(message)
        } else {
            // property price quiz validation
            const property_price_checkbox = document.getElementById('property-price-checkbox');
            if ($(property_price_checkbox).is(":checked")) {
                if ($('input[name="city-proximity-options"]:checked').val() === undefined) {
                    $('#city-proximity-options').addClass('alert alert-danger');
                    valid = false;
                    message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                        '    <strong>Error!</strong> Please select an option for city proximity\n' +
                        '</div>')
                    $('#submit-button').after(message)
                } else if ($('input[name="rent-or-buy-options"]:checked').val() === undefined) {
                    $('#rent-or-buy-options').addClass('alert alert-danger');
                    valid = false;
                    message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                        '    <strong>Error!</strong> Please select an option for rent or buy\n' +
                        '</div>')
                    $('#submit-button').after(message)
                } else {
                    if ($('input[name="rent-or-buy-options"]:checked').val() === "Rent") {
                        if ($('input[name="rental-bedroom-options"]:checked').val() === undefined) {
                            $('#rent-questions').addClass('alert alert-danger');
                            valid = false;
                            message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                                '    <strong>Error!</strong> Please select an option for rental bedrooms\n' +
                                '</div>')
                            $('#submit-button').after(message)
                        }
                    } else {
                        if ($('input[name="buy-square-footage"]').val() === "") {
                            $('#buy-square-footage-question').addClass('alert alert-danger');
                            valid = false;
                            message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                                '    <strong>Error!</strong> Please enter desired square footage\n' +
                                '</div>')
                            $('#submit-button').after(message)
                        } else if ($('input[name="down-payment"]').val() === "") {
                            $('#down-payment-question').addClass('alert alert-danger');
                            valid = false;
                            message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                                '    <strong>Error!</strong> Please enter desired down payment\n' +
                                '</div>')
                            $('#submit-button').after(message)
                        }
                    }
                }
            }
            if (valid) {
                document.getElementById('cost-of-living-quiz').submit();
                console.log("submitted cost of living quiz")
            }
        }
    }
})