from django.contrib import admin
# Register your models here.
from .models import UserProfiles
# Register your models here.
class UserProfilesAdmin(admin.ModelAdmin):
  list_display = ['user', 'fullname', 'email', 'phone', 'avatar']
  list_filter = ['user']
  search_fields = ['user'] 
admin.site.register(UserProfiles,UserProfilesAdmin)