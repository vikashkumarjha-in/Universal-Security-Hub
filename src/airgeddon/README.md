# 📡 Airgeddon Interface Module

## Overview
This module acts as the integration gateway for wireless security auditing. Because wireless environments require administrative card access, interactive terminal monitoring, and multi-stage menus, this module interfaces directly with `qterminal`.

## Operational Workflow
1. **Interface Tracking:** The framework verifies the availability of a packet-injection-capable wireless interface (`wlan0`/`wlan1`).
2. **Execution Hook:** Spawns a separate, interactive console wrapper executing `sudo airgeddon` to prevent shell disruption or freezing within the master Tkinter dashboard.
3. **Log Handling:** Captured raw `.cap` files and execution flags are stored locally within the `~/UniversalTool/logs/` environment directory.