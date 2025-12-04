
import socket
import random
import time
import os

SERVER_IP = "0.0.0.0"
SERVER_PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((SERVER_IP, SERVER_PORT))
print(f"Streaming server listening on {SERVER_IP}:{SERVER_PORT}...")


server_dir = os.path.dirname(os.path.abspath(__file__))

while True:
    data, client_addr = server.recvfrom(1024)
    filename = data.decode('utf-8').strip()
    print(f"Client {client_addr} requested file: {filename}")

    filepath = os.path.join(server_dir, filename)

    if not os.path.exists(filepath):
        server.sendto(b"FILE_NOT_FOUND", client_addr)
        print(f"File {filename} not found in {server_dir}")
        continue

    with open(filepath, "rb") as f:
        while True:
            chunk_size = random.randint(1000, 2000)
            chunk = f.read(chunk_size)
            if not chunk:
                break
            server.sendto(chunk, client_addr)
            time.sleep(0.05)  

    print(f"Finished sending {filename} to {client_addr}")

