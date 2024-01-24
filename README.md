# KL_MAC_Changer

## Overview

**KL_MAC_Changer** is a Python script for Kali Linux that simplifies MAC address modification on network interfaces.

## Usage

1. **Run Script:**
   - Open terminal.
   - Navigate to script directory.
   - Execute: `python Kali_MAC_Changer.py`

2. **Input:**
   - Enter interface (e.g., wlan0).
   - Input new MAC (format: XX:XX:XX).

3. **Admin Privileges:**
   - Script requires sudo. Enter pass.

4. **Output:**
   - Displays process.
   - Confirms MAC change.

**Example:**
```bash
$ python Kali_MAC_Changer.py
Interface: wlan0
New MAC: 00:11:22
MAC of wlan0 changed.
