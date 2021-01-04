# Paramiko script
# Script 1: Basic Paramiko script to collect “show version” output on Cisco IOS {Exec method}

import time
import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect("192.168.32.200", port=22, username="admin",
                   password="cisco", look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh_client.exec_command("show version")

output = stdout.read().decode()
print(output)

ssh_client.close()

with open("R1_show_version.txt", "w") as f:
    f.write(output)

# Script 2: Basic Paramiko script to take “ifconfig” output on Linux server {Exec method}


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect("192.168.32.169", port=22, username="network-automation",
                   password="cisco", look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh_client.exec_command("ifconfig")

output = stdout.read().decode()
print(output)

ssh_client.close()

with open("ifconfig.txt", "w") as f:
    f.write(output)

# Script 3: Basic Paramiko script to take “ifconfig” output on Linux server {Exec method}


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect("192.168.32.169", port=22, username="network-automation",
                   password="cisco", look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh_client.exec_command(
    "sudo apt update && apt install nmap", get_pty=True)
stdin.write("cisco\n")

# print(stderr.read().decode()

output = stdout.read().decode()
print(output)

ssh_client.close()

with open("logs-collected.txt", "w") as f:
    f.write(output)

# Script 4: Script to configure “Loopback”, “OSPF” using Paramiko Invoke method


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect("192.168.32.169", port=22, username="network-automation",
                   password="cisco", look_for_keys=False, allow_agent=False)

remote_connection = ssh_client.invoke_shell()

remote_connection.send("conf t\n")
remote_connection.send("int lo 1\n")
remote_connection.send("ip add 1.1.1.1 255.255.255.255\n")
remote_connection.send("int lo 2\n")
remote_connection.send("ip add 2.2.2.2 255.255.255.255\n")
remote_connection.send("router ospf 1\n")
 remote_connection.send("network 0.0.0.0 0.0.0.0 area 0\n")
  remote_connection.send("end\n")

   import time
    time.sleep(3)

    output = remote_connection.recv(4096)
    print(output.decode())

# Script 5: Script to configure “Loopback”, “OSPF” and Vlans via “for” loops using Paramiko Invoke Method


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect("192.168.32.200", port=22, username="admin",
                   password="cisco", look_for_keys=False, allow_agent=False)

remote_connection = ssh_client.invoke_shell()

remote_connection.send("conf t\n")
remote_connection.send("int lo 1\n")
remote_connection.send("ip add 1.1.1.1 255.255.255.255\n")
remote_connection.send("int lo 2\n")
remote_connection.send("ip add 2.2.2.2 255.255.255.255\n")
 remote_connection.send("router ospf 1\n")
  remote_connection.send("network 0.0.0.0 0.0.0.0 area 0\n")
   for n in range(1, 10):
        print("Creating VLAN " + str(n))
        remote_connection.send("vlan " + str(n) + "\n")
        remote_connection.send("name Test_Vlan_ " + str(n) + "\n")
    remote_connection.send("end\n")

    time.sleep(3)

    ssh_client.close()

    output = remote_connection.recv(4096)
    print(output.decode())

    # to save the output
    with open("logs-collected.txt", "w") as f:
        f.write(output.decode())
