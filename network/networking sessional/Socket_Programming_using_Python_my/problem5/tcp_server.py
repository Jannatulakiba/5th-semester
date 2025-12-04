# tcp_chat_server.py
import socket

SERVER_IP = '0.0.0.0'
SERVER_PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP, SERVER_PORT))
server.listen(1)
print(f"TCP Server listening on {SERVER_IP}:{SERVER_PORT}...")

conn, addr = server.accept()
print(f"Connection established with {addr}")

try:
    while True:
        # ক্লায়েন্টের বার্তা পড়া
        message = conn.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Client: {message}")

        # সার্ভারের উত্তর
        reply = input("Server: ")
        conn.send(reply.encode('utf-8'))

except KeyboardInterrupt:
    print("\nServer stopped.")
finally:
    conn.close()
    server.close()
