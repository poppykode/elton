from django.contrib import admin
from .models import  Dependent,Video

# Register your models here.
class DependentAdmin(admin.ModelAdmin):
    date_hierarchy='timestamp'
    search_fields =['guardian','first_name','sports_category']
    list_display =['guardian','first_name','sports_category','dob','doctor_number']
    list_editable =['sports_category']

    class Meta:
        model=Dependent
admin.site.register(Dependent,DependentAdmin)

class VideoAdmin(admin.ModelAdmin):
    date_hierarchy='timestamp'


    class Meta:
        model=Video
admin.site.register(Video,VideoAdmin)
