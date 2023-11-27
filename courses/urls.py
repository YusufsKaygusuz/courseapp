from django.http import HttpResponse
from django.urls import path
from . import views

'''
    İlk aşamada url patternlarımızın karşılıklarına gelecek olan sayfaların ayarlanmasını yaptık. 
    Örneğin;
    https://127.0.0.1:8000/
    https://127.0.0.1:8000/anasayfa
    https://127.0.0.1:8000/kurs
'''

urlpatterns = [
    path('', views.index, name="main_page"),
    path('search', views.search, name="search"),
    path('create-course', views.create_course, name="create_course"),
    path('course-list', views.course_list, name="course_list"),
    path('course-edit<int:id>', views.course_edit, name="course_edit"),
    path('course-delete<int:id>', views.course_delete, name="course_delete"),
    path('<course_slug>', views.details, name="courseDetail"),
    path('kategori/<slug:slug>', views.getCoursesByCategoryName, name='courses_by_category'),
]
