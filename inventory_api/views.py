from django.shortcuts import render
from rest_framework import viewsets
from inventory_api import models
from inventory_api import serializers

class ClubViewSet(viewsets.ModelViewSet):
    queryset = models.Club.objects.all().order_by('club_name')
    serializer_class = serializers.ClubSerializer
    