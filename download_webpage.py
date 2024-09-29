import socket
def download_webpage(host,port,path):
    # Create a TCP socket socket.
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        # To connect the host and port to the server socket.
        server.connect((host,port))
        request = f"GET {path} HTTP/1.1\r\nHOST: {host} \r\nConnection: close\r\n\r\n"
        # To send the details to server socket 
        server.sendall(request.encode('utf-8'))
        response = b''
        while True:
            data = server.recv(4096)# Here 4096 is 4KB.
            if not data:
                break
            response += data
        response_str = response.decode('utf-8')
        header,body = response_str.split('\r\n\r\n',1)
        return body
    finally:
        # Close the created server.
        server.close()
# Define host,poet and path.
host = 'example.com'
port = 80 # Port 80 is a standardized port number assigned to HTTP.
path = '/'
html = download_webpage(host,port,path)
print(html)