import time
import re
from collections import defaultdict
import os

LOG_FILE = "access.log"
BRUTE_FORCE_THRESHOLD = 5

SQLI_PATTERN = re.compile(r"(?i)(union.*select|select.*from|insert.*into|drop.*table|%27|'|1=1)")
LOGIN_PATH = re.compile(r"(?i)(/login|/wp-admin|/admin)")

ip_login_attempts = defaultdict(int)

def follow_log(filename):
    with open(filename, 'r') as file:
        file.seek(0, 2)
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.5)
                continue
            yield line

def analyze_log():
    print("-" * 60)
    print(f"[*] Mini SIEM Initialized")
    print(f"[*] Monitoring {LOG_FILE} for threats in real-time...")
    print("-" * 60)

    for line in follow_log(LOG_FILE):
        match = re.search(r'^(\S+) \S+ \S+ \[.*?\] "(.*?)" (\d{3})', line)
        
        if match:
            ip = match.group(1)
            request = match.group(2)
            status_code = match.group(3)

            if SQLI_PATTERN.search(request):
                print(f"\n[!] THREAT DETECTED: SQL Injection")
                print(f"    Source IP : {ip}")
                print(f"    Payload   : {request}")

            if LOGIN_PATH.search(request) and "POST" in request:
                ip_login_attempts[ip] += 1
                
                if ip_login_attempts[ip] >= BRUTE_FORCE_THRESHOLD:
                    print(f"\n[!] THREAT DETECTED: Potential Brute Force Attack")
                    print(f"    Source IP : {ip}")
                    print(f"    Target    : {request.split()[1] if len(request.split()) > 1 else request}")
                    print(f"    Attempts  : {ip_login_attempts[ip]}")
                    ip_login_attempts[ip] = 0

if __name__ == '__main__':
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, 'w').close()
    
    try:
        analyze_log()
    except KeyboardInterrupt:
        print("\n[*] SIEM Analyzer stopped by user.")