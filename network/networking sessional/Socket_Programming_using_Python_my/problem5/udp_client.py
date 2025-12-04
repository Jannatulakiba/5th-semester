# udp_chat_client.py
import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 9999
MAX_SIZE = 1000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Connected to UDP server.")

try:
    while True:
        message = input("Client: ")
        client.sendto(message.encode('utf-8'), (SERVER_IP, SERVER_PORT))

        reply, _ = client.recvfrom(MAX_SIZE)
        print(f"Server: {reply.decode('utf-8')}")

except KeyboardInterrupt:
    print("\nClient stopped.")
finally:
    client.close()
