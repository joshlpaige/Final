from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from contactform.models import ContactForm
from trending.models import Trending
import random
from random import randint
import string
from django.contrib.auth.models import User, Permission, Group
from manager.models import Manager
from comment.models import Comment







# Create your views here.

def home(request):

    site = Main.objects.get(pk=1)
    news = News.objects.all().order_by('-pk')
    news1 = News.objects.all().order_by('-pk')[:4]
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    lastnews2 = News.objects.all().order_by('-pk')[:1]
    popnews = News.objects.all().order_by('-show')[:4]
    popnews2 = News.objects.all().order_by('-show')[:2]
    trending = Trending.objects.all().order_by('-pk')[:5]

    


    

    return render(request, 'front/home.html', {'site':site, 'news':news, 'cat':cat, 'subcat':subcat, 'lastnews':lastnews, 'popnews':popnews, 'popnews2':popnews2, 'trending':trending, 'lastnews2':lastnews2})

def about(request):

    site = Main.objects.get(pk=1)
    news = News.objects.all().order_by('-pk')
    news1= News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    lastnews1 = News.objects.all().order_by('-pk')[:1]
    popnews = News.objects.all().order_by('-show')[:4]
    popnews2 = News.objects.all().order_by('-show')[:2]
    popnews3 = News.objects.all().order_by('-show')[:2]
    trending = Trending.objects.all().order_by('-pk')[:5]

    return render(request, 'front/about.html', {'site':site, 'news':news, 'news1':news1, 'cat':cat, 'subcat':subcat, 'lastnews':lastnews, 'lastnews1':lastnews1,'popnews':popnews, 'popnews2':popnews2, 'popnews3':popnews3, 'trending':trending})

def panel(request):

    if not request.user.is_authenticated:
        return redirect("mylogin")

    perm = 0
    perms = Permission.objects.filter(user=request.user)
    for i in perms :
        if i.codename == "master_user" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html', {'error':error})     

    return render(request, 'back/home.html')

def mylogin(request):

    if request.method == 'POST':

        utxt = request.POST.get('username')
        ptxt = request.POST.get('password')

        if utxt != '' and ptxt != '':
            
            user = authenticate(username=utxt, password=ptxt)

            if user != None:

                login(request, user)
                return redirect('panel')
    
    return render(request, 'front/login.html')

def mylogout(request):
    
    logout(request)

    return redirect('mylogin')

def site_setting(request):

    if not request.user.is_authenticated:
        return redirect("mylogin")

    

    if request.method == "POST":

        name = request.POST.get('name')
        txt = request.POST.get('txt')
        facebook = request.POST.get('facebook')
        twitter = request.POST.get('twitter')
        steam = request.POST.get('steam')
        instagram = request.POST.get('instagram')
        youtube = request.POST.get('youtube')
        git = request.POST.get('git')
        linkedin = request.POST.get('linkedin')

        if facebook == '' : facebook = '#'
        if twitter == '' : twitter = '#'
        if steam == '' : steam = '#'
        if instagram == '' : instagram = '#'
        if youtube == '' : youtube = '#'
        if git == '' : git = '#'
        if linkedin == '' : git = '#'

        if name == '' or txt == '':
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error':error})
        
        try : 

            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            picurl = url
            picname = filename


        except:

            picurl = '-'
            picname = '-'

        
        try : 

            myfile2 = request.FILES['myfile2']
            fs2 = FileSystemStorage()
            filename2 = fs2.save(myfile2.name, myfile2)
            url2 = fs2.url(filename2)

            picurl2 = url2
            picname2 = filename2


        except:

            picurl2 = '-'
            picname2 = '-'

        b = Main.objects.get(pk=1)
        b.name = name
        b.facebook = facebook
        b.twitter = twitter
        b.steam = steam
        b.instagram = instagram
        b.youtube = youtube
        b.git = git
        b.linkedin = linkedin
        b.about = txt

        if picurl != "-" : b.picurl = picurl
        if picname != "-" : b.picname = picname
        if picurl2 != "-" :  b.picurl2 = picurl2
        if picname2 != "-" : b.picname2 = picname2
        
        b.save()
            

        


            
    site = Main.objects.get(pk=1)
    return render(request, 'back/setting.html', {'site':site})

def about_setting(request):

    if not request.user.is_authenticated :
        return redirect('mylogin')

    if request.method == "POST":
        
        txt = request.POST.get('txt')

        if txt == "":
            error = "All Fields Requirded"
            return render(request, 'back/error.html' , {'error':error})
        
        b = Main.objects.get(pk=1)
        b.abouttxt = txt
        b.save() 

    about = Main.objects.get(pk=1).abouttxt


    return render(request, 'back/about_setting.html', {'about':about})

def contact(request):

    site = Main.objects.get(pk=1)
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    popnews = News.objects.all().order_by('-show')
    popnews2 = News.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]
    

    return render(request, 'front/contact.html' , {'site':site, 'news':news, 'cat':cat, 'subcat':subcat, 'lastnews':lastnews, 'popnews':popnews, 'popnews2':popnews2, 'trending':trending})


