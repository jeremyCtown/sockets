import socket
# from datetime import datetime as dt


def echo():
    port = 3000
    address = ('127.0.0.1', port)

    sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            socket.IPPROTO_TCP
        )

    sock.connect(address)

    try:
        message = input('Enter Echo > ')
        sock.sendall(message)

        received = 0
        expected = len(message)

        if message == 'quit':
            sock.close()
            quit()
        else:
            while received < expected:
                data = sock.recv(16)
                received += len(data)
        
        print(data)

    except KeyboardInterrupt:
        sock.close()
        quit()

if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        pass
