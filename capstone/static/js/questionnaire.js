$(document).ready(function () {
    const atLeastOne = document.getElementById('at-least-one');
    const maximumThree = document.getElementById('maximum-three');

    const driveDistance = document.getElementById('when-driving');

    const monthlyOptions = document.getElementById('when-public-monthly');
    const onDemandOptions = document.getElementById('when-public-on-demand');

    const propertyPriceOptions = document.getElementById('property-price-options');
    const rentQuestions = document.getElementById('rent-questions')
    const buyQuestions = document.getElementById('buy-questions')

    const childcareOptions = document.getElementById('childcare-options')

    processCitiesCheckboxes = function () {
        var $cs = $('#cities-checkboxes').find(':checkbox:checked');
        $(maximumThree).removeClass('fw-bold spruce-text');
        if ($cs.length >= 3) {
            $(maximumThree).addClass('fw-bold spruce-text');
        }
        return $cs.length > 3;
    }

    toggleDrivingOptions = function () {
        if ($('#driving-options').val() === '0') {
            driveDistance.style.display = 'none';
        } else {
            driveDistance.style.display = 'block';
        }
    }

    togglePublicTransport = function () {
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

    toggleProperty = function () {
        if ($('#property-price-checkbox').is(":checked")) {
            propertyPriceOptions.style.display = 'block'
        } else {
            propertyPriceOptions.style.display = 'none'
        }
    }

    toggleRentOrBuy = function () {
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

    toggleChildcare = function () {
        if ($('#childcare-checkbox').is(":checked")) {
            childcareOptions.style.display = 'block'
        } else {
            childcareOptions.style.display = 'none'
        }
    }

    removeError = function () {
        $(".alert-danger").removeClass("alert-danger");
        $(".alert").removeClass("alert");
        $(".alert-dismissible").remove();
    }

    errorScroll = function () {
        $([document.documentElement, document.body]).animate({
            scrollTop: $(".alert-dismissible").offset().top
        }, 'fast');
    }

    processCitiesCheckboxes();
    toggleDrivingOptions();
    togglePublicTransport();
    toggleProperty();
    toggleRentOrBuy();
    toggleChildcare();

    $('#cities-checkboxes :checkbox').change(function () {
        if (processCitiesCheckboxes()) {
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
        removeError();
        toggleRentOrBuy();
    })

    $('#buy').click(function () {
        removeError();
        toggleRentOrBuy();
    })

    $('#childcare-checkbox').click(function () {
        toggleChildcare();
    })

    $('#cost-of-living-quiz').on("click", ".alert-danger", function () {
        removeError();
    });

    submitForms = function () {
        // valid will be set to false if form fails any validation check
        let valid = true;

        // reset error messages to perform validation anew
        removeError();

        // cost of living quiz validation
        cities_checkboxes = document.getElementsByClassName("cities-checkbox");
        var cities_checked = false;

        for (i = 0; i < cities_checkboxes.length; i++) {
            if (cities_checkboxes[i].checked === true) {
                cities_checked = true;
            }
        }

        if (!cities_checked) {
            const checkboxes = $('#cities-checkboxes');
            checkboxes.addClass('alert alert-danger');
            valid = false;
            message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                '    <strong>Error!</strong> Please select at least one city to evaluate.\n' +
                '</div>');
            checkboxes.before(message);
            errorScroll();
        } else if ($('input[name="salary"]').val() === "") {
            const salaryQuestion = $('#salary-question');
            salaryQuestion.addClass('alert alert-danger');
            valid = false;
            message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                '    <strong>Error!</strong> Please enter anticipated annual income.\n' +
                '</div>');
            salaryQuestion.before(message);
            errorScroll();
        } else if ($('input[name="vacation-spending"]').val() === "") {
            const vacationSpending = $('#vacation-spending-question');
            vacationSpending.addClass('alert alert-danger');
            valid = false;
            message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                '    <strong>Error!</strong> Please enter vacation spending.\n' +
                '</div>');
            vacationSpending.before(message);
            errorScroll();
        } else {
            // property price quiz validation
            const property_price_checkbox = document.getElementById('property-price-checkbox');
            if ($(property_price_checkbox).is(":checked")) {
                if ($('input[name="city-proximity-options"]:checked').val() === undefined) {
                    const cityProximityOptions = $('#city-proximity-options');
                    cityProximityOptions.addClass('alert alert-danger');
                    valid = false;
                    message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                        '    <strong>Error!</strong> Please select an option for city proximity.\n' +
                        '</div>');
                    cityProximityOptions.before(message);
                    errorScroll();
                } else if ($('input[name="rent-or-buy-options"]:checked').val() === undefined) {
                    const rentOrBuyOptions = $('#rent-or-buy-options');
                    rentOrBuyOptions.addClass('alert alert-danger');
                    valid = false;
                    message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                        '    <strong>Error!</strong> Please select an option for rent or buy.\n' +
                        '</div>');
                    rentOrBuyOptions.before(message);
                    errorScroll();
                } else {
                    if ($('input[name="rent-or-buy-options"]:checked').val() === "Rent") {
                        if ($('input[name="rental-bedroom-options"]:checked').val() === undefined) {
                            const rentQuestions = $('#rent-questions');
                            rentQuestions.addClass('alert alert-danger');
                            valid = false;
                            message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                                '    <strong>Error!</strong> Please select an option for rental bedrooms.\n' +
                                '</div>');
                            rentQuestions.before(message);
                            errorScroll();
                        }
                    } else {
                        if ($('input[name="buy-square-footage"]').val() === "") {
                            const buySquareFootageQuestion = $('#buy-square-footage-question');
                            buySquareFootageQuestion.addClass('alert alert-danger');
                            valid = false;
                            message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                                '    <strong>Error!</strong> Please enter desired square footage.\n' +
                                '</div>');
                            buySquareFootageQuestion.before(message);
                            errorScroll();
                        } else if ($('input[name="down-payment"]').val() === "") {
                            const downPaymentQuestion = $('#down-payment-question');
                            downPaymentQuestion.addClass('alert alert-danger');
                            valid = false;
                            message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                                '    <strong>Error!</strong> Please enter desired down payment.\n' +
                                '</div>');
                            downPaymentQuestion.before(message);
                            errorScroll();
                        }
                    }
                }
            }
            // if we have passed all checks without valid being set to false, we are ready to submit
            if (valid) {
                // accept 0 as a valid driving-distance value if user did not submit their own
                const drivingDistance = $('input[name="driving-distance"]')
                if (drivingDistance.val() === "") {
                    drivingDistance.val(0);
                }
                // submit form
                document.getElementById('cost-of-living-quiz').submit();
            }
        }
    }
})