def msgbox(request):
    
    site = Main.objects.get(pk=1)
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    popnews = News.objects.all().order_by('-show')
    popnews2 = News.objects.all().order_by('-show')[:3]
    

    return render(request, 'front/contact/submit.html' , {'site':site, 'news':news, 'cat':cat, 'subcat':subcat, 'lastnews':lastnews, 'popnews':popnews, 'popnews2':popnews2})

def hacker(request):

    site = Main.objects.get(pk=1)
    news = News.objects.all().order_by('-pk')
    news1 = News.objects.all().order_by('-pk')[:4]
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    lastnews2 = News.objects.all().order_by('-pk')[:1]
    popnews = News.objects.all().order_by('-show')[:4]
    popnews2 = News.objects.all().order_by('-show')[:2]
    trending = Trending.objects.all().order_by('-pk')[:5]


    

    return render(request, 'front/hacker.html', {'site':site, 'news':news, 'cat':cat, 'subcat':subcat, 'lastnews':lastnews, 'popnews':popnews, 'popnews2':popnews2, 'trending':trending, 'lastnews2':lastnews2,})

def slay(request):

    site = Main.objects.get(pk=1)
    news = News.objects.all().order_by('-pk')
    news1 = News.objects.all().order_by('-pk')[:4]
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    lastnews2 = News.objects.all().order_by('-pk')[:1]
    popnews = News.objects.all().order_by('-show')[:4]
    popnews2 = News.objects.all().order_by('-show')[:2]
    trending = Trending.objects.all().order_by('-pk')[:5]
    


    

    return render(request, 'front/slay.html', {'site':site, 'news':news, 'cat':cat, 'subcat':subcat, 'lastnews':lastnews, 'popnews':popnews, 'popnews2':popnews2, 'trending':trending, 'lastnews2':lastnews2,})

def playground(request):

    site = Main.objects.get(pk=1)

    return render(request, 'front/playground.html', {'site':site})



def change_pass(request):
    
    if not request.user.is_authenticated :
        return redirect('mylogin')

    if request.method == 'POST' :

        oldpass = request.POST.get('oldpass')
        newpass = request.POST.get('newpass')

        if oldpass == "" or newpass == "" :
            error = "All Fields Requirded"
            return render(request, 'back/error.html' , {'error':error})

        user = authenticate(username=request.user, password=oldpass)

        if user != None :

            if len(newpass) < 8 :
                error = "Your Password Most Be At Less 8 Character"
                return render(request, 'back/error.html' , {'error':error})

            count1 = 0
            count2 = 0
            count3 = 0 
            count4 = 0

            for i in newpass :

                if i > "0" and i < "9" :
                    count1 = 1
                if i > "A" and i < "Z" :
                    count2 = 1
                if i > 'a' and i < 'z' :
                    count3 = 1
                if i > "!" and i < "(" :
                    count4 = 1

            if count1 == 1 and count2 == 1 and count3 == 1 and count4 == 1 :

                user = User.objects.get(username=request.user)
                user.set_password(newpass)
                user.save()
                return redirect('mylogout')

        else:

            error = "Your Password Is Not Correct"
            return render(request, 'back/error.html' , {'error':error})


    return render(request, 'back/changepass.html')

def myregister(request):
        
    if request.method == 'POST':

        name = request.POST.get('name')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if name == '':
            msg = "Input Your Name"
            return render(request, 'front/msgbox.html', {'msg':msg})

        if uname == "" :
            msg = "Input Your Username"
            return render(request, 'front/msgbox.html', {'msg':msg})

        
        if password1 != password2 :
            msg = "Your Passwords Don't Match"
            return render(request, 'front/msgbox.html', {'msg':msg})

        count1 = 0
        count2 = 0
        count3 = 0 
        count4 = 0

        for i in password1 :

            if i > "0" and i < "9" :
                count1 = 1
            if i > "A" and i < "Z" :
                count2 = 1
            if i > 'a' and i < 'z' :
                    count3 = 1
            if i > "!" and i < "(" :
                count4 = 1

        if count1 == 0 or count2 == 0 or count3 == 0 or count4 == 0 :
            msg = "Your Password Is Not Strong"
            return render(request, 'front/msgbox.html', {'msg':msg})

        if len(password1) < 8 :
            msg = "Your Password Must Be 8 Characters"
            return render(request, 'front/msgbox.html', {'msg':msg})

        if len(User.objects.filter(username=uname)) == 0 and len(User.objects.filter(email=email)) == 0:

            user = User.objects.create_user(username=uname,email=email,password=password1)
            b = Manager(name=name, utxt=uname, email=email)
            b.save()

    return render(request, 'front/login.html')

def news_all_show(request,word):
    
    catid = Cat.objects.get(name=word).pk
    allnews = News.objects.filter(ocatid=catid)

    site = Main.objects.get(pk=1)
    news = News.objects.filter(act=1).order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.filter(act=1).order_by('-pk')[:3]
    popnews = News.objects.filter(act=1).order_by('-show')
    popnews2 = News.objects.filter(act=1).order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]
    lastnews2 = News.objects.filter(act=1).order_by('-pk')[:4]

    return render(request, 'front/all_news.html', {'site':site, 'news':news, 'cat':cat, 'subcat':subcat, 'lastnews':lastnews, 'popnews':popnews, 'popnews2':popnews2, 'trending':trending, 'lastnews2':lastnews2, 'allnews':allnews})



