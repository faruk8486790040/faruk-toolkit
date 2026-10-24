import socket

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

print(f"{CYAN}╔════════════════════════════════╗")
print(f"║  FARUK's PRO TOOLKIT - DHING  ║")
print(f"║  Ethical Hacker - Level 8     ║")
print(f"╚════════════════════════════════╝{RESET}")

target = input(f"{YELLOW}Target Website (ex: google.com): {RESET}")

print(f"\n{CYAN}[1] IP Finding...{RESET}")
try:
    ip = socket.gethostbyname(target)
    print(f"{GREEN}    -> IP: {ip}{RESET}")
except:
    ip = target
    print(f"{RED}    -> IP puwa nai{RESET}")

print(f"\n{CYAN}[2] Port Scanning...{RESET}")
for port in [21, 22, 80, 443, 8080, 3306]:
    s = socket.socket()
    s.settimeout(0.5)
    if s.connect_ex((ip, port)) == 0:
        print(f"{GREEN}    -> Port {port}: KHOLA ✓{RESET}")
    else:
        print(f"{RED}    -> Port {port}: Bondho X{RESET}")
    s.close()

print(f"\n{YELLOW}=== SCAN COMPLETE - Jai Aai Axom! ==={RESET}")
