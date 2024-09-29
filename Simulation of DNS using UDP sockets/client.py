import socket

# Create the socket object
client = socket.socket()
host = 'localhost'
port = 40841
client.connect((host, port))
print("Connected to the server...")
cmsg = client.recv(1024).decode()
print(cmsg)

while True:
    msg = input("Enter web address to request (or type 'bye' to exit): ")
    client.send(msg.encode())  # Send the website request
    if msg.lower() == "bye":
        break  # Exit the loop if 'bye' is typed
    response = client.recv(1024).decode()  # Receive the response
    print("Response from the server:", response)

client.close()
