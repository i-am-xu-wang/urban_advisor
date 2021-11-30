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
def generate_rating_qualifier(city):
    if city == "sf":
        return "Silicon Valley"
    elif city == "dc":
        return "Washington D.C."
    else:
        return city


@register.filter(name='zip')
def zip_lists(a, b):
    return zip(a, b)


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
