from rest_framework import serializers
from dependencies.models import Dependent

class DependentSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Dependent
        fields = ('id','guardian','first_name','dob','last_name','age','allergies','doctor_number','other',)