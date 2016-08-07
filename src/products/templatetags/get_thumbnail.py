from django import template

register = template.Library()




@register.filter
def get_thumbnail(obj,arg):

	''' obj =  product instance '''

	return obj.thumbnail_set.filter(type=arg).first().media.url

