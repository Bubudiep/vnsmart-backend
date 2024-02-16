from django.contrib import admin
# Register your models here.
from .models import VNUser
# Register your models here.
class VNUserAdmin(admin.ModelAdmin):
  list_display = ['author', 'fullname', 'email', 'phone', 'avatar']
  list_filter = ['author']
  search_fields = ['author'] 
admin.site.register(VNUser,VNUserAdmin)