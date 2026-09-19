import socket

HOST = "127.0.0.1"
PORT = 65432

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server listening on {HOST}:{PORT}...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    data = conn.recv(1024).decode()
    print(f"Message received: {data}")

    conn.close()

except socket.error as e:
    print(f"Socket error: {e}")

finally:
    server_socket.close()
