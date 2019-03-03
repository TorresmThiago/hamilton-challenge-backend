from django.shortcuts import render
from rest_framework import viewsets
from customers.models import Customer
from customers.serializers import CustomerSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


@csrf_exempt
def customer_add(request):
    data = JSONParser().parse(request)
    serializer = CustomerSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def customer_list(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def customer_remove(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
        customer.delete()
        return HttpResponse(status=204)
    except Customer.DoesNotExist:
        return HttpResponse(status=404)


@csrf_exempt
def customer_edit(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(customer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    except Customer.DoesNotExist:
        return HttpResponse(status=404)
