from django.contrib import admin

from staff.models import Project, Staff

# Register your models here.
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("name","surname","title","projectName","dateofBirth","is_active",)
    list_editable = ("is_active",)
    search_fields = ("name","surname")
   


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("projectName","projectManager","customerName",)
    search_fields = ("projectName","customerName",)