#!/bin/bash

# آدرس پایه بر اساس لینک‌های ارسالی شما
REPO_URL="https://raw.githubusercontent.com/amirdavodi/Iran-Internet-Revivall/refs/heads/main"

echo "=========================================="
echo "   Iran Internet Revival - Auto Installer "
echo "=========================================="
echo "1) Foreign Server (Provider Mode)"
echo "2) Iran Server (Receiver Mode)"
echo "------------------------------------------"
read -p "Select Mode [1-2]: " mode

if [ "$mode" == "1" ]; then
    echo "[*] Downloading Provider Script from GitHub..."
    curl -sLO "$REPO_URL/provider.py"
    if [ $? -eq 0 ]; then
        python3 provider.py
    else
        echo "[ERROR] Failed to download provider.py. Check internet/link."
    fi

elif [ "$mode" == "2" ]; then
    echo "[*] Downloading Receiver Script from GitHub..."
    # در اینجا از پروکسی موقت استفاده نمی‌کنیم چون فرض بر این است که 
    # سرور خارج قبلاً تونل را باز کرده است.
    curl -sLO "$REPO_URL/receiver.py"
    if [ $? -eq 0 ]; then
        python3 receiver.py
    else
        echo "[ERROR] Failed to download receiver.py. Check if Foreign server is active."
    fi
else
    echo "Invalid option. Exiting."
fi
