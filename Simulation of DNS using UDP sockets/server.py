import socket
# Create the socket object
server = socket.socket()
# Define host and port for the server
host = 'localhost'
port = 40841  # Port number for the server
# Bind the socket to the host and port
server.bind((host, port))
server.listen()
print("Waiting for client connection...")
client, address = server.accept()  # Accept the client connection
print(f"Got connection from {address}...")
client.send(b"Thank you for connecting...")
# Predefined lists for IP addresses and website names
ip_list = [
    "172.16.7.167",
    "172.16.7.168",
    "172.16.7.166",
    "172.16.7.170",
    "172.16.7.169"
]

website_list = [
    'www.google.com',
    'www.youtube.com',
    'www.gmail.com'
]

while True:
    data = client.recv(1024).decode()  # Decode the received bytes
    if not data:
        break  # Break the loop if no data is received

    if data in website_list:
        i = website_list.index(data)
        client.send(ip_list[i].encode())  # Send the corresponding IP address
        print("Found:", data)
    else:
        print("Not Found:", data)

client.close()
server.close()
