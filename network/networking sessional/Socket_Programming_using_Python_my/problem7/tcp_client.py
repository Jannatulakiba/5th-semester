import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))
    print("[CONNECTED] Connected to server.\n")

    try:
        while True:
            msg = input("You: ")
            client.send(msg.encode('utf-8'))
            reply = client.recv(1024).decode('utf-8')
            print("Server:", reply)
    except KeyboardInterrupt:
        print("\n[DISCONNECTED] Closing client.")
    finally:
        client.close()

if __name__ == "__main__":
    start_client()
