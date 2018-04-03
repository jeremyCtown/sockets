import socket
from datetime import datetime as dt


def listen():
    port = 3000
    address = ('127.0.0.1', port)

    print("--- Starting server on port {} at {}---".format(port, dt))

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP
    )
    sock.bind(address)
    sock.listen(1)

    while True:
        conn, addr = sock.accept()
        while True:
            message = conn.recv(16)

            try:
                if message == 'quit':
                    print("--- Stopping server on port {} at {}---".format(port, dt))
                    conn.close()
                    sock.close()
                    quit()
                else:
                    conn.sendall(message.encode('utf8'))
                    print(message)
            except KeyboardInterrupt:
                print("--- Stopping server on port {} at {}---".format(port, dt))
                conn.close()
                sock.close()
                quit()
    

if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        pass


# buffer_length = 8
# message_complete = False
# message = "--- Starting server on port {} at {}---".format(port, dt)

# conn.sendall(message.encode('utf8'))

# while not message_complete:
#     part = conn.recv(buffer_length)
#     print(part.decode('utf8'))
#     if ln(part) < buffer_length:
#         break
