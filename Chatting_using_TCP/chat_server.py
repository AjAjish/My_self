import socket

def main():
    # Create server socket..
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Binding is the process of associating a local address and port to a socket
    server_socket.bind(('localhost', 2000))# Port number 2000 is used by SCCP.
    # The listen() call indicates a readiness to accept client connection requests.
    server_socket.listen(1)
    print("Chat server is ready and listening on port 2000")
    # accept() it accepts a received incoming attempt to create a new TCP connection from the remote
    client_socket, addr = server_socket.accept()
    print("Client " + str(addr) + " is now connected")

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print("Client: " + data)
        
        msg = input("Server: ")
        client_socket.sendall(msg.encode())
        
        if msg.lower() == "end":
            break

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
