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

            data = conn.recv(1024)
            print("First contact; received: ", data.decode())
            conn.sendall(f"Received {data.decode()}.".encode())
            total = 0
            try:
                total = float(data.decode())
            except ValueError as vex:
                print("Couldn't decode starting number sent from client.")

            while True:
                data = conn.recv(1024)
                if not data:
                    break
                rec_s = data.decode()
                print("Server received:", rec_s)

                input_pieces = rec_s.split(" ")
                match input_pieces[0]:
                    case "ADD" | "+":
                        total += float(input_pieces[1])
                    case "SUB" | "-":
                        total -= float(input_pieces[1])
                    case "MULT" | "*":
                        total *= float(input_pieces[1])
                    case "DIV" | "/":
                        if float(input_pieces[1]) != 0:
                            total /= float(input_pieces[1])
                        else:
                            print("Cannot divide by 0. No operation performed.")
                    case "EXP" | "**":
                        total = total ** float(input_pieces[1])
                    case _:
                        print("The received instruction doesn't match what I expected.")

                conn.sendall(("Current total: " + str(total)).encode())

            print("Closing connection.")
