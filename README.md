
---

```markdown
# 🛡️ Universal Security Hub

<div align="center">

![Project Banner](assets/screenshots/banner.png)

**An Advanced, Multi-Threaded GUI Command Center for Centralized Network Reconnaissance & Threat Simulation**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Platform: Kali Linux](https://img.shields.io/badge/Platform-Kali%20Linux-blueviolet.svg)]()
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10+-green.svg)]()
[![Framework: OWASP WSTG](https://img.shields.io/badge/Framework-OWASP%20WSTG-orange.svg)]()

<br/>

┌─────────────────────────────────────────────────────────┐
│            UNIVERSAL SECURITY HUB  v1.0                 │
│  ┌──────────────────┐  ┌─────────────────────────────┐  │
│  │  COMMAND CENTER  │  │      LIVE OUTPUT FEED       │  │
│  │                  │  │  >>> DISCOVERING HOSTS ...  │  │
│  │  [Network Scan]  │  │  [PORT] 80/tcp  open http   │  │
│  │  [Vuln Scan   ]  │  │  [OS]   Linux 5.x           │  │
│  │  [WiFi Crack  ]  │  │  [VULN] CVE-2021-44228 !!   │  │
│  │  [Phish Center]  │  │  >>> SCAN COMPLETE          │  │
│  │  [Hound GPS   ]  │  └─────────────────────────────┘  │
│  └──────────────────┘                                   │
└─────────────────────────────────────────────────────────┘

[📖 Documentation](docs/usage.md) · [🚀 Quick Start](#-installation--setup) · [🤝 Contributing](docs/CONTRIBUTING.md) · [⚖️ Disclaimer](#-ethical--legal-disclaimer)

</div>

---

## 📑 Table of Contents
- [🔍 Executive Summary](#-executive-summary)
- [🏗️ System Architecture](#%EF%B8%8F-system-architecture)
- [💻 Technical Stack](#-technical-stack)
- [📦 Core Dependencies](#-core-dependencies)
- [📂 Repository Structure](#-repository-structure)
- [🚀 Installation & Setup](#-installation--setup)
- [💻 Interface Workflow & Usage](#-interface-workflow--usage)
- [⚖️ Ethical & Legal Disclaimer](#-ethical--legal-disclaimer)
- [🤝 Contribution Guidelines](#-contribution-guidelines)
- [📬 Contact & Support](#-contact--support)

---

## 🔍 Executive Summary
The **Universal Security Hub** is a modular security research dashboard engineered to aggregate critical penetration testing utilities into a single asynchronous controller layer. Rather than managing fragmented terminal frames, security analysts can deploy host reconnaissance, vulnerability checking, wireless signal analysis, and identity testing vectors inside an intuitive, color-coded graphical interface. 

### Core Features
* 🏎️ **Non-Blocking Multi-Threading:** Background processes run asynchronously via Python `threading`, ensuring the Tkinter UI layer never experiences deadlocks or window freezes during high-volume scans.
* 📋 **Streamed Subprocess Piping:** Intercepts system standard outputs (`stdout`) in real-time, instantly rendering colorized console reports straight into the UI text widgets.
* 📦 **Self-Contained Installer:** Auto-provisions required application directory pathing, clones remote tool dependencies, handles script execution bits, and overrides current sudo environmental variables safely.

---

## 🏗️ System Architecture

The tool follows a decoupled controller-agent paradigm. The primary graphical engine establishes a centralized command structure while launching isolated runtime modules as dedicated external shell subsystems.

![System Architecture Diagram](assets/screenshots/system_architecture.png)

### Data & Process Flow
1. **Input Collection:** The control layout gathers operational parameters (such as the target subnet strings) via standard sidebar fields.
2. **Asynchronous Spawning:** Action button hooks pass variables down to background workers, utilizing `subprocess.Popen` wrappers to initiate concurrent system execution.
3. **Interactive Terminal Isolation:** Modules requiring real-time terminal interactions (such as credential tracking or live interface selection loops) are isolated into a separate `qterminal` instance, maintaining the structural stability of the main application window.
4. **Log Retention:** Execution findings and tool feeds map directly back to timestamped structural output arrays inside the local runtime tree.

---

## 💻 Technical Stack

* **UI Engine:** Python 3 Custom Tkinter layout
* **Concurrency Model:** Multi-threaded workers + decoupled system process pipes
* **Host Engine Environment:** Kali Linux / Debian-based architectures
* **Operational Dependencies:** Nmap (Network Mapping Engine), Aircrack-ng Framework, Zphisher, Hound PHP Engine
* **Command Shell Deployment:** GNU Bash Scripting

---

## 📦 Core Dependencies

The deployment layout requires specific packages and specialized wireless hardware capabilities for the advanced audit utilities:

### Software Requirements
| Tool / Library | Version Context | Functional Purpose |
| :--- | :--- | :--- |
| `python3-tk` | Core Package | Standard graphical frame bindings |
| `nmap` | System Utility | Raw socket scanning & OS fingerprinting engines |
| `qterminal` | System Utility | Isolated command-line wrapper shell allocation |
| `aircrack-ng` | System Utility | Monitor management and packet injection hooks |
| `php` | Sub-module | Serves underlying identity beacon modules |

### Recommended Wireless Specifications
* **Chipsets:** Atheros AR9271, Ralink RT3070, or Realtek RTL8812AU
* **Capabilities:** Must support raw **Monitor Mode** configuration and **Packet Injection** logic.

---

## 📂 Repository Structure

The code storage tree mirrors an optimized open-source structure designed for clear separation of manuals, core scripts, configuration tables, and reference artifacts:

```text
Universal-Security-Hub/
│
├── 📄 .gitignore                 ← Scope tracking exclusions (caches, workspace configurations)
├── 📄 LICENSE                    ← MIT Open Source Permission Record
├── 📄 README.md                  ← Global Landing Page & Architectural Blueprint (This File)
├── 🔧 install_hub.sh             ← Automated Application Provisioner & Command Registrar
├── 🔧 main_gui.py                ← Primary Multi-Threaded Tkinter Control Center Core
│
├── 📁 assets/                    
│   └── screenshots/              ← Interface captures, design flow diagrams, and banners
│
├── 📁 docs/                      
│   ├── CONTRIBUTING.md           ← Group collaboration standards & git branching parameters
│   ├── installation.md           ← End-user deployment walkthrough manual
│   └── usage.md                  ← Functional guide on individual tool modules
│
├── 📁 src/                       
│   ├── airgeddon/                ← Wireless auditing interface runner files
│   ├── hound/                    ← Web application hosting & parsing assets
│   ├── nmap/                     ← Network reconnaissance profiling and logic files
│   └── zphisher/                 ← Phishing simulation handling scripts
│
└── 📁 examples/                  
    ├── airgeddon/                ← Sample captured handshake capture validations
    ├── hound/                    ← Mock coordinate parsing outputs
    ├── nmap/                     ← Sample network scans and NSE vulnerability logs
    └── zphisher/                 ← Sample structural credential log configurations

