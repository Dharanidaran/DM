
from django.http import Http404
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView


from django.core.urlresolvers import reverse
from digitalmarket.mixins import LoginRequiredMixin,MultiSlugMixin,SubmitBtnMixin
	
from .forms import ProductAddForm, ProductModelForm
from .models import Product
from .mixins import ProductManagerMixin

class ProductCreateView( LoginRequiredMixin, SubmitBtnMixin, CreateView):
	model = Product
	template_name = "form.html"
	form_class = ProductModelForm
	# success_url ="/products/"
	submit_btn = "Add Product"

	def form_valid(self,form):
		user = self.request.user
		form.instance.user = user
		valid_data = super(ProductCreateView,self).form_valid(form)
		# now the instance is saved to the database
		# So we are ready to add the many-to-many field which depends on other models
		form.instance.managers.add(user)
		return valid_data

	def get_success_url(self):
		return reverse("product:list")



# ProductManagerMixin takes care of LoginRequiredMixin	
class ProductUpdateView(ProductManagerMixin, SubmitBtnMixin, MultiSlugMixin, UpdateView):
	model = Product
	template_name = "form.html"
	form_class = ProductModelForm
	#success_url ="/products/"
	submit_btn = "Add Product"




class ProductDetailView(DetailView):
	model = Product


class ProductListView(ListView):
	model = Product 
	def get_queryset(self,*args,**kwargs):
		qs = super(ProductListView,self).get_queryset(**kwargs)
		qs =qs.filter(description__icontains='')
		return qs



def create_view(request): 
	form = ProductModelForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.sale_price = instance.price
		instance.save()
	template = "form.html"
	context = {
			"form": form,
			"submit_btn": "Create Product",
		}
	return render(request, template, context)


def update_view(request, object_id=None):
	product = get_object_or_404(Product, id=object_id)
	form = ProductModelForm(request.POST or None, instance=product)
	if form.is_valid():
		instance = form.save(commit=False)
		#instance.sale_price = instance.price
		instance.save()
	template = "form.html"
	context = {
		"object": product,
		"form": form,
		"submit_btn": "Update Product"
		}
	return render(request, template, context)




def detail_slug_view(request, slug=None):
	product = Product.objects.get(slug=slug)
	try:
		product = get_object_or_404(Product, slug=slug)
	except Product.MultipleObjectsReturned:
		product = Product.objects.filter(slug=slug).order_by("-title").first()

	template = "detail_view.html"
	context = {
		"object": product
		}
	return render(request, template, context)


def detail_view(request, object_id=None):
	product = get_object_or_404(Product, id=object_id)
	template = "detail_view.html"
	context = {
		"object": product
		}
	return render(request, template, context)

	# if object_id is not None:
	# 	product = get_object_or_404(Product, id=object_id)
	# 	# product = Product.objects.get(id=object_id)
	# 	# try:
	# 	# 	product = Product.objects.get(id=object_id)
	# 	# except Product.DoesNotExist:
	# 	# 	product = None

		
	# else:
	# 	raise Http404


def list_view(request):
	# list of items

	queryset = Product.objects.all()
	template = "list_view.html"
	context = {
		"queryset": queryset
	}
	return render(request, template, context)