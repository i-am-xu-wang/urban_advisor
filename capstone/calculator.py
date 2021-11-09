# major calculations perform here

selected_cities = ["Seattle", "Boston", "Roanoke"]


class UserInfo:
    def __init__(self, salary, property_option, crime_rate, healthcare, childcare):
        self.salary = salary
        self.property_option = property_option
        self.crime_rate = crime_rate
        self.healthcare = healthcare
        self.childcare = childcare


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


class CostPropertyResult:
    def __init__(self, city, rent_or_buy, monthly_payment, property_size):
        self.city = city
        self.rent_or_buy = rent_or_buy
        self.monthly_payment = monthly_payment
        self.property_size = property_size


def register_user(salary, feature_options):
    print(feature_options)
    property_option = False
    crime_rate = False
    healthcare = False
    childcare = False
    for option in feature_options:
        if option == 'property':
            property_option = True
        if option == 'crime-rate':
            crime_rate = True
        if option == 'healthcare':
            healthcare = True
        if option == 'childcare':
            childcare = True
    user = UserInfo(salary, property_option, crime_rate, healthcare, childcare)
    return user


def cost_of_living_calculation(cities, household_member, eating_options, inexpensive_restaurant_options,
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
    print(grocery, entertainment, gym, cities, household_member, eating_options, inexpensive_restaurant_options,
          coffee_option, going_out_options,
          smoking_option, drinking_options, driving_options, rideshare_options, public_transit_options,
          public_transit_members, public_transit_trips, gym_options, vacation_spending, clothing_options)
    # todo:perform logic calculation for the result
    # just some dummy data
    cost_of_living_result1 = CostLivingResult(cities[0], food, grocery, 300, 400, 500, gym, entertainment,
                                              vacation_spending, clothing_options,
                                              mortgage, total)
    cost_of_living_result2 = CostLivingResult(cities[1], food, grocery, 300, 400, 500, gym, entertainment,
                                              vacation_spending, clothing_options,
                                              mortgage, total)
    cost_of_living_result3 = CostLivingResult(cities[2], food, grocery, 300, 400, 500, gym, entertainment,
                                              vacation_spending, clothing_options,
                                              mortgage, total)
    cities_living_expense = [cost_of_living_result1, cost_of_living_result2, cost_of_living_result3]
    # return cost_of_living_result
    return cities_living_expense


def cost_of_property_calculation(proximity, rent_or_buy, property_size):
    # todo: perform property calculation logic here

    # dummy data
    cost_property_result1 = CostPropertyResult(selected_cities[0], "Rent", 500, property_size)
    cost_property_result2 = CostPropertyResult(selected_cities[1], "Rent", 500, property_size)
    cost_property_result3 = CostPropertyResult(selected_cities[2], "Rent", 500, property_size)
    cities_property_expense = [cost_property_result1, cost_property_result2, cost_property_result3]
    return cities_property_expense
