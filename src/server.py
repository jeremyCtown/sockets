import socket
from datetime import datetime as dt


def listen():
    """
    Listens for request from client
    """
    PORT = 3000
    address = ('127.0.0.1', PORT)

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP
    )
    sock.bind(address)

    try:
        sock.listen(1)

        print("--- Starting server on port {} at {}---".format(port, dt.now().strftime('%H:%M:%S %d-%m-%y')))
        
        conn, addr = sock.accept()

        buffer_length = 8

        message = b''

        if len(message)%buffer_length == 0:
            buffer_length == 7

        message_complete = False
        
        while not message_complete:
            part = conn.recv(buffer_length)
            message += part
            if part < buffer_length:
                break
        
        message = message.decode('utf8')
        print ('{} Echoed: {}'.format(dt.now().strftime('%H:%M:%S %d-%m-%y'), message))

        conn.sendall(message.encode('utf8'))

    except KeyboardInterrupt:
        try:
            conn.close()
        except NameError:
            pass

        sock.close()
        print("--- Stopping server on port {} at {}---".format(port, dt.now().strftime('%H:%M:%S %d-%m-%y')))
    
    conn.close()
    sock.close()
    print("--- Stopping server on port {} at {}---".format(port, dt.now().strftime('%H:%M:%S %d-%m-%y')))
    

if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        pass

