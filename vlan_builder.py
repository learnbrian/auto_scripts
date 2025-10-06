from netmiko import ConnectHandler
from getpass import getpass
import re

#def load_device_ips(file_path="device_ips.txt"):
#    with open(file_path, "r") as file:
#        return [line.strip() for line in file if line.strip() and not line.startswith("#")]

def load_device_hostnames(file_path="dev_hostnames.txt"):
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip() and not line.startswith("#")]

#def load_vlan_config(file_path="vlan_config.txt"):
#    with open(file_path, "r") as file:
#        return [line.strip() for line in file if line.strip()]

#def get_existing_vlans(net_connect):
#    output = net_connect.send_command("show vlan brief")
#    vlan_ids = set()
#    for line in output.splitlines():
#        match = re.match(r"^(\d+)\s", line)
#        if match:
#            vlan_ids.add(match.group(1))
#    return vlan_ids

#def parse_vlan_config(vlan_commands):
#    vlan_blocks = []
#    current_block = []
#    for line in vlan_commands:
#        if line.lower().startswith("vlan "):
#            if current_block:
#                vlan_blocks.append(current_block)
#            current_block = [line]
#        else:
#            current_block.append(line)
#    if current_block:
#        vlan_blocks.append(current_block)
#    return vlan_blocks

def configure_vlans_on_devices():
    device_hosts = load_device_hostnames()
#    vlan_commands = load_vlan_config()
#    vlan_blocks = parse_vlan_config(vlan_commands)

    username = input("Enter SSH username: ")
    password = getpass("Enter SSH password: ")

    for host in device_hosts:
        print(f"\n?? Connecting to {host} ...")
        try:
            device = {
                "device_type": "cisco_ios",
                "host": host,
                "username": username,
                "password": password,
                "fast_cli": True,
            }

            net_connect = ConnectHandler(**device)
            hostname = net_connect.find_prompt().strip("#")
            print(f"? Connected to {hostname}")

#               existing_vlans = get_existing_vlans(net_connect)

#             for vlan_block in vlan_blocks:
#                vlan_id = vlan_block[0].split()[1]
#                if vlan_id in existing_vlans:
#                    print(f"? VLAN {vlan_id} already exists on {hostname}, skipping.")
#                    continue

#                print(f"? Creating VLAN {vlan_id} on {hostname}")
#                output = net_connect.send_config_set(vlan_block)
#                print(output)

#            net_connect.save_config()
            net_connect.disconnect()
#            print(f"?? Config saved on {hostname}\n")
            print(f"?? Logging out of {host}\n")

        except Exception as e:
          print(f"? Failed to configure {host}: {e}")

if __name__ == "__main__":
    configure_vlans_on_devices()