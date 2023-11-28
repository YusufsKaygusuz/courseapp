from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import auth, User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token

def user_login(request):
    if request.user.is_authenticated and "next" in request.GET:
        return render(request, "account/login.html", {
                "error": "You don't have authority."
            })
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password=password)

        if user is not None:
            login(request, user)
            nextUrl = request.GET.get("next", None)
            if nextUrl is None:
                return redirect("main_page")
            else:
                return redirect(nextUrl)
        else:
            return render(request, "account/login.html", {
                "error": "The username info or password is wrong!"
            })

    return render(request, "account/login.html")

def user_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
    
        if password == repassword:
            if User.objects.filter(email = email).exists():
                return render(request, "account/register.html", {
                    "error": "The e-mail address is using.",
                    "username": username,
                    "email": email
                })
            else:
                if User.objects.filter(username = username).exists():
                    return render(request, "account/register.html", {
                        "error": "The username is exists.",
                        "username": username,
                        "email": email
                    })
                else:
                    user = User.objects.create_user(username = username, email=email, password=password)
                    this_user = {'email': email}
                    user.is_active= False
                    user.save()
                    current_site = get_current_site(request)
                    mail_subject = 'Activation link has been sent to your email id'
                    message = render_to_string ( 'acc_active_email.html', {
                        'user' : user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': account_activation_token.make_token(user),
                    })
                    to_email = this_user['email']
                    email = EmailMessage(
                        mail_subject, message, to=[to_email]
                    )
                    
                    email.send()
                    return render(request, "account/login.html", {
                     "error": "Please confirm your email address to login!"
                    })
                
        else:
            return render(request, "account/register.html", {
                    "error": "passwords doesn't match each other.",
                    "username": username,
                    "email": email
                })
        
    else:
        return render(request, "account/register.html")
    


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect("main_page")
    else:
        return render(request, "account/register.html")


def user_logout(request):
    logout(request)
    return redirect("main_page")