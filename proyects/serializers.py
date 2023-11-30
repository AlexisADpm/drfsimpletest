from rest_framework import serializers

from .models import Poryect

class ProyectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poryect
        fields = ('id', 'title', 'desctiption', 'technology', 'created_at')
        read_only_fields = ('created_at',)