import socket

# EchoClient
class EchoClient:
    def __init__(self, host, portnum):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, portnum))
        except Exception as err:
            print(err)

    def run(self):
        try:
            with self.sock, \
                 self.sock.makefile('r', encoding='utf-8') as sock_in, \
                 self.sock.makefile('w', encoding='utf-8') as sock_out:
                 
                print(sock_in.readline().strip())
                while True:
                    message = input().strip()
                    sock_out.write(f"{message}\n")
                    sock_out.flush()
                    response = sock_in.readline().strip()
                    print(response)
                    if message == 'bye':
                        break
        except Exception as err:
            print(err)

if __name__ == "__main__":
    host = 'localhost'
    port = 2000
    server = EchoClient(host,port)
    server.run()