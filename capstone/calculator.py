# major calculations perform here
from dataclasses import dataclass
from typing import List

from capstone.models import Expense


@dataclass
class UserInfo:
    salary: int
    property_option: bool
    crime_rate: bool
    healthcare: bool
    childcare: bool


@dataclass
class CostLivingResult:
    city: str
    restaurant: float
    grocery: float
    public_transportation: float
    ride_share: float
    gas: float
    fitness: float
    cinema: float
    vacation: float
    clothing: float
    smoking: float
    alcohol: float
    total: float


@dataclass
class CostPropertyResult:
    city: str
    rent_or_buy: str
    monthly_payment: float
    property_size: str


@dataclass
class HealthCareResult:
    skill: int
    speed: int
    equipment: int
    accuracy: int
    friendliness: int
    satisfaction_responsiveness: int
    satisfaction_cost: int
    location: int
    doctor_visit: int
    dentist_visit: int
    optometrist_visit: int
    RX_drug: int
    veterinary_visit: int


def register_user(salary, feature_options: List[str]):
    property_option = 'property' in feature_options
    crime_rate = 'crime-rate' in feature_options
    healthcare = 'healthcare' in feature_options
    childcare = 'childcare' in feature_options
    return UserInfo(salary, property_option, crime_rate, healthcare, childcare)


# pass a list of cities and user selections. Calculated each cities' result based selection, return a list of
# results of each city. The function need to add cities into selected_cities for other functions to access it
selected_cities = []


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
    taxi = []
    gas = []
    total = []
    avg_mpg = 25
    mil = 0
    for i, v in enumerate(cities):
        #selected_cities.append(v)
        food.append((int(eating_options) * int(household_member) * getattr(Expense.objects.get(id=1), v)) + (
                int(inexpensive_restaurant_options) * int(household_member) * getattr(Expense.objects.get(id=2),
                                                                                      v)) / 2 + (
                            int(coffee_option) * int(household_member) * getattr(Expense.objects.get(id=6), v)))
        grocery.append(getattr(Expense.objects.get(id=10), v))
        entertainment.append(int(going_out_options) * int(household_member) * getattr(Expense.objects.get(id=16), v))
        gym.append(int(gym_options) * int(household_member) * getattr(Expense.objects.get(id=14), v))
        cigarettes.append(int(smoking_option) * getattr(Expense.objects.get(id=14), v))
        drinks.append(int(drinking_options) * getattr(Expense.objects.get(id=5), v))
        public_transport.append(int(public_transit_members) * getattr(Expense.objects.get(id=57), v) + int(
            public_transit_trips) * 2 * getattr(Expense.objects.get(id=56), v))
        clothing.append(int(clothing_options) * getattr(Expense.objects.get(id=57), v))
        taxi.append(20 * 2 * int(rideshare_options))
        gas.append(int(driving_options) * 2 * mil / avg_mpg * int(getattr(Expense.objects.get(id=61), v)))
        total.append(
            int(food[i]) + int(grocery[i]) + int(entertainment[i]) + int(gym[i]) + int(vacation_spending) / 12.0 + int(
                cigarettes[i]) + int(drinks[i]) + int(public_transport[i]) + clothing[i] + gas[i] + taxi[i])

    cost_of_living_result = []
    for i in range(len(cities)):
        cost_of_living_result.append(
            CostLivingResult(cities[i], food[i], grocery[i], public_transport[i], taxi[i], gas[i], gym[i],
                             entertainment[i],
                             int(vacation_spending) / 12.0, clothing[i], cigarettes[i], drinks[i], total[i]))
    return cost_of_living_result


def cost_of_property_calculation(cities, proximity, rent_or_buy, property_size, down_payment_percent):
    cities_property_expense = []
    for i, v in enumerate(cities):
        if rent_or_buy == "Rent":
            if proximity == 'City Center' and property_size == 'One Bedroom':
                cities_property_expense.append(
                    CostPropertyResult(cities[i], rent_or_buy, getattr(Expense.objects.get(id=32), v), property_size))
            elif proximity == 'City Center' and property_size == 'Two Bedrooms':
                cities_property_expense.append(CostPropertyResult(cities[i], rent_or_buy, (
                        int(getattr(Expense.objects.get(id=32), v)) + int(
                    getattr(Expense.objects.get(id=34), v)) / 2), property_size))
            elif proximity == 'City Center' and property_size == 'Three Bedrooms':
                cities_property_expense.append(
                    CostPropertyResult(cities[i], rent_or_buy, getattr(Expense.objects.get(id=34), v), property_size))
            elif proximity == 'Suburb' and property_size == 'One Bedroom':
                cities_property_expense.append(
                    CostPropertyResult(cities[i], rent_or_buy, getattr(Expense.objects.get(id=33), v), property_size))
            elif proximity == 'Suburb' and property_size == 'Two Bedrooms':
                cities_property_expense.append(CostPropertyResult(cities[i], rent_or_buy, (
                        int(getattr(Expense.objects.get(id=33), v)) + int(
                    getattr(Expense.objects.get(id=35), v)) / 2), property_size))
            elif proximity == 'Suburb' and property_size == 'Three Bedrooms':
                cities_property_expense.append(
                    CostPropertyResult(cities[i], rent_or_buy, getattr(Expense.objects.get(id=35), v), property_size))
        else:
            r = getattr(Expense.objects.get(id=18), v) / 1200
            n = 20 * 12
            if proximity == 'Suburb':
                down = (int(property_size) * int(getattr(Expense.objects.get(id=37), v))) * int(
                    down_payment_percent) / 100
                p = (int(property_size) * int(getattr(Expense.objects.get(id=37), v))) - down
                m = p * ((r * ((1 + r) ** n)) / ((1 + r) ** n - 1))
                cities_property_expense.append(CostPropertyResult(cities[i], rent_or_buy, m, property_size))
            elif proximity == 'City Center':
                down = (int(property_size) * int(getattr(Expense.objects.get(id=37), v))) * int(
                    down_payment_percent) / 100
                p = int(property_size) * int(getattr(Expense.objects.get(id=36), v)) - down
                m = p * ((r * ((1 + r) ** n)) / ((1 + r) ** n - 1))
                cities_property_expense.append(CostPropertyResult(cities[i], rent_or_buy, m, property_size))

    return cities_property_expense


# this function purely fetch data from DB, not using data pass from frontend.
def cost_of_health_calculation(cities):
    health_care_city = []
    for i, v in enumerate(cities):
        health_care_city.append(
            HealthCareResult((getattr(Expense.objects.get(id=19), v)), (getattr(Expense.objects.get(id=20), v)),
                             (getattr(Expense.objects.get(id=21), v)), (getattr(Expense.objects.get(id=22), v)),
                             (getattr(Expense.objects.get(id=23), v)), (getattr(Expense.objects.get(id=24), v)),
                             (getattr(Expense.objects.get(id=25), v)), (getattr(Expense.objects.get(id=26), v)),
                             (getattr(Expense.objects.get(id=27), v)), (getattr(Expense.objects.get(id=28), v)),
                             (getattr(Expense.objects.get(id=29), v)), (getattr(Expense.objects.get(id=30), v)),
                             (getattr(Expense.objects.get(id=31), v))))
    return health_care_city



