from django.shortcuts import render
from . import calculator


# Create your views here.
def index_page(request):
    return render(request, "capstone/questionnaire.html", )


def about_us(request):
    return render(request, "capstone/about-us.html")


def methodology_page(request):
    return render(request, "capstone/methodology.html")


def register_form(request):
    # for registering user info
    feature_options = request.POST.getlist('feature-option')
    salary = request.POST.get('salary')
    cities = request.POST.getlist('cities-checkbox')
    user_info = calculator.register_user(cities, salary, feature_options)
    salary_section_list = zip(user_info.cities, user_info.salary_comparison, user_info.remain_money)
    # for cost of living option
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
    if public_transit_options == "No":
        public_transit_members = 0
        public_transit_trips = 0
    elif public_transit_options == "Monthly":
        public_transit_members = request.POST["public-transit-members"]
        public_transit_trips = 0
    else:
        public_transit_members = 0
        public_transit_trips = request.POST["public-transit-trips"]
    gym_options = request.POST["gym-options"]
    vacation_spending = request.POST["vacation-spending"]
    clothing_options = request.POST["clothing-options"]
    living_expense = calculator.cost_of_living_calculation(
        household_member, eating_options, inexpensive_restaurant_options, coffee_option, going_out_options,
        smoking_option, drinking_options, driving_options, rideshare_options, public_transit_options,
        public_transit_members, public_transit_trips, gym_options, vacation_spending, clothing_options,
    )
    # for property option
    proximity = request.POST.get('city-proximity-options')
    rent_or_buy = request.POST.get('rent-or-buy-options')
    if rent_or_buy == "Rent":
        property_size = request.POST.get('rental-bedroom-options')
        down_payment_percent = 0
    else:
        property_size = request.POST.get('buy-square-footage')
        down_payment_percent = request.POST.get('down-payment')
        print(down_payment_percent)
    property_expense = calculator.cost_of_property_calculation(proximity, rent_or_buy, property_size,
                                                               down_payment_percent)

    # for child care questions
    daycare_number = request.POST.get('daycare-numbers')
    private_school_number = request.POST.get('private-school-numbers')
    child_care_expense = calculator.cost_of_child_care(daycare_number, private_school_number)


    # for overall quality of life option
    overall_quality = calculator.overall_quality_of_life(user_info, living_expense, property_expense, child_care_expense)
    # for health care option
    cities_health_care = calculator.cost_of_health_calculation()

    # for crime rate option
    cities_crime_rate = calculator.cost_of_crime_calculation()

    # for food option
    cities_food_option = calculator.food_option_calculation()

    return render(request, "capstone/report.html",
                  {"cities_living_expense": living_expense, "user_info": user_info,
                   "salary_section_list": salary_section_list, "overall_quality": overall_quality,
                   "cities_property_expense": property_expense, "child_care": child_care_expense,
                   "cities_health_care": cities_health_care, "cities_crime_rate": cities_crime_rate,
                   "cities_food_option": cities_food_option})
