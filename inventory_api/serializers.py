from rest_framework import serializers
from inventory_api import models

class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Club
        fields = ('id', 'club_name', 'owner_name', 'club_logo')
    
    