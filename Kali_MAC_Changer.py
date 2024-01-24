import subprocess

def change_mac(interface, new_mac):
    print(f"Changing MAC address of {interface} to {new_mac}")

    # Disable the network interface
    subprocess.call(["sudo", "ifconfig", interface, "down"])

    # Change the MAC address
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])

    # Enable the network interface
    subprocess.call(["sudo", "ifconfig", interface, "up"])

def main():
    interface = input("Enter the network interface (e.g., wlan0): ")
    new_mac = input("Enter the new MAC address (format: XX:XX:XX:XX:XX:XX): ")

    change_mac(interface, new_mac)

    print(f"MAC address of {interface} changed to {new_mac}")

if __name__ == "__main__":
    main()
