# Module Blueprint: Network Reconnaissance (Nmap)

## 1. Technical Architecture
This module utilizes a *Synchronous-to-Asynchronous Bridge* pattern. It executes system-level Nmap commands and pipes the output into a background thread-pool, which then updates the main application GUI in real-time.

## 2. Safety & Ethical Constraints
*   *Authorization*: Scans must only be conducted on networks where the researcher has explicit, written, and verified consent.
*   *Stealth vs. Speed*: Researchers should configure scan intensity (e.g., -T flag) based on the target environment’s traffic handling capacity to avoid inadvertent DoS conditions.

## 3. Error Handling

| Symptom | Root Cause | Remediation |
| :--- | :--- | :--- |
| Nmap not found | Dependency missing | Install via sudo apt install nmap |
| Access Denied | Insufficient privileges | Execute the hub with root context |
| Thread Timeout | Excessive scan time | Increase scan_timeout in configuration settings |

## 4. Verification
*   *Scan Test*: Execute nmap -sV localhost in the terminal to confirm the local Nmap installation is operational before launching the Hub GUI.
