from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import memeber,gympaln,enquries,equipments
from googlesearch import search
import wikipediaapi
# Create your views here.
def home(request):
    return render(request,'app1/home.html')


def login_user(request):
    if request.method=="POST":
        username=request.POST.get('name')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"your have been succesfully login")
            return redirect('home')
        else:
            messages.error(request, "There was an error. Please check your username and password.")
            return redirect('login')
    return render(request,'app1/login.html')

def register(request):
    if request.method=="POST":
        username=request.POST.get('name')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        email=request.POST.get('email')
        if password!=password2:
            messages.error(request, "There was an error. Please check your password.")
            return redirect('register')
        else:
            user=User.objects.create_user(username,email,password)
            messages.success(request,"you have been registered")
            return redirect('home')
    return render(request,'app1/sigin.html')

def logout_user(request):
    logout(request)
    messages.success(request,"you have been looged out...!")
    return redirect('home')

def view_member(request):
    member=memeber.objects.all()
    return render(request,'app1/member.html',{'member':member})

def view_add(request):
    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        plan=request.POST.get('plan')
        phone=request.POST.get('phone')
        date=request.POST.get('date')
        try:
            plan_instance = gympaln.objects.get(plan=plan)
        except:
                    return render(request,'app1/add_member.html')
        member = memeber.objects.create(name=name,age=age,plan=plan_instance,phonenumber=phone,date=date)
        return redirect('member')
    else:
        return render(request,'app1/add_member.html')
    
def view_enquiries(request):
    enquiries_list = enquries.objects.all()
    return render(request, 'app1/enquries.html', {'enquiries_list': enquiries_list})

def view_enq(request):
    if request.method=="POST":
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        enq=request.POST.get('enqiure')
        enqurie=enquries.objects.create(name=name,conatct=contact,email=email,age=age,gender=gender,description=enqurie)
        return redirect('enquries')
    else:
        return render(request,'app1/add_enq.html')

def view_plan(request):
    plan = gympaln.objects.all()
    return render(request, 'app1/gymplan.html', {'plan':plan})


def view_equipment(request):
    enq=equipments.objects.all()
    return render(request,'app1/equipment.html',{"enq":enq})

def view_planadd(request):
    if request.method=="POST":
        plan=request.POST.get('plan')
        fee=request.POST.get('fee')
        plan=gympaln.objects.create(plan=plan,fee=fee)
        return redirect('plan')
    else:
        return render(request,'app1/add_plan.html')
    
def nutrition(request):
    return render(request,'app1/nutrition.html')

def query(request):
    if request.method=='POST':
        customer="vignesh A/1.0(vigneshaynar@gmail.com)"
        query = request.POST.get('query', '')        
        Search=list(search(query,num=5,stop=5,pause=2))  
        return render(request,'app1/search.html',{'query':query,'results':Search})
    
    return render(request, 'app1/gg.html')
