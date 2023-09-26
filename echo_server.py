import socket

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# set a port number for the server to listen on
port = 12345

# bind the socket to a public host and a well-known port
serversocket.bind((host, port))

# become a server socket
serversocket.listen(1)

print("Server started and listening on port", port)

# continuously listen for incoming connections
while True:
    # establish a connection
    clientsocket, address = serversocket.accept()
    
    print("Connection from", address)
    
    # send a welcome message to the client
    message = "Welcome to the server!"
    clientsocket.send(message.encode('ascii'))
    
    # receive data from the client
    data = clientsocket.recv(1024).decode('ascii')
    
    # print the received data
    print("Received data:", data)
    
    # send a response to the client
    response = "Data received successfully!"
    clientsocket.send(response.encode('ascii'))
    
    # close the connection with the client
    clientsocket.close()