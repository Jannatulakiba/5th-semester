# tcp_chat_client.py
import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, SERVER_PORT))
print("Connected to TCP server.")

try:
    while True:
        message = input("Client: ")
        client.send(message.encode('utf-8'))

        reply = client.recv(1024).decode('utf-8')
        print(f"Server: {reply}")

except KeyboardInterrupt:
    print("\nClient stopped.")
finally:
    client.close()
