from functools import partial
import re
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import io
import requests
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.utils import json
from .models import car
from .serializers import carSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    return render(request, 'index.html')

@csrf_exempt
def carApi(request):
    if request.method=='GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        print(stream)
        python_data=JSONParser().parse(stream)
        print(python_data)
        id=python_data.get('id')
        if id is not None:
            cars=car.objects.get(id=id)
            serializer=carSerializer(cars)
            json_data=serializer.data
            return JsonResponse(json_data, safe=False)
        cars=car.objects.all()
        serializer=carSerializer(cars, many=True)
        json_data=serializer.data
        return JsonResponse(json_data, safe=False)
    
    if request.method=='POST':
        print('post called')
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=carSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg':'data saved!'})
        return JsonResponse({'msg':serializer.errors})
    
    if request.method=='PUT':
        print('put called.')
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id',None)
        if id is not None:
            cars=car.objects.get(id=id)
            serializer=carSerializer(cars,data=python_data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'msg':'data updated!'})
            return JsonResponse({'msg':'error data updated!'})
        return JsonResponse({'msg':'error ID!'})
    if request.method=='DELETE':
        print('delete called ..')
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id',None)
        cars=car.objects.get(id=id)
        cars.delete()
        print(cars)
        return JsonResponse({'msg':'record deleted!'})
            
        
            