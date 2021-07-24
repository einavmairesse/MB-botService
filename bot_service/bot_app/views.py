import json
import os
import signal

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from .services.command_service import exec_command


@csrf_exempt
def start_test(request):
    # todo: support wget
    command = request.POST.get('command')
    response_body = exec_command(command)
    headers = {'Content-Type': 'Application/json'}
    return HttpResponse(json.dumps(response_body), headers=headers)


@csrf_exempt
def stop_test(request):
    process_id = int(request.POST.get('process_id'))
    # todo: equal to kill -9 pid, change signal.SIGTERM to signal.SIGKILL
    os.kill(process_id, signal.SIGTERM)
    return HttpResponse(status=200)
