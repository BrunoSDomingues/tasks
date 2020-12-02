from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from tasks.models import Task
from tasks.serializer import Serializer


def index(request):
    return HttpResponse("Hello! You're at the postgres index.")


@api_view(["GET"])
def get_all_tasks(request):
    data = Serializer(Task.objects.all(), many=True)
    return JsonResponse(data.data, safe=False)


@api_view(["POST"])
def create_task(request):
    data = JSONParser().parse(request)
    serializer = Serializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors, status=400)


@api_view(["DELETE"])
def delete_all_tasks(request):
    Task.objects.all().delete()
    return HttpResponse("Tasks deleted successfully!")