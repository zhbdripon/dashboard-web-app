from accounts.models import Profile
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class MyUserSerializer(serializers.ModelSerializer ):
    class Meta:
        model = User
        fields = ['id', 'email','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(
            **validated_data
        )
        user.set_password(password)
        user.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'user', 'gender', 'dob', 'blood_group', 'avatar','imageb64', 'address', 'mobile']
        extra_kwargs = {'user': {'read_only':True}}



