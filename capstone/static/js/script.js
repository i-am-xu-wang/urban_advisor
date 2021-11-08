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

    submitForms = function() {
        console.log("submit clicked")
        $(".error-num").removeClass("error-num");
        $(".error-select").removeClass("error-select");

        // cost of living quiz validation
        if ($('input[name="salary"]').val() === "") {
            $('#salary').addClass('error-num');
            return alert("Please enter anticipated annual salary");
        } else if ($('input[name="vacation-spending"]').val() === "") {
            $('#vacation-spending').addClass('error-num');
            return alert("Please enter vacation spending")
        } else {
            // property price quiz validation
            const property_price_checkbox = document.getElementById('property-price-checkbox');
            if ($(property_price_checkbox).is(":checked")) {
                if ($('input[name="city-proximity-options"]:checked').val() === undefined) {
                    $('#city-proximity-options').addClass('error-select');
                    return alert("Please select an option for city proximity");
                } else if ($('input[name="rent-or-buy-options"]:checked').val() === undefined) {
                    $('#rent-or-buy-options').addClass('error-select');
                    return alert("Please select an option for rent or buy");
                } else {
                    if ($('input[name="rent-or-buy-options"]:checked').val() === "Rent") {
                        if ($('input[name="rental-bedroom-options"]:checked').val() === undefined) {
                            $('#rent-questions').addClass('error-select');
                            return alert("Please select an option for rental bedrooms");
                        }
                    } else {
                        if ($('input[name="buy-square-footage"]').val() === "") {
                            $('#buy-square-footage').addClass('error-num');
                            return alert("Please enter desired square footage")
                        }
                    }
                }
                console.log("passed the checks!")
                document.getElementById('property-price-quiz').submit();
                console.log("submitted property price quiz")
            }
            document.getElementById('cost-of-living-quiz').submit();
            console.log("submitted cost of living quiz")
        }
        console.log("done executing submitForms")
    }
})