```

> **Note:** During runtime execution, the installer establishes a tracking directory tree located at `~/UniversalTool/` to manage tool storage arrays, wordlist indices, and output logs. This pathing matches your underlying code configurations cleanly.

---

## 🚀 Installation & Setup

Deploying the hub into your research environment requires minimal setup. Follow these clean system commands:

### 1. Replicate Project Locally

Clone the environment layout to your machine:

```bash
git clone [https://github.com/vikashkumarjha-in/Universal-Security-Hub.git](https://github.com/vikashkumarjha-in/Universal-Security-Hub.git)
cd Universal-Security-Hub

```

### 2. Execute Deployment Script

The setup routine requires temporary administrative rights to securely link systemic symlinks into global file execution arrays:

```bash
sudo bash install_hub.sh

```

### 3. Clear Shell Execution

Once completed, the script registers a path macro throughout your local user files. Simply call the application from any working terminal panel:

```bash
utool

```

---

## 💻 Interface Workflow & Usage

The integrated layout provides intuitive button triggers that route arguments straight down to background handlers:

1. **Target Subnet Allocation:** Supply the target scope within the interface field window (e.g., `192.168.1.0/24`).
2. **Network Mapping Execution:** Click **Network Deep Scan** or **Vulnerability Scan** to activate the internal Nmap engines. Text output feeds automatically into the centralized application tracking box.
3. **External Environment Deployment:** Selecting options such as **WiFi Crack**, **Phishing Center**, or **Hound GPS** prompts the application to launch dedicated external windows safely, routing user-interactive inputs directly to their native runtime scripts.

---

## ⚖️ Ethical & Legal Disclaimer

**IMPORTANT NOTICE:** The Universal Security Hub is designed strictly for authorized penetration testing research, defensive validation testing, and security engineering instructional usage.

* Operational access must remain restricted to sandboxed testing labs, virtual environments, or networks where you possess formal, explicit written authorization from the infrastructure operator.
* Executing automated social-engineering templates or wireless monitoring injections on external networks without verification is illegal under standard federal statutes, international electronic communications tracking policies, and system authorization parameters.
* The maintainers accept zero liability for actions taken with this infrastructure. All usage must conform to the ethical assessment procedures specified inside the **OWASP Web Security Testing Guide (WSTG)** framework.

---

## 🤝 Contribution Guidelines

We accept modular script integrations, processing optimization fixes, and structural cleanups. To contribute to this project, review the following guidelines:

1. **Fork the Project:** Generate a local fork of the repository structure.
2. **Establish a Feature Branch:** Branch out cleanly using operational prefixes (`git checkout -b feature/enhanced-nmap-parser`).
3. **Commit Code Enhancements:** Format your commits using clean prefixes (`feat(nmap): add tracking profiles`).
4. **Submit a Merge Request:** Open a comprehensive Pull Request detailing your logic modifications, verification tests, and platform results.

*Refer to the [docs/CONTRIBUTING.md](https://www.google.com/search?q=docs/CONTRIBUTING.md) guide for standard code formatting policies.*

---

## 📬 Contact & Support

For platform updates, structural security notifications, or technical deployment queries, please use the standard channels:

* **Issue Management:** [Submit an Issue Ticket](https://www.google.com/search?q=https://github.com/vikashkumarjha-in/Universal-Security-Hub/issues)
* **Maintainer Profile:** [vikashkumarjha-in on GitHub](https://www.google.com/search?q=https://github.com/vikashkumarjha-in)
* **Secure Support Routing:** *support-placeholder@domain.local*

---

*Engineered to provide professional, accessible, and structured modular instrumentation environments.*

**If this project optimizes your security research workflow, consider providing a repository ⭐ on GitHub!**

### 💡 How to use this file:

1. Open your code editor on your Windows machine (e.g., VS Code or Notepad).
2. Open the file `C:\Users\Lenovo\Universal-Security-Hub\README.md`.
3. Copy the entire raw code block above and paste it inside the file.
4. Save the file.
5. When you place your real image file placeholders inside `assets/screenshots/` (matching the names like `banner.png` or `system_architecture.png`), GitHub will read them and render the images perfectly.