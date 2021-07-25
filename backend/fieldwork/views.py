from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.core.mail import send_mail
from .models import Observation
from .serializers import ObservationSerializer
from rest_framework import generics, serializers, viewsets
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import ObservationForm
from django.contrib.auth.models import User



def index(request):
    return render(request, 'index.html')


class ObservationCreate(CreateView):
    model = Observation
    form_class = ObservationForm
    success_url = reverse_lazy("thanks")


class ObservationListCreate(generics.ListCreateAPIView):
    # queryset = Observation.objects.latest('datetime')
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer


class ObservationViewSet(viewsets.ModelViewSet):
    serializer_class = ObservationSerializer
    queryset = Observation.objects.all()

    




