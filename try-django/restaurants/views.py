from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
   
from .models import RestaurantLocation

def restaurant_listview(request,):
	template_name = 'restaurants/restaurants_list.html'
	queryset = RestaurantLocation.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)

class RestaurantListView(ListView):
	
	def get_queryset(self):
		# print(self.kwargs)
		slug = self.kwargs.get("slug")
		if slug:
			queryset = RestaurantLocation.objects.filter(
				Q(category__iexact=slug) |
				Q(category__iexact=slug)
			)
		else:
			queryset = RestaurantLocation.objects.none()

		return queryset

class RestaurantDetailView(DetailView):
	queryset = RestaurantLocation.objects.all()

	def get_context_data(self, *args, **kwargs ):
		print(self.kwargs)
		context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return(context)
# class SearchRestaurantListView(ListView):
# 	template_name = 'restaurants_list.html'




# class AsianFusionRestaurantListView(ListView):
# 	template_name = 'restaurants_list.html'
# 	queryset = RestaurantLocation.objects.filter(category__iexact='asian fusion')



# # Create your views here.
# # function based view

# def home_old(request):
# 	html_var = 'f strings'
# 	html_ = f"""
# 	<!DOCTYPE html>
# 	<html>
# 	<head>
# 		<title>Hello</title>
# 	</head>
# 	<body>
# 	<h1>Hello Nepal</h1>
# 	<p>This is {html_var} coming through.</p>
# 	</body>
# 	</html>
# 	"""

# 	return HttpResponse(html_)
# 	#return render(request, "home.html",{})#response

# def home(request):
# 	num = random.randint(0, 1000000)
# 	some_list = [num, random.randint(0, 100000), random.randint(0,10000)]
# 	context = {
# 		"bool_item": False,
# 		"num": num,
# 		"some_list": some_list
# 	}

# 	return render(request, "home.html", context)#response

# def about(request):
	
# 	context = {
		
# 	}

# 	return render(request, "about.html", context)#response

# def contact(request):
# 	context = {
		
# 	}

# 	return render(request, "contact.html", context)#response



# class HomeView( TemplateView):
# 	template_name = 'home.html'

# 	def get_context_data(self, *args, **kwargs):
# 		context = super(HomeView, self).get_context_data(*args, **kwargs)
# 		num = random.randint(0, 1000000)
# 		some_list = [num, random.randint(0, 100000), random.randint(0,10000)]
# 		condition_bool_item = True
# 		if condition_bool_item:
# 			num = random.randint(0, 10000000)
# 		context = {
# 		"num": num,
# 		"some_list": some_list
# 		}
# 		return context
  
