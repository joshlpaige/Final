from django.shortcuts import render, get_object_or_404, redirect
from .models import SubCat
from cat.models import Cat
from main.models import Main

# Create your views here.

def subcat_list(request):

    if not request.user.is_authenticated:
        return redirect("mylogin")

    subcat = SubCat.objects.all()
    return render(request, 'back/subcat_list.html', {'subcat':subcat})

def subcat_add(request):

    if not request.user.is_authenticated:
        return redirect("mylogin")

    cat = Cat.objects.all()
    
    if request.method == 'POST':

        name = request.POST.get('name')
        catid = request.POST.get('cat')

        if name == "":

            error = "All Fields Required"
            return render(request, 'back/error.html', {'error':error})


        if len(SubCat.objects.filter(name=name)) != 0:

            error = "Category already exists"
            return render(request, 'back/error.html', {'error':error})

        catname = Cat.objects.get(pk=catid).name

        b = SubCat(name=name, catname=catname, catid=catid)
        b.save()
        return redirect('subcat_list')

        
    return render(request, 'back/subcat_add.html', {'cat':cat})