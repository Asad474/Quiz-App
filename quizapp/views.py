from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *
from .forms import *
from .models import *
from django.core.mail import send_mail
from quizproject import settings
from math import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'quizapp/home.html')


def about(request):
    return render(request, 'quizapp/about.html')


@login_required(login_url = 'loginuser')
def mainmenu(request):
    topics =  Quiztopic.objects.all()
    # topics_dict = {key : key.subtopic_set.all().values() for key in topics}

    context = {'topics' : topics, 'title' : 'topics'}
    return render(request, 'quizapp/mainmenu.html', context)


@login_required(login_url = 'loginuser')
def subtopics(request, pk):
    topic = Quiztopic.objects.get(id = pk)
    sub_topics = Subtopic.objects.filter(topic = topic)
    context = {'sub_topics' : sub_topics, 'title' : 'sub_topics', 't' : topic}
    return render(request, 'quizapp/mainmenu.html', context)


@login_required(login_url = 'loginuser')
def instructionpage(request, pk): 
    sub_t = Subtopic.objects.get(id = pk)
    count = sub_t.quizquestion_set.all().count()
    context = {
        't' : sub_t.sub_topic,  
        'count' : count,
        'sub_id' : sub_t.id,
    }  
    
    return render(request, 'quizapp/instructions.html', context)


@login_required(login_url = 'loginuser')
def questionspersubtopic(request, pk):
    sub_t = Subtopic.objects.get(id = pk)
    questions = sub_t.quizquestion_set.all()

    context = {
        'questions' : questions, 
        'sub_id' : sub_t.id,
    }

    return render(request, 'quizapp/questions.html', context)


@login_required(login_url = 'loginuser')
def score(request,pk): 
    if request.method == 'POST':
        sub_t = Subtopic.objects.get(id = pk)
        s = int(request.POST.get('score'))
        total_questions = int(request.POST.get('total-questions'))
        percentage = round(float(s / total_questions *100), 2)
        score = Score(
            user = request.user, 
            sub_topic = sub_t, 
            score = percentage, 
            no_of_correctanswers = s, 
            no_of_questions = total_questions)
        score.save()

        context = {
            'correct_answers' : s, 
            'total_questions' : total_questions,
            'percentage' : percentage,
            'sub_t' : sub_t,
        }

        return render(request, 'quizapp/score.html', context)    

    return redirect('mainmenu') 


@login_required(login_url = 'loginuser')
def scorecard(request):
    user = request.user
    sub_topics = Subtopic.objects.all()
    scorecard = {}

    for t in sub_topics:
        if len(user.score_set.filter(sub_topic = t.id)) > 0:
            s = user.score_set.filter(sub_topic = t.id).order_by('-score')[0] 
            scorecard[t.sub_topic] = s

    context = {'scorecard' : scorecard}
    return render(request, 'quizapp/scorecard.html', context)


@login_required(login_url = 'loginuser')
def viewscores(request, pk):
    user = request.user
    sub = Subtopic.objects.get(id = pk)
    scores = user.score_set.filter(sub_topic = sub.id).order_by('-date')
    context = {'scores' : scores, 'sub_t' : sub}
    return render(request, 'quizapp/all_scores.html', context)


@login_required(login_url = 'loginuser')
def questionform(request):
    if request.user.is_superuser:
        question_form = QuestionForm()

        if request.method == 'POST':
            question_form = QuestionForm(request.POST)
            if question_form.is_valid():
                question_form.save()
                return redirect('home')

        context = {'form' : question_form}
        return render(request, 'quizapp/form.html', context)

    return HttpResponse('You are not authorized to access this page!!!')


@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        valuenext= request.GET.get('next')

        try:
            user = authenticate(request, email = email, password = password)
            login(request, user)
            if valuenext == '' or valuenext == None:
                return redirect('home')
            
            return redirect(valuenext)

        except:
            messages.error(request, 'Email or Password is invalid!!!')

    return render(request,'quizapp/signin.html')


def logoutpage(request):
    logout(request)    
    return redirect('home')


@unauthenticated_user
def registeruser(request):
    form = SignUpForm()

    try:
        if request.method == 'POST':
            form = SignUpForm(request.POST)

            if form.is_valid:                
                user = form.save(commit = False)
                subject = 'Welcome to QuizApp!!!'
                mesg = f'Hi {user.username}, thank you for registering!!!'
                host_email = settings.EMAIL_HOST_USER
                user_email_list = [user.email,]
                send_mail(subject, mesg, host_email, user_email_list)
                form.save()
                messages.success(request, f'Hi {user.username}, thank you for registering!!!')
                return redirect('loginuser')

    except:
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        all_users_username = MyUser.objects.all().values('username')
        all_users_email = MyUser.objects.all().values('email')

        if {'username' : username} in all_users_username:
            messages.error(request, f'User with username "{username}" already exists!!!')

        elif {'email' : email} in all_users_email:
            messages.error(request, 'User with this email id already exists!!!')    

        elif password1 != password2:
            messages.error(request ,'Password and Confirm Password are not matching with each other!!!')

        else:
            messages.error(request ,'Something went wrong!!!')    

        return redirect('registeruser')

    context={'form' : form}
    return render(request,'quizapp/signup.html',context)


@login_required(login_url = 'loginuser')
def userprofile(request):
    u = request.user  
    context = {'u' : u}
    return render(request,'quizapp/user_profile.html',context)


@login_required(login_url = 'loginuser')    
def updateprofile(request):
    user = request.user
    form = UserForm(instance = user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        username = request.POST.get('username')
        all_users_username = MyUser.objects.all().values('username')

        if {'username' : username} in all_users_username and username != user.username:
            messages.error(request, f'User with username "{username}" already exists!!!')

        if form.is_valid():
            form.save()
            return redirect('home')

    context={'u' : user, 'form' : form}
    return render(request, 'quizapp/userform.html', context)        