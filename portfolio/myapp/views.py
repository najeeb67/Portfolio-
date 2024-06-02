from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Contacts
from .serializers import ContactSerializer

def index(request):
    return render(request, 'index.html')


@api_view(['POST'])
def create_contact(request):
    if request.method == 'POST':
        serializer =  ContactSerializer (data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


