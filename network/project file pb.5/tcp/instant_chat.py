"""
TCP BACKEND - Fast & Simple
Save as: tcp_backend.py
Run: python tcp_backend.py
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import socket
import threading
import queue

app = Flask(__name__)
CORS(app)

# Message queues
server_queue = queue.Queue()
client_queue = queue.Queue()

# TCP sockets
tcp_server = None
tcp_client = None
client_conn = None

# Connection status
server_connected = False
client_connected = False

def tcp_server_thread():
    global tcp_server, client_conn, server_connected
    
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    
    tcp_server.bind(('127.0.0.1', 7777))
    tcp_server.listen(1)
    
    print("✅ TCP Server listening on 127.0.0.1:7777")
    
    client_conn, addr = tcp_server.accept()
    server_connected = True
    
    print(f"✅ Client connected: {addr}")
    server_queue.put({'status': f'Client connected from {addr[0]}'})
    
    while server_connected:
        try:
            data = client_conn.recv(1024)
            if not data:
                break
            
            msg = data.decode('utf-8')
            print(f"📨 Server received: {msg}")
            server_queue.put({'msg': msg, 'type': 'received'})
        except:
            break
    
    server_connected = False
    if client_conn:
        client_conn.close()

def tcp_client_thread():
    global tcp_client, client_connected
    
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    
    try:
        print("🔄 Client connecting to 127.0.0.1:7777...")
        tcp_client.connect(('127.0.0.1', 7777))
        client_connected = True
        
        print("✅ Client connected to server")
        client_queue.put({'status': 'Connected to server'})
        
        while client_connected:
            try:
                data = tcp_client.recv(1024)
                if not data:
                    break
                
                msg = data.decode('utf-8')
                print(f"📨 Client received: {msg}")
                client_queue.put({'msg': msg, 'type': 'received'})
            except:
                break
        
        client_connected = False
        if tcp_client:
            tcp_client.close()
            
    except Exception as e:
        print(f"❌ Client connection error: {e}")
        client_queue.put({'status': f'Connection failed: {e}'})

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    role = data.get('role')
    
    if role == 'server':
        thread = threading.Thread(target=tcp_server_thread, daemon=True)
        thread.start()
    elif role == 'client':
        thread = threading.Thread(target=tcp_client_thread, daemon=True)
        thread.start()
    
    return jsonify({'success': True})

@app.route('/poll')
def poll():
    role = request.args.get('role')
    
    q = server_queue if role == 'server' else client_queue
    
    messages = []
    status = None
    
    while not q.empty():
        try:
            item = q.get_nowait()
            if 'status' in item:
                status = item['status']
            elif 'msg' in item:
                messages.append({'text': item['msg'], 'type': item['type']})
        except:
            break
    
    return jsonify({'status': status, 'messages': messages})

@app.route('/send', methods=['POST'])
def send():
    global client_conn, tcp_client
    
    data = request.json
    role = data.get('role')
    message = data.get('message')
    
    try:
        if role == 'server' and client_conn:
            client_conn.send(message.encode('utf-8'))
            print(f"📤 Server sent: {message}")
        elif role == 'client' and tcp_client:
            tcp_client.send(message.encode('utf-8'))
            print(f"📤 Client sent: {message}")
        
        return jsonify({'success': True})
    except Exception as e:
        print(f"❌ Send error: {e}")
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 TCP BACKEND SERVER STARTING...")
    print("="*60)
    print("📍 Backend running on: http://127.0.0.1:5555")
    print("📍 Open server.html and client.html in browser")
    print("="*60 + "\n")
    
    # Check if flask-cors is installed
    try:
        from flask_cors import CORS
    except ImportError:
        print("❌ flask-cors not found!")
        print("📦 Install it: pip install flask-cors")
        exit(1)
    
    app.run(host='127.0.0.1', port=5555, debug=False, threaded=True)