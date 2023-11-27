from django import forms

from courses.models import Course
""" 

class CourseCreateForms(forms.Form):
    title = forms.CharField(
        label="Course Name",
        error_messages={"required":"You must enter course name"},
        widget= forms.TextInput(
            attrs={"class":"form-control"}
            ))
    
    description = forms.CharField(label="Course Description" ,widget=forms.Textarea(attrs={"class":"form-control"}))
    imageUrl = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    slug = forms.SlugField(widget=forms.TextInput(attrs={"class":"form-control"}))
    isActive = forms.BooleanField()
"""   

class CourseCreateForms(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('__all__')
        labels = {
            'title': 'Course Name',
            'description': 'Course Description'
        }
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control"}),
            "description": forms.Textarea(attrs={"class":"form-control"}),
            "imageUrl": forms.TextInput(attrs={"class":"form-control"}),
            "slug": forms.TextInput(attrs={"class":"form-control"}),
            "category": forms.Select(attrs={"class":"form-control"})
        }
        error_messages = {
            "title": {
                "required": "Enter the course title",
                "max_length": "You have to enter max 50 characters"
            },
            "description": {
                "required": "Description is compulsory. ",
            }
        }

class CourseEditForms(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('__all__')
        #fields = ('title', 'description', 'imageUrl', 'slug', 'category')
        labels = {
            'title': 'Course Name',
            'description': 'Course Description'
        }
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control"}),
            "description": forms.Textarea(attrs={"class":"form-control"}),
            "imageUrl": forms.TextInput(attrs={"class":"form-control"}),
            "slug": forms.TextInput(attrs={"class":"form-control"}),
            "category": forms.Select(attrs={"class":"form-control"})
        }
        error_messages = {
            "title": {
                "required": "Enter the course title",
                "max_length": "You have to enter max 50 characters"
            },
            "description": {
                "required": "Description is compulsory. ",
            }
        }