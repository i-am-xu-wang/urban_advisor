from django.db import models


# Create your models here.

class Result:
    def __init__(self, restaurant, grocery, public_transportation, ride_share, gas, fitness, cinema, vacation,
                 clothing, total):
        self.restaurant = restaurant
        self.grocery = grocery
        self.public_transportation = public_transportation
        self.ride_share = ride_share
        self.gas = gas
        self.fitness = fitness
        self.cinema = cinema
        self.vacation = vacation
        self.clothing = clothing
        self.total = total


def cost_of_living_calculation(household_member, eating_options, inexpensive_restaurant_options, coffee_option,
                               going_out_options, smoking_option, drinking_options, driving_options, rideshare_options,
                               public_transit_members, public_transit_trips, gym_options, vacation_spending,
                               clothing_options):
    # todo:perform logic calculation for the result
    result = Result(500, 200, 300, 400, 500, 400, 200, 1000, 121, 232)
    return result
