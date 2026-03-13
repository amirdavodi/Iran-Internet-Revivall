import os

def run_receiver():
    print("\n--- PHANTOM BRIDGE: IRAN RECEIVER ---")
    bridge_port = input("[?] Enter Bridge Port (default 2000): ").strip() or "2000"

    # تزریق پروکسی به محیط سیستم
    os.environ['ALL_PROXY'] = f"socks5://127.0.0.1:{bridge_port}"
    
    print("[*] Testing Internet...")
    test = os.system("curl -s --connect-timeout 8 https://google.com > /dev/null")
    
    if test == 0:
        print("\n[SUCCESS] Internet is LIVE in Iran!")
        print("[*] Installing Persistence Tools (Autossh)...")
        os.system("sudo apt update && sudo apt install -y autossh")
        
        # فعال‌سازی BBR برای سرعت بیشتر
        os.system("echo 'net.core.default_qdisc=fq' >> /etc/sysctl.conf")
        os.system("echo 'net.ipv4.tcp_congestion_control=bbr' >> /etc/sysctl.conf")
        os.system("sysctl -p")
        print("\n[DONE] System Optimized.")
    else:
        print("\n[ERROR] No internet. Check Provider connection.")

if __name__ == "__main__":
    run_receiver()
