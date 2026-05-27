import tkinter as tk
from tkinter import scrolledtext, ttk
import subprocess
import threading
import os
import getpass

# --- SMART PATH LOGIC ---
username = os.environ.get('SUDO_USER', getpass.getuser())
BASE_PATH = f"/home/{username}/UniversalTool"
ZPHISHER_DIR = os.path.join(BASE_PATH, "tools/zphisher")
HOUND_DIR = os.path.join(BASE_PATH, "tools/hound")

class UniversalSecurityTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Universal Security Hub - Ultimate Edition")
        self.root.geometry("1000x750")
        self.root.configure(bg="#121212")

        # Sidebar
        self.sidebar = tk.Frame(root, width=200, bg="#1e1e1e")
        self.sidebar.pack(side="left", fill="y")
        
        tk.Label(self.sidebar, text="COMMAND CENTER", fg="#00e5ff", bg="#1e1e1e", font=("Arial", 11, "bold")).pack(pady=20)
        
        # --- Target IP Input Section ---
        tk.Label(self.sidebar, text="TARGET IP RANGE:", fg="white", bg="#1e1e1e", font=("Arial", 9)).pack(pady=(10, 0))
        self.target_entry = tk.Entry(self.sidebar, bg="#333", fg="#00ff00", insertbackground="white", justify="center")
        self.target_entry.insert(0, "192.168.1.0/24") 
        self.target_entry.pack(pady=5, padx=10)
        
        btn_style = {"bg": "#333", "fg": "white", "relief": "flat", "width": 20, "height": 2}
        
        # Buttons
        tk.Button(self.sidebar, text="Network Deep Scan", command=self.start_audit, **btn_style).pack(pady=5)
        tk.Button(self.sidebar, text="Vulnerability Scan", command=self.start_vuln_scan, **btn_style).pack(pady=5) # RESTORED
        tk.Button(self.sidebar, text="WiFi Crack", command=self.start_wifi_crack, **btn_style).pack(pady=5)
        tk.Button(self.sidebar, text="Phishing Center", command=self.start_phish, **btn_style).pack(pady=5)
        tk.Button(self.sidebar, text="Hound GPS", command=self.start_hound, **btn_style).pack(pady=5)

        # Output Display
        self.output_area = scrolledtext.ScrolledText(root, bg="#000", fg="#00ff00", font=("Courier", 10))
        self.output_area.pack(side="right", expand=True, fill="both", padx=10, pady=10)
        self.output_area.tag_config("header", foreground="#00e5ff", font=("Courier", 11, "bold"))
        self.output_area.tag_config("vuln", foreground="#ff3d00", font=("Courier", 10, "bold"))

    def log(self, message, tag=None):
        self.output_area.insert(tk.END, f"{message}\n", tag)
        self.output_area.see(tk.END)

    def start_audit(self):
        target = self.target_entry.get().strip()
        if not target: return
        self.output_area.delete('1.0', tk.END)
        threading.Thread(target=self.run_deep_audit, args=(target,), daemon=True).start()

    def run_deep_audit(self, target):
        self.log(f"--- DISCOVERING USERS ON {target} ---", "header")
        cmd = ["sudo", "nmap", "-sn", "-PR", target]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)
        ips = [line.split()[-1].strip("()") for line in proc.stdout if "Nmap scan report for" in line]
        
        for ip in ips:
            self.log(f"\n>>> AUDITING: {ip}", "header")
            p = subprocess.Popen(["sudo", "nmap", "-A", "-T4", "-Pn", "--open", ip], stdout=subprocess.PIPE, text=True)
            for line in p.stdout:
                if "/tcp" in line: self.log(f"   [PORT] {line.strip()}")
                elif "OS details" in line: self.log(f"   [OS]   {line.strip()}")

    # --- RESTORED: VULNERABILITY SCANNER ---
    def start_vuln_scan(self):
        target = self.target_entry.get().strip()
        if not target: return
        self.output_area.delete('1.0', tk.END)
        self.log(f"--- STARTING VULNERABILITY SCAN ON {target} ---", "header")
        
        def run_vuln():
            cmd = ["sudo", "nmap", "--script", "vuln", "-T4", "-F", target]
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)
            for line in p.stdout:
                if "VULNERABLE" in line:
                    self.log(line.strip(), "vuln")
                else:
                    self.log(line.strip())
            self.log("\n[✅] VULNERABILITY SCAN COMPLETE.", "header")
        
        threading.Thread(target=run_vuln, daemon=True).start()

    def start_wifi_crack(self):
        self.log("\n[*] INITIALIZING AIRGEDDON...", "header")
        subprocess.Popen(["qterminal", "-e", "sudo airgeddon"])

    def start_phish(self):
        self.log("\n[*] LAUNCHING ZPHISHER...", "header")
        if os.path.exists(ZPHISHER_DIR):
            subprocess.Popen(["qterminal", "-e", f"bash -c 'cd {ZPHISHER_DIR} && bash zphisher.sh; exec bash'"])

    def start_hound(self):
        self.log("\n[*] LAUNCHING HOUND...", "header")
        if os.path.exists(HOUND_DIR):
            subprocess.Popen(["qterminal", "-e", f"bash -c 'cd {HOUND_DIR} && bash hound.sh; exec bash'"])

if __name__ == "__main__":
    root = tk.Tk()
    app = UniversalSecurityTool(root)
    root.mainloop()
