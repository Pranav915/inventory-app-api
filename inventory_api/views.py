from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from inventory_api import models
from inventory_api import serializers

class ClubViewSet(viewsets.ModelViewSet):
    queryset = models.Club.objects.all().order_by('club_name')
    serializer_class = serializers.ClubSerializer
    
    def list(self, request, *args, **kwargs):
        self.queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.queryset, many=True)
        return Response({'success':True ,'club_data': serializer.data})