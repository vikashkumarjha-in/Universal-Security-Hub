📡 Airgeddon Interface Module
Overview
This module functions as the asynchronous orchestration gateway for wireless signal auditing. Given that wireless penetration testing requires specific hardware states (Monitor Mode), packet injection, and interactive user prompts, this module delegates runtime control to qterminal to ensure the primary GUI dashboard remains responsive.

Operational Workflow
Hardware Verification: The module performs an automated check for packet-injection-capable wireless interfaces (e.g., wlan0mon).

Process Isolation: Spawns a dedicated, interactive shell session executing sudo airgeddon. This prevents the master Tkinter loop from freezing during lengthy scanning or handshake capture processes.

Data Persistence: Raw .cap captures, handshake logs, and execution session snapshots are mapped to the centralized ~/UniversalTool/logs/ directory tree for post-session analysis.

Prerequisites
Hardware: Wireless adapter supporting Monitor Mode and Packet Injection (e.g., Atheros AR9271).

Dependencies: aircrack-ng, airgeddon (installed via system package manager).

Permissions: Requires sudo privileges to manipulate wireless device states.
