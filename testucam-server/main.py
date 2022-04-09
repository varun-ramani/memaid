import socket_service


socket_service.start_listening('', 51285)

while True:
    socket_service.do_poll()