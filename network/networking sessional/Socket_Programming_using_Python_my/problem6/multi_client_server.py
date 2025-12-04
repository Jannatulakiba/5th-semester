import socket
import threading

def handle_client(client_socket, address):
    print(f"[+] Connected to {address}")

    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            print(f"[{address}] says: {message}")
            
            # Reply back
            reply = input("Server reply: ")
            client_socket.send(reply.encode('utf-8'))
        except:
            break
    
    print(f"[-] Connection closed by {address}")
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(5)
    print("[*] Server listening...")

    while True:
        client_socket, address = server.accept()
        # Create a thread for each client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()
        print(f"[#] Active threads: {threading.active_count() - 1}")

if __name__ == "__main__":
    main()
