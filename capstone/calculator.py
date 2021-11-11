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


class HealthCareResult:
    def __init__(self, skill, speed, equipment, accuracy, friendliness, satisfaction_responsiveness, satisfaction_cost,
                 location, doctor_visit, dentist_visit, optometrist_visit, RX_drug, veterinary_visit):
        self.skill = skill
        self.speed = speed
        self.equipment = equipment
        self.accuracy = accuracy
        self.friendliness = friendliness
        self.satisfaction_responsiveness = satisfaction_responsiveness
        self.satisfaction_cost = satisfaction_cost
        self.location = location
        self.doctor_visit = doctor_visit
        self.dentist_visit = dentist_visit
        self.optometrist_visit = optometrist_visit
        self.RX_drug = RX_drug
        self.veterinary_visit = veterinary_visit


def register_user(salary, feature_options):
    print("register user feature options: " + feature_options[0])
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


# pass a list of cities and user selections. Calculated each cities' result based selection, return a list of
# results of each city. The function need to add cities into selected_cities for other functions to access it
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
    print("cost of living calculation values " + str(grocery), entertainment, str(gym), cities, household_member, eating_options, inexpensive_restaurant_options,
          coffee_option, going_out_options,
          smoking_option, drinking_options, driving_options, rideshare_options, public_transit_options,
          public_transit_members, public_transit_trips, gym_options, vacation_spending, clothing_options)
    # todo:perform logic calculation for the result
    # this just some dummy data
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


def cost_of_property_calculation(proximity, rent_or_buy, property_size, down_payment_percent):
    # todo: perform property calculation logic here
    print("cost of property calculation property size: " + property_size)
    # dummy data
    cost_property_result1 = CostPropertyResult(selected_cities[0], "Rent", 5000, property_size)
    cost_property_result2 = CostPropertyResult(selected_cities[1], "Rent", 5000, property_size)
    cost_property_result3 = CostPropertyResult(selected_cities[2], "Rent", 5000, property_size)
    cities_property_expense = [cost_property_result1, cost_property_result2, cost_property_result3]
    return cities_property_expense


# this function purely fetch data from DB, not using data pass from frontend.
def cost_of_health_calculation():
    # dummy data
    health_care_city1 = HealthCareResult(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    health_care_city2 = HealthCareResult(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    health_care_city3 = HealthCareResult(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    cities_health_care = [health_care_city1, health_care_city2, health_care_city3]
    return cities_health_care
