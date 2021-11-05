# major calculations perform here

class CostLivingResult:
    def __init__(self, city, restaurant, grocery, public_transportation, ride_share, gas, fitness, cinema, vacation,
                 clothing, mortgage, total):
        self.city = city
        self.restaurant = restaurant
        self.grocery = grocery
        self.public_transportation = public_transportation
        self.ride_share = ride_share
        self.gas = gas
        self.fitness = fitness
        self.cinema = cinema
        self.vacation = vacation
        self.clothing = clothing
        self.mortgage = mortgage
        self.total = total


def cost_of_living_calculation(end_city, household_member, eating_options, inexpensive_restaurant_options,
                               coffee_option, going_out_options, smoking_option, drinking_options, driving_options,
                               rideshare_options, public_transit_options, public_transit_members, public_transit_trips,
                               gym_options,
                               vacation_spending, clothing_options):
    food = 18 * int(household_member)
    grocery = 415.8 * int(household_member)
    entertainment = 14 * int(household_member)
    gym = 54.48 * int(gym_options)
    mortgage = 300
    total = food + grocery + entertainment + gym + mortgage + int(vacation_spending)
    print(grocery, entertainment, gym, end_city, household_member, eating_options, inexpensive_restaurant_options,
          coffee_option, going_out_options,
          smoking_option, drinking_options, driving_options, rideshare_options, public_transit_options,
          public_transit_members, public_transit_trips, gym_options, vacation_spending, clothing_options)
    # todo:perform logic calculation for the result

    cost_of_living_result = CostLivingResult('seattle', food, grocery, 300, 400, 500, gym, entertainment,
                                             vacation_spending, clothing_options,
                                             mortgage, total)
    return cost_of_living_result
