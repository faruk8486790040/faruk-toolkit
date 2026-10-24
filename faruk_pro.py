# FARUK TOOLKIT V2.0 - LEVEL 9
# From Dhing, Assam - Jai Aai Axom!
# Ethical Hacker - Level 9
import socket
import requests

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

print(f"{CYAN}╔═══════════════════════════════╗{RESET}")
print(f"{CYAN}║  FARUK's TOOLKIT V2.0 - LEVEL 9  ║{RESET}")
print(f"{CYAN}║  Dhing, Assam - Jai Aai Axom!  ║{RESET}")
print(f"{CYAN}╚═══════════════════════════════╝{RESET}")

def admin_finder():
    site = input(f"{YELLOW}Enter Site (https://example.com): {RESET}")
    paths = ["admin","admin/login","administrator","login","wp-admin","admin.php","admin.html"]
    print(f"{CYAN}[*] Scanning Admin Panels...{RESET}")
    for p in paths:
        url = f"{site}/{p}"
        try:
            r = requests.get(url, timeout=3)
            if r.status_code == 200:
                print(f"{GREEN}[FOUND] {url}{RESET}")
            else:
                print(f"{RED}[NOT] {url} - {r.status_code}{RESET}")
        except:
            print(f"{RED}[ERROR] {url}{RESET}")

def header_checker():
    site = input(f"{YELLOW}Enter Site URL: {RESET}")
    try:
        r = requests.get(site, timeout=5)
        print(f"\n{CYAN}--- HTTP Headers ---{RESET}")
        for k,v in r.headers.items():
            print(f"{k}: {v}")
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")

def ip_and_port():
    target = input(f"{YELLOW}Target Website (google.com): {RESET}")
    print(f"\n{CYAN}[1] IP Finding...{RESET}")
    try:
        ip = socket.gethostbyname(target)
        print(f"{GREEN}   -> IP: {ip}{RESET}")
    except:
        ip = target
        print(f"{RED}   -> IP puwa nai{RESET}")
    print(f"\n{CYAN}[2] Port Scanning...{RESET}")
    for port in [21,22,80,443,8080,3306]:
        s = socket.socket()
        s.settimeout(0.5)
        if s.connect_ex((ip, port)) == 0:
            print(f"{GREEN}   -> Port {port} OPEN{RESET}")
        else:
            print(f"{RED}   -> Port {port} closed{RESET}")
        s.close()

while True:
    print(f"\n{YELLOW}1. IP + Port Scan\n2. Admin Panel Finder (NEW)\n3. Header Checker (NEW)\n4. Exit{RESET}")
    c = input("Choose: ")
    if c == "1": ip_and_port()
    elif c == "2": admin_finder()
    elif c == "3": header_checker()
    elif c == "4": 
        print(f"{CYAN}Jai Aai Axom! - Level 9{RESET}")
        break
