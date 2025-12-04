"""
UDP Chat Server - FAST VERSION (No SocketIO)
Save as: udp_server_fast.py
Run: python udp_server_fast.py
"""

from flask import Flask, render_template_string, request, jsonify
from flask_cors import CORS
import socket
import threading
import queue

app = Flask(__name__)
CORS(app)

# UDP Configuration
UDP_HOST = '127.0.0.1'
UDP_PORT = 6000
MAX_MESSAGE_SIZE = 1000

# Message queue for instant updates
message_queue = queue.Queue()
udp_socket = None
client_address = None

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>UDP Server - Fast</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            padding: 20px;
            min-height: 100vh;
        }
        .container {
            max-width: 650px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 15px 35px rgba(0,0,0,0.3);
        }
        .header {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            padding: 25px;
            text-align: center;
        }
        .header h2 { margin: 0; }
        .status {
            padding: 12px 20px;
            text-align: center;
            font-weight: bold;
            background: #d4edda;
            color: #155724;
        }
        .info {
            padding: 10px;
            background: #d1ecf1;
            color: #0c5460;
            text-align: center;
            font-size: 13px;
        }
        .chat {
            height: 420px;
            overflow-y: auto;
            padding: 20px;
            background: #f8f9fa;
        }
        .msg {
            margin: 12px 0;
            padding: 12px 16px;
            border-radius: 10px;
            max-width: 75%;
            word-wrap: break-word;
            animation: pop 0.2s ease;
        }
        @keyframes pop {
            from { transform: scale(0.9); opacity: 0; }
            to { transform: scale(1); opacity: 1; }
        }
        .msg.sent {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            margin-left: auto;
            text-align: right;
        }
        .msg.received {
            background: white;
            border: 2px solid #e0e0e0;
        }
        .input-area {
            padding: 20px;
            background: white;
            border-top: 2px solid #e0e0e0;
        }
        .char-count {
            text-align: right;
            font-size: 12px;
            color: #666;
            margin-bottom: 8px;
        }
        .char-count.warn { color: #dc3545; font-weight: bold; }
        .input-group { display: flex; gap: 10px; }
        input {
            flex: 1;
            padding: 14px;
            border: 2px solid #dee2e6;
            border-radius: 8px;
            font-size: 15px;
        }
        input:focus {
            outline: none;
            border-color: #4facfe;
        }
        button {
            padding: 14px 28px;
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
        }
        button:hover { opacity: 0.9; }
        button:disabled { opacity: 0.5; cursor: not-allowed; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h2>🖥️ UDP Server (Fast)</h2>
            <small>Connectionless Socket - Max 1000 chars</small>
        </div>
        <div class="status">✅ UDP Server ready on 127.0.0.1:6000</div>
        <div class="info">📡 Connectionless mode | Wait for reply before next message</div>
        <div class="chat" id="chat"></div>
        <div class="input-area">
            <div class="char-count" id="count">0 / 1000</div>
            <div class="input-group">
                <input id="input" placeholder="Type message..." maxlength="1000">
                <button id="btn" onclick="send()">Send</button>
            </div>
        </div>
    </div>

    <script>
        let canSend = true;

        // Fast polling - every 100ms
        setInterval(() => {
            fetch('/poll').then(r => r.json()).then(data => {
                if (data.messages) {
                    data.messages.forEach(m => {
                        addMsg(m.text, m.type);
                        if (m.type === 'received') {
                            canSend = true;
                            document.getElementById('input').disabled = false;
                            document.getElementById('btn').disabled = false;
                        }
                    });
                }
            });
        }, 100);

        function addMsg(text, type) {
            const chat = document.getElementById('chat');
            const msg = document.createElement('div');
            msg.className = 'msg ' + type;
            msg.textContent = text;
            chat.appendChild(msg);
            chat.scrollTop = chat.scrollHeight;
        }

        function send() {
            if (!canSend) return;
            
            const input = document.getElementById('input');
            const text = input.value.trim();
            
            if (text) {
                if (text.length > 1000) {
                    alert('Too long! Max 1000 chars.');
                    return;
                }
                
                fetch('/send', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({msg: text})
                }).then(r => r.json()).then(data => {
                    if (data.success) {
                        addMsg(text, 'sent');
                        input.value = '';
                        updateCount();
                        canSend = false;
                        input.disabled = true;
                        document.getElementById('btn').disabled = true;
                    }
                });
            }
        }

        function updateCount() {
            const input = document.getElementById('input');
            const count = document.getElementById('count');
            const len = input.value.length;
            count.textContent = len + ' / 1000';
            count.className = len > 900 ? 'char-count warn' : 'char-count';
        }

        document.getElementById('input').addEventListener('input', updateCount);
        document.getElementById('input').addEventListener('keypress', e => {
            if (e.key === 'Enter' && canSend) send();
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/poll')
def poll():
    messages = []
    while not message_queue.empty():
        try:
            messages.append(message_queue.get_nowait())
        except:
            break
    return jsonify({'messages': messages})

@app.route('/send', methods=['POST'])
def send():
    global udp_socket, client_address
    
    if not client_address:
        return jsonify({'success': False, 'error': 'No client yet'})
    
    data = request.json
    message = data['msg']
    
    if len(message) > MAX_MESSAGE_SIZE:
        return jsonify({'success': False, 'error': 'Too long'})
    
    try:
        udp_socket.sendto(message.encode('utf-8'), client_address)
        print(f"📤 Sent to {client_address}: {message}")
        return jsonify({'success': True})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'success': False, 'error': str(e)})

def udp_listener():
    global udp_socket, client_address
    
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((UDP_HOST, UDP_PORT))
    
    print(f"✅ UDP Server listening on {UDP_HOST}:{UDP_PORT}")
    
    while True:
        try:
            data, addr = udp_socket.recvfrom(MAX_MESSAGE_SIZE + 100)
            client_address = addr
            message = data.decode('utf-8')
            
            print(f"📨 Received from {addr}: {message}")
            message_queue.put({'text': message, 'type': 'received'})
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 UDP SERVER (FAST) STARTING...")
    print("="*60)
    
    # Start UDP listener
    listener_thread = threading.Thread(target=udp_listener, daemon=True)
    listener_thread.start()
    
    # Wait for socket to bind
    import time
    time.sleep(0.3)
    
    print("🌐 Open in browser: http://127.0.0.1:8082")
    print("📡 UDP Server Port: 6000")
    print("⏳ Waiting for client messages...")
    print("="*60 + "\n")
    
    app.run(host='127.0.0.1', port=8082, debug=False, threaded=True)