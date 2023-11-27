from datetime import date
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from courses.forms import CourseCreateForms, CourseEditForms
from .models import Course, Category

from django.contrib.auth.decorators import login_required, user_passes_test

data = {
    "programming": "Welcome programming's courses",
    "web-development": "Welcome web-development's courses",
    "django": "Django Tutorial is this page",
    "django-api": "Django hardfull api system"
}

db = {
    "courses": [
        {
            "title": "Java Tutorial",
            "description": "Description of Java Tutorial",
            "imgUrl": "1.jpg",
            "slug": "java-tutorial",
            "date": date(2022, 10, 10),
            "isActive": True,
            "isUpdated": False
        },
        {
            "title": "C++ Tutorial",
            "description": "Description of Software Technologies",
            "imgUrl": "2.jpg",
            "slug": "cplus-tutorial",
            "date": date(2022, 9, 10),
            "isActive": True,
            "isUpdated": True
        },
        {
            "title": "Python Tutorial",
            "description": "Description of Python with Object Oriented Technologies",
            "imgUrl": "3.jpg",
            "slug": "python-tutorial",
            "date": date(2022, 8, 10),
            "isActive": True,
            "isUpdated": True
        },

    ],
    "categories": [
        {"id": 1, "name": "Programming", "slug": "programming"},
        {"id": 2, "name": "Django Tutorials", "slug": "django"},
        {"id": 3, "name": "mobil App", "slug": "mobil-app"},
        {"id": 4, "name": "Front-End", "slug": "web-development"},
    ]
}

def index(request):
    kurslar = Course.objects.all()
    kategoriler = Category.objects.all()

    # Kurları filtreleyerek iletmek için bu adımları uyguladık. #
    # for kurs in db["courses"]:
    #      if kurs["isActive"] == True:
    #           kurslar.append(kurs)

    return render(request, 'courses/index.html', {
        'courses': kurslar,
        'categories': kategoriler
    })


def details(request, course_slug):
    try:
        course = Course.objects.get(slug = course_slug)
    except:
        raise Http404()
    
    return render(request, 'courses/details.htm', 
                  {
                      "course" :  course
                  })


def getCoursesByCategoryName(request, slug):
    kurslar = Course.objects.filter(category__slug=slug, isActive=True)
    kategoriler = Category.objects.all()

    return render(request, 'courses/index.html',
                  {
                      'courses': kurslar,
                      'categories': kategoriler,
                      'selected_category': slug
                  })
    """
    if(category_name == "programming"):
        text="Welcome programming's courses"
    elif(category_name == "web-development"):
        text= "Welcome web-development's courses"
    else:
        text= "Oppss We encountered some mistakes."
    """


def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        kurslar = Course.objects.filter(isActive=True, title__contains = q).order_by("date")
        kategoriler = Category.objects.all()
    else:
        return redirect("/courses")

    return render(request, 'courses/list.html',
                  {
                      'courses': kurslar,
                      'categories': kategoriler,
                  })

def isAdmin(user):
    return user.is_superuser

@user_passes_test(isAdmin)
def create_course(request):
    if request.method == "POST":
        form = CourseCreateForms(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/courses")

    else:
        form = CourseCreateForms()
    return render(request, "courses/create_course.html", 
                {
                  "form": form
                })

@login_required()
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course-list.html', {
        'courses': courses
    })

@login_required()
def course_edit(request, id):
    course = get_object_or_404(Course, pk = id)

    if request.method == "POST":
        form = CourseEditForms(request.POST, instance=course)
        form.save()
        return redirect("course_list")
    
    else:
        form = CourseEditForms(instance = course)

    return render(request, "courses/edit-course.html", {
        "form": form
    })

@login_required()
def course_delete(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        course.delete()
        return redirect("course_list")

    return render(request, "courses/course-delete.html", { 
        "course": course
     })