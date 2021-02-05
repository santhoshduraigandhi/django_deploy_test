from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView

from .serializers import JobsSeriaizer
from rest_framework.viewsets import ModelViewSet
from .models import Jobs

# Create your views here.

class HelloWorldView(APIView):
    def get(self,request):
        return Response({"info":"Hello Mr.SAN...."})

# Views for API
class JobsView(ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSeriaizer




