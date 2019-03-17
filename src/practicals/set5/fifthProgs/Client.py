import socket


def Main():
    host = '127.0.0.1'
    port = 5001
    mySocket = socket.socket()
    mySocket.connect((host, port))
    message = input("You : ")

    while message != 'q':
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()
        print("Server : " + data)
        message = input("You : ")

    mySocket.close()


if __name__ == '__main__':
    Main()
