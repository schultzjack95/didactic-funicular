import socket
import settings
from settings import Math_Ops

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = settings.PORT

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
#        text = input("Say something to the server:")
#        s.sendall(text.encode('utf-8'))
        for i in range(1, 10):
            s.sendall(str(i).encode())
            data = s.recv(1024)
            print('Server\'s current total:', int(data.decode('utf-8')))
