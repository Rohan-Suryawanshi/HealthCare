from rest_framework import serializers
from account.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields=['email', 'name', 'password']
    extra_kwargs={
      'password':{'write_only':True}
    }

  def validate(self, attrs):
    password = attrs.get('password')
    if len(password) < 8:
       raise serializers.ValidationError({
                "general_errors": ["Password must be at least 8 characters long."]
            })
    return attrs

  def create(self, validate_data):
    return User.objects.create_user(**validate_data)

class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email', 'password']

class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'email', 'name']
