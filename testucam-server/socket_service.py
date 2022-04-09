import atexit
import socket
import selectors
import time
import image_processing

sel = selectors.DefaultSelector()


def recvall(sock: socket.socket, length: int):
    bytes_received = []
    length_remaining = length

    while length_remaining > 0:
        data_received = sock.recv(min(length_remaining, 2**14))

        if len(data_received) == 0:
            return None

        length_remaining -= len(data_received)
        bytes_received.extend(data_received)

    return bytes(bytes_received)


def destroy_conn(sock: socket.socket):
    print(f"Closing connection to {sock.getpeername()}")
    sel.unregister(sock)
    sock.close()
    time.sleep(1)


def accept_conn(master_sock: socket.socket, mask):
    client_sock, (client_host, client_port) = master_sock.accept()
    print(f"New connection: {client_host}:{client_port}")

    sel.register(client_sock, selectors.EVENT_READ, read_message)


def read_as_image(client_sock: socket.socket):
    # read image length
    image_length_bytes = recvall(client_sock, 4)
    if image_length_bytes is None:
        destroy_conn(client_sock)
        return None

    image_length = int.from_bytes(image_length_bytes, byteorder='big')
    image_bytes = recvall(client_sock, image_length)
    if image_bytes is None:
        destroy_conn(client_sock)
        return None

    print(f"Got image of length {image_length}")

    # image_processing.handle_yuv420(height, width, plane1, plane2, plane3)

def read_message(client_sock: socket.socket, mask):
    message_type = recvall(client_sock, 1)
    if message_type is None:
        destroy_conn(client_sock)
        return None
    
    message_type = message_type[0]
    if message_type == 0x01:
        read_as_image(client_sock)


def start_listening(host, port):
    global sel

    master_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    master_sock.bind((host, port))
    master_sock.listen(100)

    sel.register(master_sock, selectors.EVENT_READ, accept_conn)
    atexit.register(destroy_conn, master_sock)


def do_poll():
    events = sel.select(timeout=-1)
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
