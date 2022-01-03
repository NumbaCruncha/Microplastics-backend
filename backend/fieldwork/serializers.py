from rest_framework import serializers
from .models import Observation
from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_flex_fields import FlexFieldsModelSerializer

class ObservationSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Observation
        fields = ('id', 'datetime', 'user', 'sample_type', 'location')




