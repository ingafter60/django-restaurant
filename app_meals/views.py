# app_meals/views.py
from django.shortcuts import render
from .models import Meals

def meal_list(request):
    meal_list = Meals.objects.all()

    context = {'meal_list': meal_list}

    return render(request, 'app_meals/meal_list.html', context)

def meal_detail(request, slug): # this slug is from the url
    meal_detail = Meals.objects.get(slug=slug) # these slug are from the model and from ther url

    context = {'meal_detail': meal_detail}

    return render(request, 'app_meals/meal_detail.html', context)
