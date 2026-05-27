
---

### `docs/installation.md`

```markdown
# Installation Guide

Follow these steps to deploy the Universal-Security-Hub on a Linux-based system (Kali Linux recommended).

## Prerequisites
* Linux OS with `bash` and `python3` installed.
* Root or Sudo privileges.

## Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/vikashkumarjha-in/Universal-Security-Hub.git](https://github.com/vikashkumarjha-in/Universal-Security-Hub.git)
   cd Universal-Security-Hub

```

2. **Run the Automated Installer:**
The `install_hub.sh` script handles the setup of directories and system commands.
```bash
sudo bash install_hub.sh

```


3. **Execution:**
Once installed, you can launch the dashboard from any terminal by typing:
```bash
utool

```



## Troubleshooting

* **Permissions:** Ensure `install_hub.sh` is executable by running `chmod +x install_hub.sh`.
* **Dependency Issues:** The installer handles tool cloning; ensure your machine has an active internet connection to download the required sub-modules.

```

---
