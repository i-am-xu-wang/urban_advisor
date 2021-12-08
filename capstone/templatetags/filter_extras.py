from django import template

register = template.Library()


@register.filter(name='rating')
def generate_rating_qualifier(score):
    if 0 <= score < 20:
        return "Very Low"
    elif 20 <= score < 40:
        return "Low"
    elif 40 <= score < 60:
        return "Moderate"
    elif 60 <= score < 80:
        return "High"
    else:
        return "Very High"


@register.filter(name='city_name')
def match_city_name(city):
    if city == "sf":
        return "San Francisco"
    elif city == "dc":
        return "Washington D.C."
    else:
        return city


@register.filter(name='zip')
def zip_lists(a, b, c):
    return zip(a, b, c)


@register.filter(name='salary_percentage')
def salary_percentage_filter(salary_compare):
    if salary_compare > 0:
        return salary_compare
    else:
        return -salary_compare


@register.filter(name='modifier')
def salary_percentage_modifier(salary_compare):
    if salary_compare > 0:
        return "higher"
    else:
        return "lower"


@register.filter(name='remain_salary_number')
def remain_salary_filter(remain_salary):
    if remain_salary > 0:
        return remain_salary
    else:
        return -remain_salary


@register.filter(name='remain_salary_wording')
def salary_remaining_wording(remain_salary):
    if remain_salary > 0:
        return "You can save approximately"
    else:
        return "You may overspend"


@register.filter(name='income_ratio_rating')
def income_ratio_rating(ratio):
    if 0 <= ratio < 15:
        return "Very Low"
    elif 15 <= ratio < 25:
        return "Low"
    elif 25 <= ratio < 35:
        return "Moderate"
    elif 35 <= ratio < 45:
        return "High"
    else:
        return "Very High"


@register.filter(name='housing_ratio_rating')
def housing_ratio_rating(ratio):
    if 0 <= ratio < 5:
        return "Very Low"
    elif 5 <= ratio < 15:
        return "Low"
    elif 15 <= ratio < 30:
        return "Moderate"
    elif 30 <= ratio < 40:
        return "High"
    else:
        return "Very High"
