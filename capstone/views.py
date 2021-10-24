from django.shortcuts import render, redirect
from . import models


# Create your views here.

def index_page(request):
    return render(request,
                  "capstone/questionnaire.html",
                  )

# def report_page(request, result):
#     return render(request,
#                   "capstone/report.html"
#                   )


def register_form(request):
    end_city = request.POST['moving_to']
    household_member = request.POST['household-options']
    eating_options = request.POST['eating-out-options']
    inexpensive_restaurant_options = request.POST['inexpensive-restaurant-options']
    coffee_option = request.POST['coffee-options']
    going_out_options = request.POST['going-out-options']
    smoking_option = request.POST['smoking-options']
    drinking_options = request.POST['drinking-options']
    driving_options = request.POST['driving-options']
    rideshare_options = request.POST['rideshare-options']
    public_transit_options = request.POST['public-transit-options']
    public_transit_members = request.POST['public-transit-members']
    public_transit_trips = request.POST['public-transit-trips']
    gym_options = request.POST['gym-options']
    vacation_spending = request.POST['vacation-spending']
    clothing_options = request.POST['clothing-options']

    result = models.cost_of_living_calculation(end_city,household_member, eating_options, inexpensive_restaurant_options,
                                               coffee_option,
                                               going_out_options, smoking_option, drinking_options, driving_options,
                                               rideshare_options, public_transit_options, public_transit_members,
                                               public_transit_trips, gym_options, vacation_spending, clothing_options)
    return render(request,
                  "capstone/report.html",
                  {"result": result}
                  )
