from django.shortcuts import render, get_object_or_404, redirect
from .models import Cat
from main.models import Main
from django.http import HttpResponse
import csv

# Create your views here.

def cat_list(request):

    if not request.user.is_authenticated:
        return redirect("mylogin")

    cat = Cat.objects.all()
    return render(request, 'back/cat_list.html', {'cat':cat})

def cat_add(request):

    if not request.user.is_authenticated:
        return redirect("mylogin")
    
    if request.method == 'POST':

        name = request.POST.get('name')

        if name == '':

            error = "All Fields Required"
            return render(request, 'back/error.html', {'error':error})


        if len(Cat.objects.filter(name=name)) != 0:

            error = "Category already exists"
            return render(request, 'back/error.html', {'error':error})

        b = Cat(name=name)
        b.save()
        return redirect('cat_list')
        
    return render(request, 'back/cat_add.html')