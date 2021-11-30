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


# register.filter('rating', generate_rating_qualifier)
