# udp_chat_server.py
import socket

SERVER_IP = '0.0.0.0'
SERVER_PORT = 9999
MAX_SIZE = 1000  # max characters per message

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((SERVER_IP, SERVER_PORT))
print(f"UDP Server listening on {SERVER_IP}:{SERVER_PORT}...")

try:
    while True:
        message, client_addr = server.recvfrom(MAX_SIZE)
        message = message.decode('utf-8')
        print(f"Client: {message}")

        reply = input("Server: ")
        server.sendto(reply.encode('utf-8'), client_addr)

except KeyboardInterrupt:
    print("\nServer stopped.")
finally:
    server.close()
