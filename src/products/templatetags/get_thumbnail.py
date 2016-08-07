from django import template

register = template.Library()


from ..models import Product, THUMB_CHOICES



@register.filter
def get_thumbnail(obj,arg):
	arg = arg.lower()
	''' obj =  product instance '''

	if not isinstance(obj, Product):
		raise TypeError ("This is not a valid product model.")

	choices = dict(THUMB_CHOICES)
	print(choices)

	if not choices.get(arg):
		raise TypeError("This is not a valid type for this model")
	return obj.thumbnail_set.filter(type=arg).first().media.url

