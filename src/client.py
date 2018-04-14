import socket
import sys


def echo():
    """
    Checks that connection to server is solid
    """
    port = 3000

    infos = socket.getaddrinfo('127.0.0.1', port)

    stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]

    client = socket.socket(*stream_info[:3])

    client.connect(stream_info[-1])

    client_msg = str(sys.argv[1])

    message = client_msg + '***END***'

    client.sendall(message.encode('utf8'))

    buffer_length = 8

    message_complete = False

    server_msg = b''

    while not message_complete:
        part = client.recv(buffer_length)
        server_msg += part
        if b'***END***' in server_msg:
            break

    server_msg = server_msg[:-9].decode('utf8')
    print(server_msg)

    client.close()


if __name__ == "__main__":
    try:
        echo()
    except KeyboardInterrupt:
        pass
