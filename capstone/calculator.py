# major calculations perform here
from dataclasses import dataclass
from typing import List

from capstone.models import Expense


@dataclass
class UserInfo:
    cities: List[str]
    salary: int
    salary_comparison: List[int]
    property_option: bool
    crime_rate: bool
    healthcare: bool
    childcare: bool
    food_option: bool


@dataclass
class OverallQualityResult:
    cost_of_living_ratio: float
    housing_expense_ratio: float
    health_care_ratio: float
    crime_index: float
    safety_index: float
    food_option: float
    overall_index: float


@dataclass
class CostLivingResult:
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
    rent_or_buy: str
    monthly_payment: float
    property_size: str


@dataclass
class ChildCareResult:
    daycare_cost: float
    private_school_cost: float


@dataclass
class HealthCareResult:
    skill: float
    speed: float
    equipment: float
    accuracy: float
    friendliness: float
    satisfaction_responsiveness: float
    satisfaction_cost: float
    location: float
    doctor_visit: float
    dentist_visit: float
    optometrist_visit: float
    RX_drug: float
    veterinary_visit: float


@dataclass
class CrimeSafetyResult:
    crime_level: float
    crime_increasing: float
    home_broken: float
    mugged_or_robbed: float
    car_stolen: float
    things_from_car: float
    worries_attack: float
    worries_insult: float
    worries_racist: float
    problem_drugs: float
    property_crime: float
    violent_crime: float
    corruption: float
    safety_day: float
    safety_night: float


@dataclass
class FoodResult:
    restaurant_mile: float
    diversity_score: float
    cuisine_per_metro: float
    dine_out_money: float
    final_index: float


selected_cities = []


def register_user(cities, salary, feature_options: List[str]):
    selected_cities.clear()
    for city in cities:
        selected_cities.append(city)
    property_option = 'property' in feature_options
    crime_rate = 'crime-rate' in feature_options
    healthcare = 'healthcare' in feature_options
    childcare = 'childcare' in feature_options
    food_option = 'food' in feature_options
    # todo:add salary comparison of each city into the comparison list
    # for the lower than the average salary, store negative percentage number, for the higher than the average salary
    # store positive percentage number
    salary_comparison = [40, -50, 60]  # dummy data
    return UserInfo(cities, salary, salary_comparison, property_option, crime_rate, healthcare, childcare, food_option)


# todo: return a list of overall quality_of_life_result
def overall_quality_of_life(userInfo: UserInfo, living_expense: CostLivingResult, property_expense: CostPropertyResult):
    overall_quality_results = []
    for city in selected_cities:
        overall_quality_results.append(
            OverallQualityResult(40, 30, 20, 10, 11, 12, 82)  # dummy data
        )
    return overall_quality_results


# pass a list of cities and user selections. Calculated each cities' result based selection, return a list of
# results of each city.
def cost_of_living_calculation(household_member, eating_options, inexpensive_restaurant_options,
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
    for i, v in enumerate(selected_cities):
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
    for i in range(len(selected_cities)):
        cost_of_living_result.append(
            CostLivingResult(food[i], grocery[i], public_transport[i], taxi[i], gas[i], gym[i],
                             entertainment[i],
                             int(vacation_spending) / 12.0, clothing[i], cigarettes[i], drinks[i], total[i]))
    return cost_of_living_result


def cost_of_property_calculation(proximity, rent_or_buy, property_size, down_payment_percent):
    cities_property_expense = []
    for i, v in enumerate(selected_cities):
        if rent_or_buy == "Rent":
            if proximity == 'City Center' and property_size == 'One Bedroom':
                cities_property_expense.append(
                    CostPropertyResult(rent_or_buy, getattr(Expense.objects.get(id=32), v), property_size))
            elif proximity == 'City Center' and property_size == 'Two Bedrooms':
                cities_property_expense.append(CostPropertyResult(rent_or_buy, (
                        int(getattr(Expense.objects.get(id=32), v)) + int(getattr(Expense.objects.get(id=34), v)) / 2),
                                                                  property_size))
            elif proximity == 'City Center' and property_size == 'Three Bedrooms':
                cities_property_expense.append(
                    CostPropertyResult(rent_or_buy, getattr(Expense.objects.get(id=34), v), property_size))
            elif proximity == 'Suburb' and property_size == 'One Bedroom':
                cities_property_expense.append(
                    CostPropertyResult(rent_or_buy, getattr(Expense.objects.get(id=33), v), property_size))
            elif proximity == 'Suburb' and property_size == 'Two Bedrooms':
                cities_property_expense.append(CostPropertyResult(rent_or_buy, (
                        int(getattr(Expense.objects.get(id=33), v)) + int(getattr(Expense.objects.get(id=35), v)) / 2),
                                                                  property_size))
            elif proximity == 'Suburb' and property_size == 'Three Bedrooms':
                cities_property_expense.append(
                    CostPropertyResult(rent_or_buy, getattr(Expense.objects.get(id=35), v), property_size))
        else:
            r = getattr(Expense.objects.get(id=18), v) / 1200
            n = 20 * 12
            if proximity == 'Suburb':
                down = (int(property_size) * int(getattr(Expense.objects.get(id=37), v))) * int(
                    down_payment_percent) / 100
                p = (int(property_size) * int(getattr(Expense.objects.get(id=37), v))) - down
                m = p * ((r * ((1 + r) ** n)) / ((1 + r) ** n - 1))
                cities_property_expense.append(CostPropertyResult(rent_or_buy, m, property_size))
            elif proximity == 'City Center':
                down = (int(property_size) * int(getattr(Expense.objects.get(id=37), v))) * int(
                    down_payment_percent) / 100
                p = int(property_size) * int(getattr(Expense.objects.get(id=36), v)) - down
                m = p * ((r * ((1 + r) ** n)) / ((1 + r) ** n - 1))
                cities_property_expense.append(CostPropertyResult(rent_or_buy, m, property_size))

    return cities_property_expense


# todo: childcare calculation
def cost_of_child_care(daycare_number, private_school_number):
    child_care_city = []
    for city in selected_cities:
        child_care_city.append(ChildCareResult(1000, 2000))
    return child_care_city


# this function purely fetch data from DB, not using data pass from frontend.
def cost_of_health_calculation():
    health_care_city = []
    for i, v in enumerate(selected_cities):
        health_care_city.append(
            HealthCareResult((getattr(Expense.objects.get(id=19), v)), (getattr(Expense.objects.get(id=20), v)),
                             (getattr(Expense.objects.get(id=21), v)), (getattr(Expense.objects.get(id=22), v)),
                             (getattr(Expense.objects.get(id=23), v)), (getattr(Expense.objects.get(id=24), v)),
                             (getattr(Expense.objects.get(id=25), v)), (getattr(Expense.objects.get(id=26), v)),
                             (getattr(Expense.objects.get(id=27), v)), (getattr(Expense.objects.get(id=28), v)),
                             (getattr(Expense.objects.get(id=29), v)), (getattr(Expense.objects.get(id=30), v)),
                             (getattr(Expense.objects.get(id=31), v))))
    return health_care_city


# todo: this function purely fetch data from DB, not using data pass from frontend.
def cost_of_crime_calculation():
    crime_city = []
    for city in selected_cities:
        crime_city.append(
            CrimeSafetyResult(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
        )
    return crime_city


# todo: this function purely fetch data from DB, not using data pass from frontend.
def food_option_calculation():
    food_city = []
    for city in selected_cities:
        food_city.append(
            FoodResult(1, 2, 3, 4, 5)
        )
    return food_city
