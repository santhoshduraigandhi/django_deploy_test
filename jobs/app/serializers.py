from rest_framework import serializers

from .models import Jobs

class JobsSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'