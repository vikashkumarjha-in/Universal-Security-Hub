# 🛡️ Nmap Execution Module

## Executive Overview
The Nmap Execution Module functions as the core reconnaissance engine within the Universal Security Hub. It is designed to bridge standard Nmap network discovery logic with the application’s asynchronous event loop, ensuring high-performance scanning without compromising the responsiveness of the primary GUI dashboard.

## Operational Methodology
* *Threaded Orchestration*: Binds native Nmap command-line arguments to asynchronous Python threads, allowing for concurrent host discovery and vulnerability assessment.
* *Dynamic Parsing*: Automatically streams scan output into the main_gui.py parsing engine, converting raw console data into structured XML/JSON tracking objects.
* *Session Integrity*: Manages execution state to prevent zombie processes, ensuring that scan interrupts or application exits are handled gracefully by the master supervisor.

## Requirements
* *Dependency*: Requires nmap and python-nmap libraries installed within the host environment.
* *Execution Context*: Designed for elevated privileges (sudo/root) to enable advanced features such as OS fingerprinting, version detection, and stealthy SYN scanning.
