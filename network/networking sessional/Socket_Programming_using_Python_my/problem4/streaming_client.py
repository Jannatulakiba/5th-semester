
import socket
import threading

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999

filename = input("Enter the multimedia file to stream: ")

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(filename.encode('utf-8'), (SERVER_IP, SERVER_PORT))

received_bytes = bytearray()

def receive_stream():
    while True:
        try:
            data, _ = client.recvfrom(2048)  
            if data == b"FILE_NOT_FOUND":
                print("File not found on server.")
                break
            if not data:
                break
            received_bytes.extend(data)
            print(f"Received {len(data)} bytes, total: {len(received_bytes)} bytes")
        except:
            break

#
t = threading.Thread(target=receive_stream)
t.start()

while True:
    cmd = input("Type 'play' to open media player (simulation) or 'exit' to quit: ").strip().lower()
    if cmd == 'play':
        print(f"Playing media from {len(received_bytes)} received bytes...")
    elif cmd == 'exit':
        break

client.close()
t.join()
