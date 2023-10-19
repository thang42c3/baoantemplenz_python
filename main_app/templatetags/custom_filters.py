from django import template

register = template.Library()

@register.filter
def get_name_for_language(name_of_class, language_code):
    if language_code == 'vi':
        return name_of_class.vn_name
    else:
        return name_of_class.en_name


@register.filter
def get_description_for_language(name_of_class, language_code):
    if language_code == 'vi':
        return name_of_class.vn_description
    else:
        return name_of_class.en_description
