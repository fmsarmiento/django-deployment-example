from django import template

register = template.Library()

def cutMeUp(value, arg):
    return value.replace(arg,'')

register.filter('cutMeUp',cutMeUp)