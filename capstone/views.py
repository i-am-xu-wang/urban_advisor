from django.shortcuts import render, redirect
from . import models, calculator


# Create your views here.


def index_page(request):
    return render(request, "capstone/questionnaire.html", )


def register_form(request):
    # TODO: change 'end city' to city list selected from checkboxes. pass city_list to output page
    # TODO: pass checkbox_selections and additional property questions to calculator
    end_city = request.POST["moving-to"]
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

    living_expense = calculator.cost_of_living_calculation(
        end_city,
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

    # TODO: pass to backend "city_list": city_list, "checkbox_selections": checkbox_selections
    return render(request, "capstone/report.html", {"living_expense": living_expense})
