from django.shortcuts import render, redirect
from . import models, calculator


# Create your views here.
def index_page(request):
    return render(request, "capstone/questionnaire.html", )


def register_form(request):
    # TODO: change 'end city' to city list selected from checkboxes. pass city_list to output page
    # TODO: pass checkbox_selections and additional property questions to calculator
    feature_options = request.POST.getlist('feature-option')
    salary = request.POST.getlist('salary')
    cities = request.POST.getlist('cities-checkbox')
    household_member = request.POST["household-options"]
    eating_options = request.POST["eating-out-options"]
    inexpensive_restaurant_options = request.POST["inexpensive-restaurant-options"]
    coffee_option = request.POST["coffee-options"]
    going_out_options = request.POST["going-out-options"]
    smoking_option = request.POST["smoking-options"]
    drinking_options = request.POST["drinking-options"]
    driving_options = request.POST["driving-options"]
    rideshare_options = request.POST["rideshare-options"]
    public_transit_options = request.POST["public-transit-options"]
    public_transit_members = request.POST["public-transit-members"]
    public_transit_trips = request.POST["public-transit-trips"]
    gym_options = request.POST["gym-options"]
    vacation_spending = request.POST["vacation-spending"]
    clothing_options = request.POST["clothing-options"]
    user_info = calculator.register_user(salary, feature_options)
    living_expense = calculator.cost_of_living_calculation(
        cities,
        household_member,
        eating_options,
        inexpensive_restaurant_options,
        coffee_option,
        going_out_options,
        smoking_option,
        drinking_options,
        driving_options,
        rideshare_options,
        public_transit_options,
        public_transit_members,
        public_transit_trips,
        gym_options,
        vacation_spending,
        clothing_options,
    )
    proximity = request.POST.get('city-proximity-options')
    # print("register form proximity: " + proximity)
    rent_or_buy = request.POST.get('rent-or-buy-options')
    if rent_or_buy == "Rent":
        property_size = request.POST.get('rental-bedroom-options')
        down_payment_percent = 0
    else:
        property_size = request.POST.get('buy-square-footage')
        down_payment_percent = request.POST.get('down-payment')
        print(down_payment_percent)

    # print("register form property size: " + property_size)
    property_expense = calculator.cost_of_property_calculation(cities, proximity, rent_or_buy, property_size,
                                                               down_payment_percent)
    cities_health_care = calculator.cost_of_health_calculation(cities)
    return render(request, "capstone/report.html", {"cities_living_expense": living_expense, "user_info": user_info,
                                                    "cities_property_expense": property_expense,
                                                    "city1_property": property_expense[0],
                                                    "cities_health_care": cities_health_care})

# def register_property_form(request):
#     proximity = request.POST.get('city-proximity-options')
#     print("register property form proximity: " + proximity)
#     rent_or_buy = request.POST.get('rent-or-buy-options')
#     if rent_or_buy == "Rent":
#         property_size = request.POST["rental-bedroom-options"]
#     else:
#         property_size = request.POST["buy-square-footage"]
#     property_expense = calculator.cost_of_property_calculation(proximity, rent_or_buy, property_size)
#
#     return render(request, "capstone/report.html",
#                   {"cities_property_expense": property_expense, "city1_property": property_expense[0]}
#                   )
