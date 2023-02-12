from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .models import Organisation, Post, Philanthropist
from django.http import HttpResponse
from .functions import handel_file
from django.core.files.storage import FileSystemStorage
# Create your views here.

def access(request):
    return render(request,'access.html')

def signup(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            user = User.objects.create_user(
                                            email=request.POST['email'],
                                            password=request.POST['password'],
                                            username=request.POST['name'],
                                            last_name=request.POST['name'],
                                            )
            if user:
                user.save()
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Email already in use')
        else:
            return redirect('dashboard')
    return redirect('/access')

def logins(request):
    if request.method == 'POST':
        if request.POST['ngo_email']:
            username = request.POST['ngo_email']
            password = request.POST['ngo_password']
            is_org = Organisation.objects.filter(email=username)
            if is_org:
                print("hello")
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    messages.error(request, 'invalid Email or Password ')
                    return redirect('/access')
            else:
                    messages.error(request, 'invalid Email or Password ')
                    return redirect('/access')
        else :
            password = request.POST['ph_password']
            username = request.POST['ph_email']
            is_org = Organisation.objects.filter(email=username)
            if is_org==None:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    messages.error(request, 'invalid Email or Password')
                    return redirect('/access')
            else:
                messages.error(request, 'invalid Email or Password ph')
                return redirect('/access')
    return redirect('/access')

def logouts(request):
    logout(request)
    return redirect('/access')

def create_account(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            password=request.POST['password']
            rpassword=request.POST['rpassword']
            username=request.POST['email']
            chk=User.objects.filter(username=username)
            if chk==None:
                pass
                if password==rpassword:
                    
                    user = User.objects.create_user(
                                                username=request.POST['email'],
                                                email=request.POST['email'],
                                                password=request.POST['password'],
                                                )
                    if user:
                        email=request.POST['email']
                        org_obj=Organisation.objects.create(email=email)
                        org_obj.save()
                        user.save()
                        login(request, user)
                        return redirect('dashboard/ngo')
                    else:
                        messages.error(request, 'Email already in use')

                else:
                    messages.error(request, 'Passwords didn\'t match')
            else: 
                        messages.error(request, 'Email already in use')


        else:
            return redirect('dashboard/ngo')
    return render(request,'signupOrg.html')

def create_account_ph(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            password=request.POST['password']
            rpassword=request.POST['rpassword']
            username=request.POST['email']
            chk=User.objects.filter(username=username)
            if chk==None:
                if password==rpassword:
                    
                    user = User.objects.create_user(
                                                username=request.POST['email'],
                                                email=request.POST['email'],
                                                password=request.POST['password'],
                                                )
                    if user:
                        email=request.POST['email']
                        org_obj=Philanthropist.objects.create(email=email)
                        org_obj.save()
                        user.save()
                        login(request, user)
                        return redirect('dashboard/philanthropist')
                    else:
                        messages.error(request, 'Email already in use')

                else:
                    messages.error(request, 'Passwords didn\'t match')
            else: 
                        messages.error(request, 'Email already in use')


        else:
            return redirect('dashboard/philanthropist')
    return render(request,'signupUser.html')

def dashboard(request):
    posts=Post.objects.all()
    return render(request,'dashboard.html',{'posts':posts})

def create_post(request):
    if request.user.is_authenticated :
        print("hello")
        if request.method=='POST':
            user=request.user.username
            caption=request.POST['caption']
            description= request.POST['description']
            image=request.FILES.get('image')
            print(type(image))

            new_post=Post.objects.create(user=user,caption=caption,description=description)
            
            
            new_post.image=request.FILES['image']
            a=new_post.image
            print(type(a))
            # handel_file(request.FILES.get('image'))
            # model_instance = new_post.save(commit=False)
            # model_instance.save()
            new_post.save()
            return HttpResponse('<h1> Uploaded </h1>')
    
    return render(request,"userNewPost.html")

    


    