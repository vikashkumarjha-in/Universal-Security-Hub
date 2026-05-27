#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "Please run with sudo: sudo bash install_hub.sh"
   exit 1
fi

REAL_USER=$(logname)
BASE_DIR="/home/$REAL_USER/UniversalTool"

echo "🚀 Starting Universal Hub Installation..."

mkdir -p "$BASE_DIR/tools" "$BASE_DIR/wordlists" "$BASE_DIR/logs"
cp main_gui.py "$BASE_DIR/"

echo "[*] Downloading Modules (Zphisher, Airgeddon, Hound)..."
cd "$BASE_DIR/tools"
git clone https://github.com/htr-tech/zphisher.git
git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git
git clone https://github.com/techchipnet/hound.git
chmod +x zphisher/zphisher.sh airgeddon/airgeddon.sh hound/hound.sh

echo "[*] Creating 'utool' system command..."
cat <<EOF > /usr/local/bin/utool
#!/bin/bash
cd $BASE_DIR
sudo python3 main_gui.py
EOF
chmod +x /usr/local/bin/utool

chown -R $REAL_USER:$REAL_USER "$BASE_DIR"
echo "✅ SUCCESS! Type 'utool' to start."
