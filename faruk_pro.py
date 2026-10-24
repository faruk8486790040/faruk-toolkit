# FARUK TOOLKIT V3.0 - LEVEL 10 [PRO]
# From Dhing, Nagaon, Assam
# Certified Ethical Hacker - Professional
import socket
import requests
import threading

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
PURPLE = "\033[95m"
RESET = "\033[0m"

BANNER = f"""
{CYAN}╔═══════════════════════════════════════╗
║                                       ║
║   FARUK TOOLKIT V3.0 - LEVEL 10       ║
║   ██████╗ ██████╗  ██████╗            ║
║   ██╔══██╗██╔══██╗██╔═══██╗           ║
║   ██████╔╝██████╔╝██║   ██║           ║
║   ██╔═══╝ ██╔══██╗██║   ██║           ║
║   ██║     ██║  ██║╚██████╔╝           ║
║   ╚═╝     ╚═╝  ╚═╝ ╚═════╝            ║
║                                       ║
║   From Dhing, Assam - Jai Aai Axom!   ║
║   [ PRO EDITION ]                     ║
╚═══════════════════════════════════════╝{RESET}
"""

print(BANNER)

# [1] IP + PORT SCANNER
def ip_and_port():
    target = input(f"{YELLOW}Target (google.com): {RESET}")
    try:
        ip = socket.gethostbyname(target)
        print(f"{GREEN}[+] IP: {ip}{RESET}")
    except:
        ip = target
        print(f"{RED}[-] IP puwa nai, direct use korim{RESET}")
    
    print(f"{CYAN}[*] Scanning Ports...{RESET}")
    ports = [21,22,23,25,53,80,110,135,139,443,445,3306,8080,8443]
    for port in ports:
        s = socket.socket()
        s.settimeout(0.5)
        if s.connect_ex((ip, port)) == 0:
            print(f"{GREEN}[OPEN] Port {port}{RESET}")
        s.close()

# [2] ADMIN FINDER
def admin_finder():
    site = input(f"{YELLOW}Site URL (https://example.com): {RESET}")
    paths = ["admin","admin/login","administrator","login","wp-admin","admin.php","admin.html","cpanel","admin1","admin2"]
    print(f"{CYAN}[*] Scanning...{RESET}")
    for p in paths:
        url = f"{site.rstrip('/')}/{p}"
        try:
            r = requests.get(url, timeout=3)
            if r.status_code == 200:
                print(f"{GREEN}[FOUND] {url}{RESET}")
        except:
            pass

# [3] SUBDOMAIN FINDER - NEW PRO
def subdomain_finder():
    domain = input(f"{YELLOW}Domain (example.com): {RESET}")
    subs = ["www","mail","ftp","admin","test","dev","api","blog","shop","secure","vpn","m","mobile","support"]
    print(f"{CYAN}[*] Finding Subdomains for {domain}...{RESET}")
    for sub in subs:
        full = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(full)
            print(f"{GREEN}[FOUND] {full} -> {ip}{RESET}")
        except:
            print(f"{RED}[NOT] {full}{RESET}")

# [4] SQLi CHECKER - NEW PRO
def sqli_checker():
    url = input(f"{YELLOW}URL with param (https://site.com/page?id=1): {RESET}")
    payloads = ["'","' OR '1'='1","' OR 1=1--","\" OR \"\"=\"\""]
    print(f"{CYAN}[*] Testing SQL Injection...{RESET}")
    for pay in payloads:
        try:
            r = requests.get(url+pay, timeout=5)
            if "sql" in r.text.lower() or "mysql" in r.text.lower() or "syntax" in r.text.lower():
                print(f"{GREEN}[VULN FOUND!] Payload: {pay}{RESET}")
            else:
                print(f"{YELLOW}[SAFE] Payload: {pay} tested{RESET}")
        except Exception as e:
            print(f"{RED}[ERROR] {e}{RESET}")

# [5] HEADER + SECURITY CHECKER
def header_checker():
    site = input(f"{YELLOW}Site URL: {RESET}")
    try:
        r = requests.get(site, timeout=5)
        print(f"\n{CYAN}--- Security Headers ---{RESET}")
        secure_headers = ["X-Frame-Options","Content-Security-Policy","Strict-Transport-Security","X-XSS-Protection"]
        for h in secure_headers:
            if h in r.headers:
                print(f"{GREEN}[SECURE] {h} found{RESET}")
            else:
                print(f"{RED}[MISSING] {h} missing!{RESET}")
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")

while True:
    print(f"\n{PURPLE}═══ LEVEL 10 PRO MENU ═══{RESET}")
    print(f"{YELLOW}1. IP + Pro Port Scan")
    print(f"2. Admin Panel Finder")
    print(f"3. Subdomain Finder [NEW PRO]")
    print(f"4. SQL Injection Checker [NEW PRO]")
    print(f"5. Security Header Checker")
    print(f"6. Exit - Pro Hacker{RESET}")
    c = input(f"{CYAN}Choose (1-6): {RESET}")
    if c == "1": ip_and_port()
    elif c == "2": admin_finder()
    elif c == "3": subdomain_finder()
    elif c == "4": sqli_checker()
    elif c == "5": header_checker()
    elif c == "6": 
        print(f"{GREEN}Jai Aai Axom! Pro Hacker Faruk - Level 10 Complete!{RESET}")
        break
