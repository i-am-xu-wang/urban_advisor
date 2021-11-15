# major calculations perform here

selected_cities = ["Seattle", "Boston", "Roanoke"]
from capstone.models import Expense


class UserInfo:
    def __init__(self, salary, property_option, crime_rate, healthcare, childcare):
        self.salary = salary
        self.property_option = property_option
        self.crime_rate = crime_rate
        self.healthcare = healthcare
        self.childcare = childcare


class CostLivingResult:
    def __init__(self, city, restaurant, grocery, public_transportation, ride_share, gas, fitness, cinema, vacation,
                 clothing,smoking,alcohol,total):
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
        self.smoking = smoking
        self.alcohol = alcohol
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
                               gym_options, vacation_spending, clothing_options):
    food = []
    grocery = []
    entertainment = []
    gym = []
    cigarettes = []
    drinks = []
    clothing = []
    public_transport = []
    total = []
    # print(Expense.objects.get(id))
    for i, v in enumerate(cities):
        if v == 'Boston':
            v = 'boston'
        elif v == 'Washington D.C.':
            v = 'dc'
        elif v == 'Philadelphia':
            v = 'philly'
        elif v == 'Seattle':
            v = 'seattle'
        elif v == 'Silicon Valley':
            v = 'sf'
        elif v == 'Roanoke':
            v = 'roanoke'

        #getattr(obj, v)
        food.append((int(eating_options)*int(household_member)*getattr(Expense.objects.get(id=1), v)) + (int(inexpensive_restaurant_options)*int(household_member)*getattr(Expense.objects.get(id=2), v))/2 + (int(coffee_option)*int(household_member)*getattr(Expense.objects.get(id=6), v)))
        grocery.append(getattr(Expense.objects.get(id=10),v))
        entertainment.append(int(going_out_options)*int(household_member)*getattr(Expense.objects.get(id=16),v))
        gym.append(int(gym_options)*int(household_member)*getattr(Expense.objects.get(id=14), v))
        cigarettes.append(int(smoking_option)*getattr(Expense.objects.get(id=14), v))
        drinks.append(int(drinking_options)*getattr(Expense.objects.get(id=5), v))
        public_transport.append(int(public_transit_members)*getattr(Expense.objects.get(id=57), v) + int(public_transit_trips)*2*getattr(Expense.objects.get(id=56), v))
        clothing.append(int(clothing_options)*getattr(Expense.objects.get(id=57), v))
        total.append(int(food[i])+int(grocery[i])+int(entertainment[i])+int(gym[i])+int(vacation_spending)+int(cigarettes[i])+int(drinks[i])+public_transport[i]+clothing[i])

    cost_of_living_result = []
    for i in range(len(cities)):
        cost_of_living_result.append(CostLivingResult(cities[i], food[i], grocery[i], public_transport[i], 400, 500, gym[i], entertainment[i],
                                                  vacation_spending, clothing_options,cigarettes[i],drinks[i],total[i]))
    return cost_of_living_result


def cost_of_property_calculation(cities,proximity, rent_or_buy, property_size, down_payment_percent):
    # todo: perform property calculation logic here
    print("cost of property calculation property size: " + property_size)
    print('proximity',proximity)
    print('rent_or_buy',rent_or_buy)
    print('property_size',property_size)
    #print('down_payment_percent',down_payment_percent)
    # dummy data
    cities_property_expense = []
    for i, v in enumerate(cities):
        if v == 'Boston':
            v = 'boston'
        elif v == 'Washington D.C.':
            v = 'dc'
        elif v == 'Philadelphia':
            v = 'philly'
        elif v == 'Seattle':
            v = 'seattle'
        elif v == 'Silicon Valley':
            v = 'sf'
        elif v == 'Roanoke':
            v = 'roanoke'
        cities_property_expense.append(CostPropertyResult(cities[i], rent_or_buy, 5000, property_size))
    #cost_property_result1 = CostPropertyResult(selected_cities[0], ", 5000, property_size)
    #cost_property_result2 = CostPropertyResult(selected_cities[1], "Rent", 5000, property_size)
    #cost_property_result3 = CostPropertyResult(selected_cities[2], "Rent", 5000, property_size)
    #cities_property_expense = [cost_property_result1, cost_property_result2, cost_property_result3]
    return cities_property_expense


# this function purely fetch data from DB, not using data pass from frontend.
def cost_of_health_calculation(cities):
    # dummy data
    health_care_city = []
    for i, v in enumerate(cities):
        if v == 'Boston':
            v = 'boston'
        elif v == 'Washington D.C.':
            v = 'dc'
        elif v == 'Philadelphia':
            v = 'philly'
        elif v == 'Seattle':
            v = 'seattle'
        elif v == 'Silicon Valley':
            v = 'sf'
        elif v == 'Roanoke':
            v = 'roanoke'

        health_care_city.append(HealthCareResult((getattr(Expense.objects.get(id=19),v)), (getattr(Expense.objects.get(id=20),v)), (getattr(Expense.objects.get(id=21),v)), (getattr(Expense.objects.get(id=22),v)), (getattr(Expense.objects.get(id=23),v)), (getattr(Expense.objects.get(id=24),v)), (getattr(Expense.objects.get(id=25),v)), (getattr(Expense.objects.get(id=26),v)), (getattr(Expense.objects.get(id=27),v)), (getattr(Expense.objects.get(id=28),v)), (getattr(Expense.objects.get(id=29),v)), (getattr(Expense.objects.get(id=30),v)), (getattr(Expense.objects.get(id=31),v))))
    #health_care_city2 = HealthCareResult(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    #health_care_city3 = HealthCareResult(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    #cities_health_care = [health_care_city1, health_care_city2, health_care_city3]
    return health_care_city
