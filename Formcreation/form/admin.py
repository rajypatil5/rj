from django.contrib import admin
from .models import registrationModel
from .form import registrationForm

# Register your models here.
class registrationAdmin(admin.ModelAdmin):
    list_display = ['Designation','Name','Email','Mobile']
admin.site.register(registrationModel,registrationAdmin)