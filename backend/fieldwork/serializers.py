from rest_framework import serializers
from .models import Observation, FieldUser
from django.contrib.auth.models import User

class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = ('id', 'datetime', 'sample_type', 'location')


class FieldUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldUser
        fields = ('id', 'fname', 'lname')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password')