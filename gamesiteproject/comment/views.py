from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from trending.models import Trending
from django.contrib.auth.models import User, Group, Permission
from manager.models import Manager
import random
import string
import datetime

# Create your views here.

 
def news_cm_add(request,pk) :


    if request.method == 'POST':

        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        
        if len(str(day)) == 1 :
            day = "0" + str(day)
        if len(str(month)) == 1 :
            month = "0" + str(month)

    
        today = str(month) + "/" + str(day) + "/" + str(year)
        time = str(now.hour) + ":" + str(now.minute)

        cm = request.POST.get('msg')

        if request.user.is_authenticated :

            manager = Manager.objects.get(utxt=request.user)

            b = Comment(name=manager.name,email=manager.email,cm=cm,news_id=pk,date=today,time=time)
            b.save()

        else:

            name = request.POST.get('name')
            email = request.POST.get('email')

            b = Comment(name=name,email=email,cm=cm,news_id=pk,date=today,time=time)
            b.save()
            

    newsname = News.objects.get(pk=pk).name

    return redirect('news_detail' , word=newsname)


def comments_list(request):

    
    if not request.user.is_authenticated :
        return redirect('mylogin')
    

    ''' perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        a = News.objects.get(pk=pk).writer
        if str(a) != str(request.user) :
            error = "Access Denied"
            return render(request, 'back/error.html' , {'error':error}) '''
    

    comment = Comment.objects.all()

    return render(request, 'back/comments_list.html', {'comment':comment})



def comments_del(request,pk):
    
    
    if not request.user.is_authenticated :
        return redirect('mylogin')
    

    ''' perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        a = News.objects.get(pk=pk).writer
        if str(a) != str(request.user) :
            error = "Access Denied"
            return render(request, 'back/error.html' , {'error':error}) '''
    

    comment = Comment.objects.filter(pk=pk)
    comment.delete()

    return redirect('comments_list')


def comments_confirm(request,pk):
    
    
    if not request.user.is_authenticated :
        return redirect('mylogin')
    

    ''' perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        a = News.objects.get(pk=pk).writer
        if str(a) != str(request.user) :
            error = "Access Denied"
            return render(request, 'back/error.html' , {'error':error}) '''
    

    comment = Comment.objects.get(pk=pk)
    comment.status = 1
    comment.save()

    return redirect('comments_list')