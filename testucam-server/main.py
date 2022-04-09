import socket
import selectors

sel: selectors.DefaultSelector = selectors.DefaultSelector()

def accept_new_conn(incoming_sock):

def setup_master_sock(port=23712):
    master_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    master_sock.bind(('', port))
    master_sock.listen()

def main_loop():
    while True:
        events = sel.select()
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)

if __name__ == "__main__":
    main()