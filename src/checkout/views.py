from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse

import datetime

# Create your views here.
class CheckoutTestView(View):

	def post(self,request, *args, **kwargs):


		if request.is_ajax():
			data ={
				"works":True,
				"time": datetime.datetime.now(),

			}
			return JsonResponse(data)


		return HttpResponse("Hello There")

	def get(self,request,*args,**kwargs):
		template = "checkout/test.html"
		context ={}
		return render(request,template,context)

