import time

malicious_logs = [
    '192.168.1.100 - - [05/May/2026:22:15:00 +0300] "GET /index.html HTTP/1.1" 200 1024\n',
    '10.0.0.5 - - [05/May/2026:22:15:02 +0300] "GET /login?user=admin\' OR 1=1-- HTTP/1.1" 200 512\n',
    '192.168.1.50 - - [05/May/2026:22:15:05 +0300] "POST /wp-admin HTTP/1.1" 401 256\n',
    '192.168.1.50 - - [05/May/2026:22:15:06 +0300] "POST /wp-admin HTTP/1.1" 401 256\n',
    '192.168.1.50 - - [05/May/2026:22:15:07 +0300] "POST /wp-admin HTTP/1.1" 401 256\n',
    '192.168.1.50 - - [05/May/2026:22:15:08 +0300] "POST /wp-admin HTTP/1.1" 401 256\n',
    '192.168.1.50 - - [05/May/2026:22:15:09 +0300] "POST /wp-admin HTTP/1.1" 401 256\n',
]

print("[*] Red Team Attack Simulator Started...")
print("[*] Target: access.log\n")

with open("access.log", "a") as f:
    for log in malicious_logs:
        print(f"[+] Sending traffic -> IP: {log.split()[0]}")
        f.write(log)
        f.flush()
        time.sleep(1.5)

print("\n[*] Attack simulation completed.")