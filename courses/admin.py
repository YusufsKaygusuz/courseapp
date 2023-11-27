from django.contrib import admin
from .models import Course, Category

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "isActive", "slug",)
    prepopulated_fields = {"slug": ("title",),}
    #readonly_fields = ("slug",)
    list_filter = ("isActive",)
    list_editable = ("isActive",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",) 
    prepopulated_fields = {"slug": ("name",),}