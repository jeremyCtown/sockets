import socket
import sys


def echo():
    port = 3000

    infos = socket.getaddrinfo('127.0.0.1', port)

    stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
    # for sock_data in infors:
    #     if sock_data[1] == socket.SOCK_STREAM:
    #         stream_info = sock_data    #5-tuple repr of socket

    # 5-tuple => (Family, Kind, Protocol, '', Endpoint)

    client = socket.socket(*stream_info[:3])
    # client = socket.socket(
    #     stream_info[0]  Family
    #     stream_info[1]  Kind
    #     stream_info[2]  Protocol
    # )

    client.connect(stream_info[-1]) # endpoint = address

    message = str(sys.argv[1])

    client.sendall(message.encode('utf8'))

    buffer_length = 8

    message_complete = False

    server_msg = b''

    while not message_complete:
        part = conn.recv(buffer_length)
        server_msg += part
        if len(part) < buffer_length:
            break

    # sock = socket.socket(
    #         socket.AF_INET,
    #         socket.SOCK_STREAM,
    #         socket.IPPROTO_TCP
    #     )

    # sock.connect(address)

    # try:
    #     message = input('Enter Echo > ')
    #     sock.sendall(message.encode('utf8'))

    #     received = 0
    #     expected = len(message)

    #     if message == 'quit':
    #         sock.close()
    #         quit()
    #     else:
    #         while received < expected:
    #             data = sock.recv(16)
    #             received += len(data)
        
    #     print(data)

    # except KeyboardInterrupt:
    #     sock.close()
    #     quit()


if __name__ == "__main__":
    try:
        echo()
    except KeyboardInterrupt:
        pass
