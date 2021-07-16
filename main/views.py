from django.shortcuts import render
from main.models import Logs
from main.lib import do_add_logs
from main.tasks import add_logs as task_add_logs

from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

# Create your views here.
@api_view(['GET'])
def get_logs(request):
    all_logs = {}
    logs = Logs.objects.all()
    for log in logs:
        all_logs[log.id] = log.text
    return Response(dict(status="SUCCESS", logs=all_logs), status=status.HTTP_200_OK) #render(request, "logs_list.html", Logs.objects.all())

@api_view(['POST'])
@parser_classes([JSONParser])
def add_logs(request):
    data = request.data
    log = data["log"]
    do_add_logs(log)
    return Response(dict(status="SUCCESS"), status=status.HTTP_200_OK)

@api_view(['GET'])
@parser_classes([JSONParser])
def start_logging(request):
    task_add_logs.apply()
    return Response(dict(status="SUCCESS"), status=status.HTTP_200_OK)
