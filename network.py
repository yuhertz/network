import os
import subprocess

def create_fake_network(interface, ssid):
    subprocess.call(f"airmon-ng start {interface}", shell=True)
    subprocess.call(f"airbase-ng -e {ssid} -c 6 mon0", shell=True)

def stop_fake_network():
    subprocess.call("airmon-ng stop mon0", shell=True)

if __name__ == "__main__":
    interface = input("Enter the name of your wireless interface: ")
    ssid = input("Enter the SSID for the fake network: ")

    create_fake_network(interface, ssid)
    print("Fake network created!")

    input("Press Enter to stop the fake network...")
    stop_fake_network()
    print("Fake network stopped!")
