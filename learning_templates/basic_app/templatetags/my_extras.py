from django import template

register = template.Library()

@register.filter(name='cut')
# value from context_dict
def cut(value,arg):
    # This cuts out all values of "arg" from the string!
    return value.replace(arg,'')

# Need to register this Function
# filter(this is the string of what you wish to call this filter, the actual function you created)

# since we are essentially passing in a function cut into another function called filter, we can use a decorator @
# register.filter('cut',cut)
