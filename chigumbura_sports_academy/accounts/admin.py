from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    date_hierarchy='date_joined'
    list_display =['first_name','last_name','email']
    search_fields =['is_superuser','is_client','is_approve']
    list_display =['first_name','last_name','email','is_superuser','is_client','is_approve']
    list_editable =['is_approve','is_superuser']
      
    class Meta:
        model=User
admin.site.register(User,UserAdmin)
