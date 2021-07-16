
from django.urls import path
from main.views import add_logs, get_logs, start_logging


urlpatterns = [
    path('get-logs/', get_logs),
    path('add-logs/', add_logs),
    path('start-logging/', start_logging)
]
