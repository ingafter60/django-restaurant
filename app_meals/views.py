# app_meals/views.py
from django.shortcuts import render
from .models import Meals

def meal_list(request):
    meal_list = Meals.objects.all()
    context = {'meal_list': meal_list}

    return render(request, 'app_meals/meal_list.html', context)

def meal_detail(request, slug):
    pass
