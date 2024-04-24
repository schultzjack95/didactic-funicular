import socket
import settings

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = settings.PORT

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by: ', addr)
            total = 0
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                received_num = int(data.decode())
                total += received_num
                print("Server received:", received_num)

                conn.sendall(str(total).encode())

            print("Closing connection.")
