from logging import info
from django.shortcuts import render,redirect
from django.urls import reverse
from urllib.parse import urlencode
from app.models import data,Upload
import random 
from django.core.mail import send_mail
from django.views.decorators.cache import never_cache
from django.core.exceptions import ValidationError
from .models import data

# Create your views here.
def index(req):
    return redirect('landingpage')

def landingpage(req):
    if req.session.get('id',False):
        return redirect('dashboard')
    return render(req,'landingpage.html')
def home(req):
    return render(req,'home.html')
# def Interactives(req):
#     return render(req,'Interactives.html')
def about_interactive(req):
    return render(req,'about_interactive.html')
def Videos(req):
    return render(req,'Videos.html')
def Resources(req):
    return render(req,'Resources.html')
def new_Login(req):
    return redirect('Venue_Login')
def Venue_Login(req):
    if req.session.get('id',False):
        return redirect('dashboard')
    else:
        return render(req,'Venue_Login.html')
def contact(req):
    return render(req,'contact.html')
def terms_condition(req):
    return render(req,'terms_condition.html')
def accessibility(req):
    return render(req,'accessibility.html')
def register(req):
    return render(req,'register.html') 

@never_cache
def registerdata(request):
    if request.method != "POST":
        return render(request, "register.html")

    # grab raw inputs
    username    = request.POST.get('username', '').strip()
    useremail   = request.POST.get('useremail', '').strip()
    userage_raw = request.POST.get('userage', '').strip()
    discription = request.POST.get('discription', '').strip()
    image       = request.FILES.get('image')
    resume      = request.FILES.get('resume')
    password    = request.POST.get('password', '')
    cpassword   = request.POST.get('cpassword', '')

    # convert age to int if possible (or make None)
    try:
        userage = int(userage_raw) if userage_raw != '' else None
    except ValueError:
        userage = None

    # Create instance but do NOT save yet
    user = data(
        username=username,
        useremail=useremail or None,
        userage=userage,
        discription=discription,
        image=image,
        resume=resume,
        password=password,
        cpassword=cpassword
    )

    try:
        # run validators (field validators + clean())
        # Note: this also calls validate_unique by default (if your model has unique=True)
        user.full_clean()

        # Explicit duplicate-check for email (only if email provided)
        if useremail:
            # case-insensitive check
            if data.objects.filter(useremail__iexact=useremail).exists():
                raise ValidationError({"useremail": ["User already exists!"]})

        # all good -> save
        user.save()
        return render(request, "Venue_Login.html", {"y": "Registration Done"})

    except ValidationError as e:
        # e.message_dict is a dict mapping field -> list(messages)
        return render(request, "register.html", {
            "errors": e.message_dict,
            "formdata": request.POST
        })



@never_cache
def login(request):
    if request.session.get('id',False):
        return redirect('dashboard')
    
    elif request.method == 'POST':
        le = request.POST.get('email')
        lp = request.POST.get('password')

        user = data.objects.filter(useremail=le)
        if user:
            userdata = data.objects.get(useremail=le)
            id = userdata.id
            name = userdata.username
            email = userdata.useremail
            discription = userdata.discription
            image = userdata.image
            age = userdata.userage
            resume = userdata.resume
            password = userdata.password
            cpassword = userdata.cpassword

            if lp == password:
                request.session['id']=id
                return redirect('dashboard')

            else:
                msg = 'Email & Password not Matched'
                return redirect('Venue_Login')

        else:
            msg = 'Email & Password not Matched'
            return redirect('Venue_Login')

    return redirect('Venue_Login')

@never_cache
def dashboard(request):
    if not request.session.get('id',False):
        return redirect('login')

    else:
        id=request.session.get('id')
        userdata = data.objects.get(id=id)
        return render(request, 'dashboard.html', {
        'id': userdata.id,
        'username': userdata.username,
        'useremail': userdata.useremail,
        'userage': userdata.userage,
        'discription': userdata.discription,
        'image': userdata.image,
        'resume': userdata.resume,
         })

@never_cache
def logout(req):
    if not req.session.get('id',False):
        return redirect('login') 

    elif req.session['id']:
        req.session.flush()
        return redirect('login')
    else:
        return redirect('login')
def otp(req):
    return render(req,'forgot_password.html')
  
def send_otp(req):
    if req.method=='POST':
        email=req.POST.get('email')
        if not data.objects.filter(useremail=email).exists():
            return render(req,"forgot_password.html",{
                    "error": "Email not registered,Try again",
                    "show_error": True
                })
        else:
            if req.method=='POST':
                e=req.POST.get('email')
                otp=random.randint(111111,999999)
                req.session['email']=e
                req.session['otp']=otp
                print(otp,e)
                send_mail(
                    "Password reset from Django App",
                    f"Your password reset OTP is: {otp}",  # FIXED f-string to send message and value
                    "tanishparihar14@gmail.com",           # sender email
                    [e],                                   # FIXED LIST not {} reciever email
                    fail_silently=False
        )
                return render(req,'reset.html',{'msg2':""
                ""})
@never_cache
def reset(req):
    return render(req,'forgot_password.html')
def new_pass(req):
    e = req.session['email']
    otp = req.session['otp']
    email_otp = int(req.POST.get('otp'))
    np = req.POST.get('new_pass')
    ncp=req.POST.get('new_cpass')
    if otp!=email_otp:
         msg = "😢 OTP incorrect"
         return render(req,'reset.html',{'msg2':msg})
    if np != ncp:
        msg = "😢 Passwords do not match"
        return render(req, 'reset.html', {'msg2': msg})
    else:
        if np == ncp:
            user=data.objects.get(useremail=e)
            user.password = np
            user.cpassword = ncp
            user.save()
            success_msg = "🎉🥳 Password changed successfully!"
            return render(req,'Venue_Login.html',{'success_msg': success_msg})
           
def upload(req):
    if req.method=='POST':
        a=Upload.objects.create(
            name=req.POST.get('name'),
            age=req.POST.get('age'),
            email=req.POST.get('email'),
            photo=req.FILES.get('photo'),
            video=req.FILES.get('video'),
        )
        return redirect('dashboard')

def show_upload(req,pk):
    userdata=Upload.objects.get(id=pk)
    data={'name':userdata.name,
          'age':userdata.age,
          'email':userdata.email,
          'photo':userdata.photo,
          'video':userdata.video
    }  
    all_data=Upload.objects.filter(email=userdata.email)
    return render(req,'dashboard.html',{'data':data,'up':all_data})
       

# def show_data(req):
#     uploads = Upload.objects.all()   
#     return render(req, 'show_data.html', {'uploads': uploads})

def delete_upload(req,pk):
    upload = Upload.objects.get(id=pk)
    upload.delete()
    return redirect('show_data')

def show_data(request):
    uploads = Upload.objects.all()
    edit_obj = None

    edit_id = request.GET.get('edit')
    if edit_id:
        edit_obj = Upload.objects.get(id=edit_id)

    return render(request, 'show_data.html', {
        'uploads': uploads,
        'edit_obj': edit_obj
    })


def update_upload(request, pk):
    obj = Upload.objects.get(id=pk)

    if request.method == 'POST':
        obj.name = request.POST.get('name')
        obj.age = request.POST.get('age')
        obj.email = request.POST.get('email')

        if request.FILES.get('photo'):
            obj.photo = request.FILES.get('photo')

        if request.FILES.get('video'):
            obj.video = request.FILES.get('video')

        obj.save()
        return redirect('show_data')
