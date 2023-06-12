from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Category, Vehicle
from rest_framework import filters
from django.views.generic import DetailView

# Create your views here.
def base(request):
    categories = Category.objects.all()
    return render(request, 'cars/base.html', {'category': categories})

class VehicleDetailView(DetailView):
    model = Vehicle
    template_name='cars/vehicle_details.html'
    context_object_name='vehicle'

def about(request):
    return render(request, 'cars/about.html')

def categories(request):
    categories = Category.objects.all()
    return render(request, 'cars/categories.html', {'category': categories})

def vehicles(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'cars/vehicles.html', {'vehicle': vehicles})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Vehicle.objects.all()
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'layout.html', 
                {
                    'category':category,
                    'categories':categories, 
                    'vehicles':products
                })