from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db.models.fields import PointField
from django.contrib.gis.geos import Point, Polygon
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.urls import reverse
from django.utils.timezone import now

DEFAULT_LOCATION = (-45.87867, 170.49587)

class Organisation(models.Model):
    org_name = models.CharField(default=None, max_length=200)
    pri_contact_fname = models.CharField(default=None, max_length=200)    
    pri_contact_lname = models.CharField(default=None, max_length=200)


  
class Observation(models.Model):
    datetime = models.DateTimeField(default=now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='observations', related_query_name='observations')
    location = PointField(default=Point(DEFAULT_LOCATION))
    sample_type = models.CharField(default='Unknown', max_length=200)

    def str(self):
        return self.datetime

    def __repr__(self):
        return str(self.datetime)




