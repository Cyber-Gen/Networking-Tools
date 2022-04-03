import socket

target_host = "0.0.0.0"
target_port = 5555


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)       #AF_INET refers to IPv4 addr or hostname / SOCK_DGRAM refers to UDP client

# send data
client.sendto(b"hello dolly!",(target_host,target_port))

# receive data
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()