import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 2000))
    print("Connected to chat server")
    
    while True:
        msg = input("Client: ")
        client_socket.sendall(msg.encode())
        
        if msg.lower() == "end":
            break
        
        data = client_socket.recv(1024).decode()
        print("Server: " + data)

        if data.lower() == "bye":
            break

    client_socket.close()

if __name__ == "__main__":
    main()
