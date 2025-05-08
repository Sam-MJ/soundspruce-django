from django import template

register = template.Library()

@register.filter(name="concat_prefix_to_id")
def concat_prefix_to_id(prefix, id):
    return prefix + str(id)
