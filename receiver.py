import os
import sys

def run_receiver():
    print("========================================")
    print("   PHANTOM BRIDGE - IRAN RECEIVER       ")
    print("========================================")
    
    bridge_port = input("[?] Enter the Bridge Port (default 2000): ").strip() or "2000"

    # تنظیم پروکسی برای کل سیستم در این نشست (Session)
    os.environ['ALL_PROXY'] = f"socks5://127.0.0.1:{bridge_port}"
    
    print("\n[*] Injecting Internet into system environment...")
    print("[*] Testing connection to Global Internet...")

    # تست با استفاده از curl
    test = os.system("curl -s --connect-timeout 10 https://google.com > /dev/null")
    
    if test == 0:
        print("\n" + "!"*40)
        print("[SUCCESS] INTERNET REACHED IRAN!")
        print("!"*40)
        
        print("\n[*] Now upgrading system and installing permanent tools...")
        # نصب خودکار پکیج‌های پایداری
        os.system("sudo apt update && sudo apt install -y autossh stunnel4")
        
        # بهینه‌سازی سرعت شبکه
        os.system("echo 'net.core.default_qdisc=fq' >> /etc/sysctl.conf")
        os.system("echo 'net.ipv4.tcp_congestion_control=bbr' >> /etc/sysctl.conf")
        os.system("sysctl -p")
        
        print("\n[DONE] Your Iran server is now 'Global'.")
    else:
        print("\n[ERROR] Connection failed. Did you run provider.py on the Foreign server first?")

if __name__ == "__main__":
    run_receiver()
