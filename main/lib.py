from main.models import Logs

def do_add_logs(log: str):
    Logs.objects.create(text=log)
