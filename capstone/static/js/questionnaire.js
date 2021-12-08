$(document).ready(function () {
    const moneyRegExp = /^[$0-9][$0-9,]+?$/;
    const numberRegExp = /^[0-9,]+$/;
    const percentRegExp = /^([0-9]{1,2}){1}(\.[0-9]{1,2})?$/;

    const maximumThree = document.getElementById('maximum-three');

    const driveDistance = document.getElementById('when-driving');
    const drivingDistance = $('input[name="driving-distance"]');

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

    countHousehold = function () {
        return $('#household-options').find(':checked').val();
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
            onDemandOptions.style.display = 'none';
            if (countHousehold() > 1) {
                monthlyOptions.style.display = 'block';
            } else {
                monthlyOptions.style.display = 'none';
                $('#public-transit-members').val(1);
            }
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

    $('#household-options').change(function () {
        togglePublicTransport();
        var num = countHousehold();
        $('#public-transit-members-3').attr('hidden', num<3);
        $('#public-transit-members-4').attr('hidden', num<4);
        $('#public-transit-members-5').attr('hidden', num<5);
        $('#gym-members-2').attr('hidden', num<2);
        $('#gym-members-3').attr('hidden', num<3);
        $('#gym-members-4').attr('hidden', num<4);
        $('#gym-members-5').attr('hidden', num<5);
    })

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
        } else if (!moneyRegExp.test($('input[name="salary"]').val())) {
            const salaryQuestion = $('#salary-question');
            salaryQuestion.addClass('alert alert-danger');
            valid = false;
            message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                '    <strong>Error!</strong> Please only submit a whole dollar amount for this field.\n' +
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
        } else if (!moneyRegExp.test($('input[name="vacation-spending"]').val())) {
            const vacationSpending = $('#vacation-spending-question');
            vacationSpending.addClass('alert alert-danger');
            valid = false;
            message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                '    <strong>Error!</strong> Please only submit a whole dollar amount for this field.\n' +
                '</div>');
            vacationSpending.before(message);
            errorScroll();
        } else if (!(drivingDistance.val() === "") && !numberRegExp.test(drivingDistance.val())) {
            const whenDriving = $('#when-driving');
            whenDriving.addClass('alert alert-danger');
            valid = false;
            message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                '    <strong>Error!</strong> Please only submit a whole number for this field.\n' +
                '</div>');
            whenDriving.before(message);
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
                        } else if (!numberRegExp.test($('input[name="buy-square-footage"]').val())) {
                            const buySquareFootageQuestion = $('#buy-square-footage-question');
                            buySquareFootageQuestion.addClass('alert alert-danger');
                            valid = false;
                            message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                                '    <strong>Error!</strong> Please only submit a whole number for this field.\n' +
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
                        } else if (!percentRegExp.test($('input[name="down-payment"]').val())) {
                            const downPaymentQuestion = $('#down-payment-question');
                            downPaymentQuestion.addClass('alert alert-danger');
                            valid = false;
                            message = $('<div class="alert alert-danger alert-dismissible fade show">\n' +
                                '    <strong>Error!</strong> Please only submit a percentage between 0-99.99 (maximum two decimal places).\n' +
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
                if (drivingDistance.val() === "") {
                    drivingDistance.val(0);
                }
                // replace all dollar signs or commas allowed in text input
                $('input[name="salary"]').val($('input[name="salary"]').val().replace(/[$,]/g , ""));
                $('input[name="driving-distance"]').val($('input[name="driving-distance"]').val().replaceAll(',', ''));
                $('input[name="vacation-spending"]').val($('input[name="vacation-spending"]').val().replace(/[$,]/g , ""));
                $('input[name="buy-square-footage"]').val($('input[name="buy-square-footage"]').val().replaceAll(',', ''));
                // submit form
                document.getElementById('cost-of-living-quiz').submit();
            }
        }
    }
})