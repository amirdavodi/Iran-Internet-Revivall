import os
import sys

def run_provider():
    print("========================================")
    print("   PHANTOM BRIDGE - FOREIGN PROVIDER    ")
    print("========================================")
    
    iran_ip = input("[?] Enter Iran Server IP: ").strip()
    iran_port = input("[?] Enter Iran SSH Port (default 22): ").strip() or "22"
    iran_user = input("[?] Enter Iran Username (default root): ").strip() or "root"
    bridge_port = input("[?] Enter Bridge Port (default 2000): ").strip() or "2000"

    print(f"\n[*] Creating a tunnel to {iran_ip}...")
    print("[!] When asked, enter the password of your IRAN server.")
    
    # دستور -R باعث می‌شود پورت سرور خارج روی سرور ایران باز شود
    # این دستور اینترنت را به صورت معکوس تزریق می‌کند
    ssh_cmd = f"ssh -R {bridge_port}:localhost:22 -N -f {iran_user}@{iran_ip} -p {iran_port}"
    
    result = os.system(ssh_cmd)
    
    if result == 0:
        print("\n" + "="*40)
        print("[SUCCESS] Bridge Established!")
        print(f"Internet is now flowing to Iran via port: {bridge_port}")
        print("Keep this terminal open or ensure the process is running.")
        print("="*40)
    else:
        print("\n[ERROR] Could not connect to Iran server. Check IP/Port/Firewall.")

if __name__ == "__main__":
    run_provider()
