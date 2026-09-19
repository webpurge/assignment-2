import socket

HOST = "127.0.0.1"
PORT = 65432

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    client_socket.sendall("Hello from client!".encode())
    print("Message sent to server.")

except socket.error as e:
    print(f"Socket error: {e}")

finally:
    client_socket.close()
