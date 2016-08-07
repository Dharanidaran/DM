from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse



# Create your models here.


from products.models import Product

class Tag(models.Model):
	title = models.CharField(max_length=120, unique = True)
	slug = models.SlugField(unique=True)
	products = models.ManyToManyField(Product,blank=True)
	active = models.BooleanField(default=True)
	


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		view_name = "tags:detail"
		return reverse(view_name,kwargs={"slug":self.slug})


 
def tag_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance)
		
pre_save.connect(tag_pre_save_receiver, sender=Tag)

