from subprocess import Popen, PIPE


def exec_command(command):
    command_line = command.split(" ")
    command_to_exec = command_line[0]
    target_url = command_line[1]

    if command_to_exec == 'ping':
        command = ['ping', target_url]
        response_body = execute_command(command)
    elif command_to_exec == 'wget':
        command = ['watch', 'wget', '--delete-after', target_url]
        response_body = execute_command(command)
    else:
        print('Unsupported command received: ', command_line)

    return response_body


def execute_command(command):
    pid = Popen(command, stdout=PIPE, stderr=PIPE).pid
    response_body = {'process_id': pid}
    return response_body
