import socket
from datetime import datetime as dt


def listen():
    port = 3000
    address = ('127.0.0.1', port)

    print("--- Starting server on port {} at {}---".format(port, dt.now()))

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP
    )
    sock.bind(address)
    sock.listen(1)

    while True:
        conn, addr = sock.accept()
        buffer_length = 8
        while True:
            message = conn.recv(buffer_length)
            data = message.decode('utf8')

            try:
                if data == 'quit':
                    print("--- Stopping server on port {} at {}---".format(port, dt.now()))
                    conn.close()
                    sock.close()
                    quit()
                elif len(message) < buffer_length:
                    # message_complete = True
                    break
                else:
                    conn.sendall(data.encode('utf8'))
                    print(data)
            except KeyboardInterrupt:
                print("--- Stopping server on port {} at {}---".format(port, dt.now()))
                conn.close()
                sock.close()
                quit()
    

if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        pass



# conn.sendall(message.encode('utf8'))

# while not message_complete:
#     part = conn.recv(buffer_length)
#     print(part.decode('utf8'))
#     if ln(part) < buffer_length:
#         break
