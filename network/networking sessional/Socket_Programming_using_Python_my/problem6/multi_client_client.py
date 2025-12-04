import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))  # Connect to server

    print("Connected to server. Start chatting! Press Ctrl+C to exit.")
    
    try:
        while True:
            message = input("You: ")
            client.send(message.encode('utf-8'))
            reply = client.recv(1024).decode('utf-8')
            print(f"Server: {reply}")
    except KeyboardInterrupt:
        print("\nChat ended.")
    finally:
        client.close()

if __name__ == "__main__":
    main()

