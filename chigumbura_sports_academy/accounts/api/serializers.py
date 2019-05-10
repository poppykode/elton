from rest_framework import serializers
from accounts.models import User
from rest_framework.validators import UniqueValidator

class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email','password',)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
        validated_data['password'],first_name=validated_data['first_name'],last_name=validated_data['last_name'],
        is_approve = False,is_client=True,)      
        return user

class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
