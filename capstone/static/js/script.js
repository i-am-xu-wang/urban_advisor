$(document).ready(function () {
    const driveDistance = document.getElementById('when-driving')

    const monthlyOptions = document.getElementById('when-public-monthly');
    const onDemandOptions = document.getElementById('when-public-on-demand');

    const propertyPriceOptions = document.getElementById('property-price-options');
    const rentQuestions = document.getElementById('rent-questions')
    const buyQuestions = document.getElementById('buy-questions')

    const childcareOptions = document.getElementById('childcare-options')

    driveDistance.style.display = 'none';

    monthlyOptions.style.display = 'none';
    onDemandOptions.style.display = 'none';

    propertyPriceOptions.style.display = 'none';
    rentQuestions.style.display = 'none';
    buyQuestions.style.display = 'none';

    childcareOptions.style.display = 'none';

    $('#cities-checkboxes :checkbox').change(function () {
        var $cs = $(this).closest('#cities-checkboxes').find(':checkbox:checked');
        if ($cs.length > 3) {
            this.checked = false;
        }
    });

    $('#driving-options').change(function () {
        if ($('#driving-options').val() === '0') {
            driveDistance.style.display = 'none';
        } else{
            driveDistance.style.display = 'block';
        }
    })

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

    $('#childcare-checkbox').click(function () {
        console.log("clicked it!")
        if ($(this).is(":checked")) {
            console.log("it's checked now!")
            childcareOptions.style.display = 'block'
        } else{
            console.log("it's not checked...")
            childcareOptions.style.display = 'none'
        }
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
            $('#salary').addClass('alert alert-danger');
            valid = false;
            message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                '    <strong>Error!</strong> Please enter anticipated annual salary\n' +
                '</div>')
            $('#submit-button').after(message)
        } else if ($('input[name="vacation-spending"]').val() === "") {
            $('#vacation-spending').addClass('alert alert-danger');
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
                            $('#buy-square-footage').addClass('alert alert-danger');
                            valid = false;
                            message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                                '    <strong>Error!</strong> Please enter desired square footage\n' +
                                '</div>')
                            $('#submit-button').after(message)
                        }
                    }
                }
                console.log("passed the checks!")
                //document.getElementById('property-price-quiz').submit();
                console.log("submitted property price quiz")
            }
            if (valid) {
                document.getElementById('cost-of-living-quiz').submit();
                console.log("submitted cost of living quiz")
            }
        }
        console.log("done executing submitForms")
    }
})