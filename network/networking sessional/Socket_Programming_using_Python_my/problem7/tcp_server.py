import socket
import threading

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    try:
        while True:
            msg = conn.recv(1024).decode('utf-8')
            if not msg:
                break
            print(f"[{addr}] {msg}")
            reply = f"Server received: {msg}"
            conn.send(reply.encode('utf-8'))
    except ConnectionResetError:
        print(f"[DISCONNECT] {addr} disconnected.")
    finally:
        conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen()
    print("[SERVER STARTED] TCP Server is listening...")

    try:
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    except KeyboardInterrupt:
        print("\n[SERVER STOPPED]")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()
