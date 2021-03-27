from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User, Skills, Education, Experience, Works, SocialMedias
from .forms import ContactMeForm
# send mails used for contactme form send emails
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    # get table user's latest data(row) based on id
    try:
        user = User.objects.latest('id')
    except:
        user = User.objects.all()
        
    print(type(user))            
    # get table skils's all data(row)
    '''
    for education purpose documentation:
         --it returns <QuerySet .......of all objects
         --type is <class 'django.db.models.query.QuerySet'>
         --we can get objects like ==>  skills = Skills.objects.all()[0] 
                        or
                skills[0]
                it return 0th index object
    '''
    skills = Skills.objects.all()
    # print("\n"*5,Skills.objects.all()[0] ,"\n"*5)
    # get table education's all data(row)
    education = Education.objects.all()
    # get table work's all data(row)
    works = Works.objects.all()
    # get table experience's all data(row)
    experience = Experience.objects.all()
    # get table social media's latest data(row) based on id
    try:
        social = SocialMedias.objects.latest('id')
    except:
        social = SocialMedias.objects.all()

    context =  {'user': user, 'skills': skills,
                'education': education, 'works': works,
                'experience': experience,'social':social,
                'conatct_form':ContactMeForm(),
    }
    return render(request, 'core/index.html',context)


def contactMe(request):
    if request.method == 'POST':
         #all forms data is collected
        form = ContactMeForm(request.POST)
        # check form valid or not
        if form.is_valid():
            # store message to msg
            msg = form['message'].value()
            #save to db
            form.save() 
            try:
                '''
                it sends mail to owner of website
                when someone submit contactme form
                '''
                send_mail(
                    'New Enquire',
                    msg,
                    settings.EMAIL_HOST_USER,
                    ['youemail@gmail.com'],
                    fail_silently=False,                
                )
                '''
                it sends mail to client
                who contact to owner
                '''
                # email address of client
                mail_to = form['mail'].value()
                replay = 'Thaks for contacting we will contact you shortly'
                send_mail(
                    'Replay From Akshay',
                    replay,
                    settings.EMAIL_HOST_USER,
                    [mail_to,],
                    fail_silently=False,                
                )
            except Exception as ex:
                print("Exception in Contact me mail send\n",ex,"\n")
        else:
            print("contact me not valid ",form.errors)
            return
    return redirect('index')
    