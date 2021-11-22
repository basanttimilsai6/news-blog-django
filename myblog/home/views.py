from django.shortcuts import render,HttpResponse, redirect, Http404
from .models import Contact
from django.contrib import messages

from blogapp.models import post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.contrib.auth import logout




# Create your views here.
def index(request):
    return render(request,'home/home.html')




def contct(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<5 or len(email)<5 or len(phone)<10 or len(content)<5:
            messages.error(request,'Fillup Your form correctly...')
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,'Your Data has been posted successfully...')
    return render(request,'home/contct.html')




def about(request):
    return render(request,'home/about.html')




def search(request):
    query = request.GET['query']
    if len(query) > 80 or len(query)<3:
        allposts = []
        messages.warning(request,'No Search Result Found')
    else:
        allpoststitle = post.objects.filter(title__icontains=query)
        allpostscontent = post.objects.filter(content__icontains=query)
        allposts = allpoststitle.union(allpostscontent)
    params = {'allposts':allposts, 'query':query}
    return render(request,'home/search.html', params)





def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass0 = request.POST['pass0']
        pass1 = request.POST['pass1']
        #creating user
        if len(username)>10:
            messages.error(request,"Username must be under 10 characters")
            return redirect('/')
        if not username.isalnum():
            messages.error(request,"Username must contains only letters and numbers!!")
            return redirect('/')
        if pass0 != pass1:
            messages.error(request,"Password doesnot match!!")
            return redirect('/')
        else:
            myuser=User.objects.create_user(username, email, pass1)
            myuser.fname = fname
            myuser.lname = lname
            myuser.save()
            messages.success(request,'Your account has been created successfully!!')
            return redirect('/')
    else:
        return HttpResponse('404 not found')
    


def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass2 = request.POST['pass2']


        user = authenticate(request, username=username, password=pass2)

        if user is not None:
            login(request, user)
            messages.success(request,"You're successfully logged in!")
            return redirect('/blog')
        else:
            messages.error(request,"Sorry invalid credentials!")
            return redirect('/')
    else:
        return HttpResponse('404 not found')


def logoutt(request):
    logout(request)
    messages.success(request,"You are successfully logged out..")
    return redirect('/blog')
