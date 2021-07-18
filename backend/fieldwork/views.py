from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.core.mail import send_mail
from .models import Observation, FieldUser
from .serializers import ObservationSerializer, FieldUserSerializer, UserSerializer
from rest_framework import generics, serializers, viewsets
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import ObservationForm, FieldUserModelForm
from django.contrib.auth.models import User


# def index(request):
#     return render(request, 'fieldwork/index2.html')

def fielduser_formpage(request):
    return render(request, 'fieldwork/fielduser_form.html')

def index(request):
    return render(request, 'index.html')

class FieldUserCreateView(CreateView):
    model = FieldUser
    form_class = FieldUserModelForm
    success_url = reverse_lazy("fieldwork:thanks")


class ObservationCreate(CreateView):
    model = Observation
    form_class = ObservationForm
    success_url = reverse_lazy("thanks")

def add_user(request):
    return render(request, 'fieldwork/form.html')

class ObservationListCreate(generics.ListCreateAPIView):
    # queryset = Observation.objects.latest('datetime')
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer


class ObservationViewSet(viewsets.ModelViewSet):
    serializer_class = ObservationSerializer
    queryset = Observation.objects.all()

    

class FieldUserViewSet(viewsets.ModelViewSet):
    serializer_class = FieldUserSerializer
    queryset = FieldUser.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()