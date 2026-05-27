# Usage Documentation

The Universal-Security-Hub is a GUI-based command center for security professionals and students.

## Dashboard Overview
The interface is divided into the following modules:

* **Target IP Range:** Input the subnet or IP to scan (default: `192.168.1.0/24`).
* **Network Deep Scan:** Performs comprehensive host discovery and port enumeration.
* **Vulnerability Scan:** Scans the target for potential vulnerabilities using Nmap scripting engines.
* **WiFi Crack:** Opens an external `airgeddon` instance for wireless auditing.
* **Phishing Center:** Launches `zphisher` for controlled social engineering testing.
* **Hound GPS:** Provisions `hound` for geographic location data extraction.

## Safety and Best Practices
* **Authorization:** Only perform scans on networks and devices for which you have explicit, written permission.
* **Execution:** All external tools (Airgeddon, Zphisher, Hound) run in separate terminal windows to ensure the main GUI dashboard remains stable and responsive.