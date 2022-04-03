import socket
import threading

IP = '0.0.0.0'
PORT = 5555

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP,PORT))
    server.listen(3)        # number of concurrent connections that server can accept
    print(f'[+] Listening on {IP}:{PORT}')
    
    while 1 == 1:
        client, address = server.accept()
        print(f'[+] New connection accepted from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
        
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[+] Recieved: {request.decode("utf8")}')
        sock.send(b'ACK')

if __name__ == '__main__':
    main()        