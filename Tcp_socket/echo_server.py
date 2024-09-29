import socket

class EchoServer:
    def __init__(self, portnum):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind(('', portnum))
            self.server.listen(1)
            print(f"Server started on port {portnum}.")
        except Exception as err:
            print(err)

    def serve(self):
        try:
            while True:
                client, address = self.server.accept()
                print('Connected by', address)
                client.sendall(b"Welcome to the Python EchoServer. Type 'bye' to close.\n")
                
                while True:
                    data = client.recv(1024)
                    if not data:
                        break
                    message = data.decode().strip()
                    print(f"Got: {message}")
                    client.sendall(f"Got: {message}\n".encode())
                    if message == 'bye':
                        break
                
                client.close()
                print(f"Connection with {address} closed.")
        except Exception as err:
            print(err)
        finally:
            self.server.close()

if __name__ == "__main__":
    port = 2000
    server = EchoServer(port)
    server.serve()