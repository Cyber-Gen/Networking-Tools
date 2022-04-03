import socket

target_host = "0.0.0.0"
target_port = 5555


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #AF_INET refers to IPv4 addr or hostname / SOCK_STREAM refers to TCP client

# connect to the target server
client.connect((target_host, target_port))

# send data to target server
client.send(b"hello dolly")

# recieve target server's response
response = client.recv(4096)

print(response.decode())
client.close()