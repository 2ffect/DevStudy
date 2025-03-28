from django.shortcuts import render, redirect
from .models import Restaurant

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants' : restaurants
    }
    return render(request, 'articles/index.html', context)
    
def new(request):
    return render(request, 'articles/new.html')

def create(request):
    restaurant = Restaurant()

    restaurant.name = request.POST.get('title')
    restaurant.description = request.POST.get('description')
    restaurant.address = request.POST.get('address')
    restaurant.phone_number = request.POST.get('phone_number')

    restaurant.save()

    return redirect('restaurants:index')


# name = models.CharField(max_length=100)
# description = models.CharField(max_length=250)
# address = models.TextField()
# phone_number = models.TextField()