#  SCRIPT Paramiko {Router IOS Upgrade} Part_D

import time
from scp import SCPClient
import paramiko
CLI Way of Installing Paramiko:
Install Netmiko/Paramiko
apt-get update
apt-get install python - y
apt-get install build-essential libssl-dev libffi-dev - y
apt-get install python-pip - y

pip install cryptography
pip install paramiko

Install Paramiko on Pycharm IDE:
File > Settings > Project interpreter > Click on “+” > Install “PIP” and “PARAMIKO”

How to Enable SSH on Cisco IOS:
ip domain-name networkjourney.com
crypto key zeroize rsa
crypto key generate rsa modulus 1024
username admin privilege 15 password cisco

line vty 0 4
login local
transport input ssh
exec-timeout 0 10

How to Enable SSH on Linux server:
Goto Linux > Terminal > Execute below commands:
sudo apt update
sudo apt install openssh-server  # install ssh
sudo systemctl status ssh  # ssh must be running active
sudo ufw allow ssh  # disable firewall

ssh username@ip_address  # to take ssh

# 5 || SCP {Complete IOS Software Upgrade Automation step-by-step} (Standalone paramiko script and not re-factoring method)
SCRIPT

Step  # 1 Copy "ios.bin" from your Local Laptop Folder to "terminal server" or "console server"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect("192.168.32.169", port=22, username="network-automation",
                   password="cisco", look_for_keys=False, allow_agent=False)

scp = SCPClient(ssh_client.get_transport())

# copy a file into Ubuntu
scp.put("ios.bin", "/tmp/ios.bin")

scp.close()
print("Job Completed")

Step  # 2 From "terminal sevrer" or "console server" copy into Cisco Router/Switch Flash
network-automation@ubuntu: ~$ scp / tmp/ios.bin admin@192.168.32.200: / ios.bin

Step  # 3 Verify MD5 for "ios.bin" inside Flash0:

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect("192.168.32.200", port=22, username="admin",
                   password="cisco", look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh_client.exec_command(
    "verify /md5 flash0:ios.bin")

output = stdout.read().decode()
print(output)
 time.sleep(60)
  ssh_client.close()

   with open("Verify_md5_check.txt", "w") as f:
        f.write(output)

    Step  # 4 Take Pre-checks
    You can make use of any scripts that we used in earlier for "telnetlib" "paramiko"
    - term len 0
    - show run
    - show ip int brief
    - show ip protocol
    - show version
    - show inventory
    - show cdp

    Step  # 5 Set "bootvar" "reload" on Cisco router/switch
    You can make use of any scripts that we used in earlier for "telnetlib" "paramiko"
    - (config)  # bootvar flash0:ios.bin
    - (config)  # do show bootvar
    - (config)  # do copy run start
    - (config)  # do reload [confirm]

    Step  # 6 Take Post-checks
    You can make use of any scripts that we used in earlier for "telnetlib" "paramiko"
    - term len 0
    - show run
    - show ip int brief
    - show ip protocol
    - show version
    - show inventory
    - show cdp
