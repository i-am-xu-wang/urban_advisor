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
    remain_money: List[int]


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
    proximity: str


@dataclass
class ChildCareResult:
    daycare_cost: float
    private_school_cost: float
    total: float


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
    # todo:add remain_money (per month) into the comparison list
    # for the lower than the average salary, store negative percentage number, for the higher than the average salary
    # store positive percentage number

    salary_comparison = []
    remain_money = [1, 2, 3]
    for i, city in enumerate(selected_cities):
        salary_comparison.append(((int(salary) - int(getattr(Expense.objects.get(id=67), city))) / int(
            getattr(Expense.objects.get(id=67), city))) * 100)
    return UserInfo(cities, salary, salary_comparison, property_option, crime_rate, healthcare, childcare, food_option,
                    remain_money)


'''def remaining(userInfo: UserInfo,living_expense: CostLivingResult, property_expense: CostPropertyResult,
              child_care_expense: ChildCareResult, salary):
    remaining_money = []
    salary = int(salary)/12
    for i, city in enumerate(selected_cities):
        total = 0
        if userInfo.childcare:
            total += int(child_care_expense[i].total)
        if userInfo.property_option:
            total += (int(property_expense[i].monthly_payment))
        remaining_money.append(salary - (int(living_expense[i].total) + total))
    return 
    '''


# todo: return a list of overall quality_of_life_result
def overall_quality_of_life(userInfo: UserInfo, living_expense: CostLivingResult, property_expense: CostPropertyResult,
                            child_care_expense: ChildCareResult):
    overall_quality_results = []
    for i, city in enumerate(selected_cities):
        count = 1
        total = 0
        if userInfo.property_option:
            count += 1
            total += 100 - (int(property_expense[i].monthly_payment) / int(userInfo.salary)) * 100
        if userInfo.childcare:
            count += 1
            total += (100 - (child_care_expense[i].total / int(userInfo.salary)) * 100)
        if userInfo.healthcare:
            count += 1
            total += int((getattr(Expense.objects.get(id=72), city)))
        if userInfo.crime_rate:
            count += 1
            total += int((getattr(Expense.objects.get(id=70), city))) + int((getattr(Expense.objects.get(id=71), city)))
        if userInfo.food_option:
            count += 1
            total += int((getattr(Expense.objects.get(id=77), city)))

        total += (100 - ((int(living_expense[i].total) / int(userInfo.salary)) * 100))

        overall_quality_results.append(
            OverallQualityResult(
                ((int(living_expense[i].total) + child_care_expense[i].total) / int(userInfo.salary)) * 100,
                (int(property_expense[i].monthly_payment) / int(userInfo.salary)) * 100,
                (getattr(Expense.objects.get(id=72), city)),
                (getattr(Expense.objects.get(id=70), city)),
                (getattr(Expense.objects.get(id=71), city)),
                (getattr(Expense.objects.get(id=77), city)),
                total / count)  # dummy data
        )
    return overall_quality_results


# pass a list of cities and user selections. Calculated each cities' result based selection, return a list of
# results of each city.
def cost_of_living_calculation(household_member, eating_options, inexpensive_restaurant_options,
                               coffee_option, going_out_options, smoking_option, drinking_options, driving_options,
                               driving_distance,
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
    print(driving_options, rideshare_options, public_transit_options, public_transit_members, public_transit_trips)
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
        clothing.append(int(clothing_options) * getattr(Expense.objects.get(id=69), v))
        taxi.append(20 * 2 * int(rideshare_options) * getattr(Expense.objects.get(id=59), v))
        gas.append(
            (int(driving_options) * int(driving_distance) / avg_mpg) * int(getattr(Expense.objects.get(id=61), v)))
        total.append(
            int(food[i]) + int(grocery[i]) + int(entertainment[i]) + float(gym[i]) + int(vacation_spending) / 12.0 + int(
                cigarettes[i]) + float(drinks[i]) + float(public_transport[i]) + clothing[i] + gas[i] + taxi[i])

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
                    CostPropertyResult(rent_or_buy, getattr(Expense.objects.get(id=32), v), property_size, proximity))
            elif proximity == 'City Center' and property_size == 'Two Bedrooms':
                cities_property_expense.append(CostPropertyResult(rent_or_buy, (
                        float(getattr(Expense.objects.get(id=32), v)) + float(getattr(Expense.objects.get(id=34), v)) / 2),
                                                                  property_size, proximity))
            elif proximity == 'City Center' and property_size == 'Three Bedrooms':
                cities_property_expense.append(
                    CostPropertyResult(rent_or_buy, getattr(Expense.objects.get(id=34), v), property_size, proximity))
            elif proximity == 'Suburb' and property_size == 'One Bedroom':
                cities_property_expense.append(
                    CostPropertyResult(rent_or_buy, getattr(Expense.objects.get(id=33), v), property_size, proximity))
            elif proximity == 'Suburb' and property_size == 'Two Bedrooms':
                cities_property_expense.append(CostPropertyResult(rent_or_buy, (
                        float(getattr(Expense.objects.get(id=33), v)) + float(getattr(Expense.objects.get(id=35), v)) / 2),
                                                                  property_size, proximity))
            elif proximity == 'Suburb' and property_size == 'Three Bedrooms':
                cities_property_expense.append(
                    CostPropertyResult(rent_or_buy, getattr(Expense.objects.get(id=35), v), property_size, proximity))
        else:
            r = getattr(Expense.objects.get(id=18), v) / 1200
            n = 20 * 12
            if proximity == 'Suburb':
                down = (float(property_size) * float(getattr(Expense.objects.get(id=37), v))) * float(
                    down_payment_percent) / 100
                p = (float(property_size) * float(getattr(Expense.objects.get(id=37), v))) - down
                m = p * ((r * ((1 + r) ** n)) / ((1 + r) ** n - 1))
                cities_property_expense.append(CostPropertyResult(rent_or_buy, m, property_size, proximity))
            elif proximity == 'City Center':
                down = (float(property_size) * float(getattr(Expense.objects.get(id=37), v))) * float(
                    down_payment_percent) / 100
                p = float(property_size) * float(getattr(Expense.objects.get(id=36), v)) - down
                m = p * ((r * ((1 + r) ** n)) / ((1 + r) ** n - 1))
                cities_property_expense.append(CostPropertyResult(rent_or_buy, m, property_size, proximity))

    return cities_property_expense


