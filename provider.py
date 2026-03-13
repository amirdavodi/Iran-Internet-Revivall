import os

def run_provider():
    print("\n--- PHANTOM BRIDGE: FOREIGN PROVIDER ---")
    iran_ip = input("[?] Iran Server IP: ").strip()
    iran_user = input("[?] Iran Username (default root): ").strip() or "root"
    iran_port = input("[?] Iran SSH Port (default 22): ").strip() or "22"
    bridge_port = input("[?] Bridge Port (default 2000): ").strip() or "2000"

    print(f"\n[*] Connecting to {iran_ip}...")
    # پارامترهای ServerAlive برای جلوگیری از قطع شدن تونل توسط فایروال ایران
    ssh_cmd = (f"ssh -R {bridge_port}:localhost:22 -N -f "
               f"-o ServerAliveInterval=30 -o ServerAliveCountMax=3 "
               f"{iran_user}@{iran_ip} -p {iran_port}")
    
    result = os.system(ssh_cmd)
    if result == 0:
        print(f"\n[SUCCESS] Bridge is active on port {bridge_port}")
        print("[!] Now run the installer on Iran server and choose mode 2.")
    else:
        print("\n[ERROR] Connection failed.")

if __name__ == "__main__":
    run_provider()
