from django.shortcuts import render
from .models import Book
from .serializers import BookSeriallizer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

@api_view()
def BookViewSet(request):
    queryset = Book.objects.all()
    serializerSet = BookSeriallizer(queryset, many = True)
    return Response({
        "data" : serializerSet.data
    })

class Transactions(APIView):
    def get(self, request):
        queryset = Book.objects.all()
        serializerSet = BookSeriallizer(queryset, many = True)
        return Response({
            "data" : serializerSet.data
        })
    
    def post(self, request):
        data = request.data
        serializerSet = BookSeriallizer(data = data)
        if not serializerSet.is_valid():
            return Response({
                "message" : "data not saved",
                "errors" : serializerSet.errors,
            })
        serializerSet.save()
        return Response({
            "message" : "data saved",
            "data" : serializerSet.data    
        })
    
    def put(self, request):
        data = request.data

        if not data.get('id'):
                return Response({
                "message" : "data not saved",
                "errors" : "id not present",
            })

        queryset = Book.objects.get(id = data.get('id'))
        serializerSet = BookSeriallizer(
            queryset, data = data)
        
        if not serializerSet.is_valid():
            return Response({
                "message" : "data not saved",
                "errors" : serializerSet.errors,
            })
        serializerSet.save()
        return Response({
            "message" : "data saved",
            "data" : serializerSet.data    
        })
    
    def patch(self, request):
        data = request.data

        if not data.get('id'):
                return Response({
                "message" : "data not saved",
                "errors" : "id not present",
            })

        queryset = Book.objects.get(id = data.get('id'))
        serializerSet = BookSeriallizer(
            queryset, data = data, partial = True)
        
        if not serializerSet.is_valid():
            return Response({
                "message" : "data not saved",
                "errors" : serializerSet.errors,
            })
        serializerSet.save()
        return Response({
            "message" : "data saved",
            "data" : serializerSet.data    
        })
    
    def delete(self, request):
        data = request.data

        if not data.get('id'):
            return Response({
                "message" : "data not saved",
                "errors" : "id not present",
            })
        
        queryset = Book.objects.get(id = data.get('id')).delete()

        return Response({
            "message" : "data saved",
            "data" : {} 
        })
