from rest_framework import serializers
from users.models import NewUser
from django.contrib.auth.hashers import make_password


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields  = ['email','user_name','password']
        extra_kwargs = {'password':{'write_only':True}}

    def validate_password(self, value: str) -> str:

        """
        Hash value passed by user.
        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(self.validate_password(password))
        instance.save()
        
        return instance

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewUser
        fields = [ 
            'email',
            'user_name',
            'is_staff',
            'is_active'
        ]