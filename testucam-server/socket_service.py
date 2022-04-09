import socket
import selectors

sel = selectors.DefaultSelector()


def recvall(sock: socket.socket, length: int):
    bytes_received = []
    length_remaining = length

    while length_remaining > 0:
        data_received = sock.recv(length_remaining)
        assert len(data_received) > 0, 'Connection closed'

        length_remaining -= len(data_received)
        bytes_received.extend(data_received)

    return bytes(bytes_received)

def destroy_conn(sock: socket.socket):
    sel.unregister(sock)
    sock.close()

def accept_conn(master_sock: socket.socket, mask):
    client_sock, (client_host, client_port) = master_sock.accept()
    print(f"New connection: {client_host}:{client_port}")
    sel.register(client_sock, selectors.EVENT_READ, read_client_message)

def read_client_message(client_sock: socket.socket, mask):
    
    try:
        message_len_bytes = recvall(client_sock, 4)
        print(
            f">>{client_sock.fileno()} received message len field - {message_len_bytes}")

        message_len = int.from_bytes(message_len_bytes, "big")
        print(
            f">>{client_sock.fileno()} decoded message len field - {message_len}")

        message_code = recvall(client_sock, 3)
        print(
            f">>{client_sock.fileno()} received message code field - {message_code}")

        message = recvall(client_sock, message_len)
        print(f">>{client_sock.fileno()} received message field - {message}")

        if len(message) != message_len:
            print(
                f">>{client_sock.fileno()} alas, was counterfeit; wrong len - {len(message)}")
            return

        print(
            f">>{client_sock.fileno()} received entire message - {message_len_bytes + message_code + message}")

        protocol_comm.handle_message(client_sock, message_code, message)
        
    except Exception as e:
        disconnect_socket(client_sock)
        print(f"Failed to read message: {e}")


def start_listening(host, port):
    global sel

    master_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    master_sock.bind((host, port))
    master_sock.listen(100)

    sel.register(master_sock, selectors.EVENT_READ, accept_new_client)

    print(
        f"# Listening => :{master_sock.getsockname()[1]}", flush=True, end='\n')


def do_poll():
    events = sel.select(0.05)
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
