import re
import socket
import settings
from settings import MATH_OPS_REGEX


def main():
    HOST = 'localhost'
    PORT = settings.PORT

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        starting_number = select_starting_number()

        print(f"sending {starting_number} to server")
        s.sendall(str(starting_number).encode())

        data = s.recv(1024)
        print("Server says: ", data.decode())

        text = select_operation_and_operand()
        while text.upper() != "DONE":
            s.sendall(text.encode('utf-8'))
            data = s.recv(1024)
            print('Response from server:', data.decode('utf-8'))
            text = select_operation_and_operand()
        print("Finished with calculations. Ending communications.")


def select_starting_number() -> float:
    while True:
        text = input("Enter starting number: ")
        try:
            starting_number = float(text)
            break
        except ValueError:
            print("Not a valid starting number. Try again.")

    return starting_number


def select_operation_and_operand() -> str:
    while True:
        text = input("Enter operation and second operand: ")
        matches = re.search(MATH_OPS_REGEX, text)
        if matches:
            break
        else:
            print("Invalid input, please try again.")
            continue
    return text


if __name__ == '__main__':
    main()
