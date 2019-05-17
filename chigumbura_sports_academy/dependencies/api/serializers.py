from rest_framework import serializers
from dependencies.models import Dependent,Video

class DependentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dependent
        fields = ('id','guardian','sports_category','first_name','dob','last_name','age','allergies','doctor_number','other',)

class VideoSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Video
        fields = ('id','dependent','name','video_link','sport_category','notes','timestamp',)