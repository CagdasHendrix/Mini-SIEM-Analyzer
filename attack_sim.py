import time
from datetime import datetime

def get_current_timestamp():
    return datetime.now().strftime("%d/%b/%Y:%H:%M:%S +0300")

attacks = [
    ("192.168.1.100", "GET /index.html HTTP/1.1", "200"),
    ("10.0.0.5", "GET /login?user=admin' OR 1=1-- HTTP/1.1", "200"),
    ("192.168.1.50", "POST /wp-admin HTTP/1.1", "401"),
    ("192.168.1.50", "POST /wp-admin HTTP/1.1", "401"),
    ("192.168.1.50", "POST /wp-admin HTTP/1.1", "401"),
    ("192.168.1.50", "POST /wp-admin HTTP/1.1", "401"),
    ("192.168.1.50", "POST /wp-admin HTTP/1.1", "401")
]

print("[*] Red Team Attack Simulator Started...")
print("[*] Target: access.log\n")

with open("access.log", "a") as f:
    for ip, request, status in attacks:
        timestamp = get_current_timestamp()
        log_entry = f'{ip} - - [{timestamp}] "{request}" {status} 512\n'
        
        print(f"[+] Sending traffic -> IP: {ip}")
        f.write(log_entry)
        f.flush()
        time.sleep(1.5)

print("\n[*] Attack simulation completed.")