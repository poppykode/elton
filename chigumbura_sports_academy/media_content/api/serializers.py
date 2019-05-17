from rest_framework import serializers
from media_content.models import SportsCategory

class SportsCategorySerializer(serializers.ModelSerializer):
  
    class Meta:
        model = SportsCategory
        fields = ('id','name','timestamp',)