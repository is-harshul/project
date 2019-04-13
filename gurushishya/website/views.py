from django.core.mail import send_mail
from . models import AdDetails
from django.shortcuts import render, redirect, HttpResponse
import random, string
from . models import SignupUser
from . forms import userform
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def base(request):
    return render(request, 'base.html', {})

def home(request):
    q_title = request.GET.get('search_title')
    # q_postedby = request.GET.get('search_postedby')
    q_desc = request.GET.get('search_description')
    q_cat = request.GET.get('search_category')
    q_loc = request.GET.get('search_location')
    obj = None
    if q_title is not None: #PostedBy__contains=q_postedby,
        obj = AdDetails.objects.filter(Title__contains=q_title, Description__contains=q_desc, Category__contains=q_cat, Location__contains=q_loc )
    else:
        obj = AdDetails.objects.all()

    return render(request, 'home.html', {'data': obj })

def login(request):
    if 'successSingupMsg' in request.session:
        del request.session['successSingupMsg']
    if request.method == "POST":
        username = request.POST['user']
        password = request.POST['pass']
        raw_user = SignupUser.objects.filter(Username=username, Password=password)
        if len(raw_user) > 0:
            #store user details in vars
            request.session['login_username'] = raw_user[0].Username
            request.session['login_email'] = raw_user[0].Email
            request.session['login_phone'] = raw_user[0].Phone
            return redirect('http://localhost:8000/home/')
        else:
            messages.error(request, "Username and Password did not match.")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def password_reset(request):
	obj = SignupUser()
	uname = request.session.get("name")
	return render(request,"password_reset.html",None)


def logout(request):
    del request.session['login_username']
    del request.session['login_email']
    del request.session['login_phone']
    return redirect("http://localhost:8000/login/")

# @login_required
def profile(request):
    return render(request, 'profile.html', {})

def modal(request):
    return render(request, 'modal.html', {})

def signup(request):
    if request.method == 'POST':
        form = userform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            phone = form.cleaned_data['phone']
            db_obj = SignupUser(Name=name, Username=username, Email=email, Password=password, Phone=phone)
            db_obj.save()
            request.session['successSingupMsg'] = "Successfully Signed-Up."
            # return redirect('http://localhost:8000/login/')
    else:
        form = userform()
    return render(request, "signup.html", {'frm': form})

def password_reset_done(request):
    email = request.POST.get("email")
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = 8
    random_gen_pass = ''.join(random.choice(chars) for x in range(size, 18)) + '@'
    message = 'YOUR LOGIN PASSWORD NOW IS : \n\n' + str(random_gen_pass)
    subject = 'New password'
    fromemail = 'nancy44django@gmail.com'
    toemail = [email]
    send_mail(subject, message, fromemail, toemail)
    SignupUser.objects.filter(Email=email).update(Password = random_gen_pass)
    return render(request,"password_reset_done.html",None)

def enterotp(request):
    return render(request, 'enterotp.html', {})