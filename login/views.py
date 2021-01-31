from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import QuizQA, GrandFinale, LoggedIn


@login_required(login_url='login')
def home(request):
    context = QuizQA.objects.all()
    u = User.objects.get(id=1)        
    return render(request, 'login/home.html', {'context': context})


# Round1 Groups Views
@login_required(login_url='login')
def round1GA(request):
    context = QuizQA.objects.all().filter(round='Round 1').filter(group='Group A')
    return render(request, 'login/round1/groupA.html', {'context': context})


@login_required(login_url='login')
def round1GB(request):
    context = QuizQA.objects.all().filter(round='Round 1').filter(group='Group B')
    return render(request, 'login/round1/groupB.html', {'context': context})


@login_required(login_url='login')
def round1GC(request):
    context = QuizQA.objects.all().filter(round='Round 1').filter(group='Group C')
    return render(request, 'login/round1/groupC.html', {'context' : context})

@login_required(login_url='login')
def round1GD(request):
    context = QuizQA.objects.all().filter(round='Round 1').filter(group = 'Group D')
    return render(request, 'login/round1/groupD.html', {'context' : context})

@login_required(login_url='login')
def round1GE(request):
    context = QuizQA.objects.all().filter(round='Round 1').filter(group = 'Group E')
    return render(request, 'login/round1/groupE.html', {'context' : context})

# @login_required(login_url='login')
# def round1GF(request):
#     context = QuizQA.objects.all()
#     return render(request, 'login/round1/groupF.html', {'context' : context})

# @login_required(login_url='login')
# def round1GG(request):
#     context = QuizQA.objects.all()
#     return render(request, 'login/round1/groupG.html', {'context' : context})

# @login_required(login_url='login')
# def round1GH(request):
#     context = QuizQA.objects.all()
#     return render(request, 'login/round1/groupH.html', {'context' : context})

# @login_required(login_url='login')
# def round1GI(request):
#     context = QuizQA.objects.all()
#     return render(request, 'login/round1/groupI.html', {'context' : context})

# @login_required(login_url='login')
# def round1GJ(request):
#     context = QuizQA.objects.all()
#     return render(request, 'login/round1/groupJ.html', {'context' : context})

@login_required(login_url='login')
def grandfinale(request):
    return render(request, 'login/grandfinale/gf-welcome.html')


@login_required(login_url='login')
def finalegr(request):
    context = GrandFinale.objects.all().filter(round='General Round')
    return render(request, 'login/grandfinale/gf-generalround.html', {'context' : context})

@login_required(login_url='login')
def finalebr(request):
    context = GrandFinale.objects.all().filter(round='Buzzer Round')
    return render(request, 'login/grandfinale/gf-buzzerround.html', {'context' : context})

@login_required(login_url='login')
def finalerr(request):
    context = GrandFinale.objects.all().filter(round='Risk Round')
    return render(request, 'login/grandfinale/gf-riskround.html', {'context' : context})


def loginpage(request):
    if request.user.is_staff:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user and user.is_staff:
                login(request, user)
                x = LoggedIn.objects.create(name = request.user.username, is_logged_in = True )
                print(x)
                u = User.objects.all()
                for i in u:
                    if i.username != x.username:
                        print(i)
                return redirect('home')
            else:
                messages.warning(request, 'Username or Password are not verified')
                return redirect('login')
        return render(request, 'login/login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm
        if  request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.warning(request, 'Registration is succesful, Once you are verified you can Login !! - QuizMaster')
                return redirect('login')
        return render(request, 'login/register.html', {'form':form})
