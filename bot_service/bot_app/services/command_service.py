from subprocess import Popen, PIPE


def exec_command(command):
    command_line = command.split(" ")
    command_to_exec = command_line[0]
    target_url = command_line[1]
    if command_to_exec == 'ping':
        response_body = exec_infinite_ping(target_url)
    else:
        response_body = exec_infinite_wget()
    print(response_body)

    return response_body


def exec_infinite_ping(terget_url="mazebolt.com"):
    pid = Popen(['ping', '-t', terget_url], stdout=PIPE, stderr=PIPE).pid
    response_body = {'process_id': pid}
    return response_body


def exec_infinite_wget(target_url="mazebolt.com"):
    # todo: Make command execution infinite.
    pid = Popen(['wget', target_url], stdout=PIPE, stderr=PIPE).pid
    response_body = {'process_id': pid}
    return response_body