# todo: childcare calculation
def cost_of_child_care(daycare_number, private_school_number):
    child_care_city = []
    for city in selected_cities:
        child_care_city.append(ChildCareResult(int(getattr(Expense.objects.get(id=54), city)) * int(daycare_number),
                                               int(getattr(Expense.objects.get(id=55), city)) / 12.0 * int(
                                                   private_school_number),
                                               int(getattr(Expense.objects.get(id=54), city)) * int(daycare_number) +
                                               int(getattr(Expense.objects.get(id=55), city)) / 12.0 * int(
                                                   private_school_number)))
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
            CrimeSafetyResult((getattr(Expense.objects.get(id=39), city)), (getattr(Expense.objects.get(id=40), city)),
                              (getattr(Expense.objects.get(id=41), city)), (getattr(Expense.objects.get(id=42), city)),
                              (getattr(Expense.objects.get(id=43), city)), (getattr(Expense.objects.get(id=44), city)),
                              (getattr(Expense.objects.get(id=45), city)), (getattr(Expense.objects.get(id=46), city)),
                              (getattr(Expense.objects.get(id=47), city)), (getattr(Expense.objects.get(id=48), city)),
                              (getattr(Expense.objects.get(id=49), city)), (getattr(Expense.objects.get(id=50), city)),
                              (getattr(Expense.objects.get(id=51), city)), (getattr(Expense.objects.get(id=52), city)),
                              (getattr(Expense.objects.get(id=53), city)))
        )
    return crime_city


# todo: this function purely fetch data from DB, not using data pass from frontend.
def food_option_calculation():
    food_city = []
    for city in selected_cities:
        food_city.append(
            FoodResult((getattr(Expense.objects.get(id=73), city)), (getattr(Expense.objects.get(id=74), city)),
                       (getattr(Expense.objects.get(id=75), city)), (getattr(Expense.objects.get(id=76), city)),
                       (getattr(Expense.objects.get(id=77), city)))
        )
    return food_city


def get_selected_city_salary():
    salaries = []
    for city in selected_cities:
        salaries.append(getattr(Expense.objects.get(id=67), city))
    return salaries


def get_salary_labels():
    salary_labels = ["Your Average Salary"]
    for city in selected_cities:
        salary_labels.append(city)
    return salary_labels


def add_index_data(overall_quality: List[OverallQualityResult]):
    data = []
    for overall_quality_per_city in overall_quality:
        data_per_city = [overall_quality_per_city.cost_of_living_ratio]
        if overall_quality_per_city.housing_expense_ratio != -1:
            data_per_city.append(overall_quality_per_city.housing_expense_ratio)
        if overall_quality_per_city.health_care_ratio != -1:
            data_per_city.append(overall_quality_per_city.health_care_ratio)
        if overall_quality_per_city.crime_index != -1:
            data_per_city.append(overall_quality_per_city.crime_index)
            data_per_city.append(overall_quality_per_city.safety_index)
        if overall_quality_per_city.food_option != 1:
            data_per_city.append(overall_quality_per_city.food_option)
        if len(data_per_city) > 1:
            data_per_city.append(overall_quality_per_city.overall_index)
        data.append(data_per_city)
    return data
