from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

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
                    user.save()
                    return redirect("user_login")
                
        else:
            return render(request, "account/register.html", {
                    "error": "passwords doesn't match each other.",
                    "username": username,
                    "email": email
                })
        
    else:
        return render(request, "account/register.html")

def user_logout(request):
    logout(request)
    return redirect("main_page")