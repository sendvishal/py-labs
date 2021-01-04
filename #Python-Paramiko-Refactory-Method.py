
 # SCRIPT 1 Create myparamiko.py (Parent Paramiko)

 import paramiko
  import time

   def connect(server_ip, server_port, user, pswd):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(server_ip, port=server_port, username=user,
                           password=pswd, look_for_keys=False, allow_agent=False)
        return ssh_client

    def get_shell(ssh_client):
        connection = ssh_client.invoke_shell()
        return connection

    def send_command(connection, command):
        connection.send(command + "\n")
        time.sleep(3)
        output = connection.recv(4906)
        return output

    def close(ssh_client):
        if ssh_client.get_transport().is_active():
            ssh_client.close()

    SCRIPT  # 1 || “SHOW RUN” on Cisco IOS (Child Paramiko)

    import myparamiko

    ssh_client = myparamiko.connect("192.168.32.200", 22, "admin", "cisco")
    connection = myparamiko.get_shell(ssh_client)
    myparamiko.send_command(connection, 'terminal length 0')
    output = myparamiko.send_command(connection, 'show run')
    print(output.decode())
    # output1 = paramiko1.send_command(connection,'show clock')
    # print(output1.decode())

    myparamiko.close(ssh_client)

    # SCRIPT 2  Create “Users” on Linux (Child Paramiko)

    import myparamiko

    ssh_client = myparamiko.connect(
        "192.168.32.169", 22, "network-automation", "cisco")
    connection = myparamiko.get_shell(ssh_client)  # ssh_estbld
    myparamiko.send_command(
        connection, "sudo useradd -m -d/home/user68 -s/bin/bash user68")
    myparamiko.send_command(connection, "cisco")
    output = myparamiko.send_command(connection, "cat /etc/passwd")
    print(output.decode())

    myparamiko.close(ssh_client)

    # To validate commands
    # cat /etc/passwd
    # less /etc/passwd

    # Script # 3  Trim Unwanted Output from “Show run” on Single Cisco IOS using “split”, “list”, “join” (Child Paramiko)
    SCRIPT

    import myparamiko

    ssh_client = myparamiko.connect("192.168.32.200", 22, "admin", "cisco")
    connection = myparamiko.get_shell(ssh_client)
    myparamiko.send_command(connection, 'terminal length 0')
    output = myparamiko.send_command(connection, 'show run')

    output_str = output.decode()
    # print(output_str)

    list = output_str.split("\n")
    # print(list)
    list = list[4:-1]
    config = "\n".join(list)
    print(config)

    with open("router_backup.txt", "w") as f:
        f.write(config)

    myparamiko.close(ssh_client)

    Reference for .split, list, .join -> https: // realpython.com/python-string-split-concatenate-join/

    # Script 4 Trim Unwanted Output from “Show run” on Multiple Cisco IOS using “split”, “list”, “join” and Save it on Daily basis with “time” module (Child Paramiko)

    import myparamiko

    my_devices = ["192.168.32.200", "192.168.32.201", "192.168.32.202"]
    for devices in my_devices:
        ssh_client = myparamiko.connect(devices, 22, "admin", "cisco")
        connection = myparamiko.get_shell(ssh_client)
        print("Backup started on " + devices)
        myparamiko.send_command(connection, 'terminal length 0')
        output = myparamiko.send_command(connection, 'show run')

        output_str = output.decode()
        # print(output_str)

        list = output_str.split("\n")
        list = list[4:-1]
        config = "\n".join(list)
        print(config)

        # with open(devices + ".txt", "w") as f:
             # print("Backup Saving for " + devices)
             # f.write(config)
             # print("Ok")

        # 192.168.32.200-2020-04-13
        import datetime
        now = datetime.datetime.now()
        today = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
        file = devices + "-" + today + ".txt"
        with open(file, "w") as f:
            print("Backup Saved for " + devices)
            f.write(config)
            print("Ok")

        myparamiko.close(ssh_client)

    # 5  SCRIPT SCP {Complete IOS Software Upgrade Automation step-by-step} (Standalone paramiko script and not re-factoring method)
   

    Step  # 1 Copy "ios.bin" from your Local Laptop Folder to "terminal server" or "console server"
    import paramiko
    from scp import SCPClient

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect("192.168.32.169", port=22, username="network-automation",
                       password="cisco", look_for_keys=False, allow_agent=False)

    scp = SCPClient(ssh_client.get_transport())

    # copy a file into Ubuntu
    scp.put("ios.bin", "/tmp/ios.bin")

    scp.close()
    print("Job Completed")

    # SCRIPT Step 2 From "terminal sevrer" or "console server" copy into Cisco Router/Switch Flash
    network-automation@ubuntu: ~$ scp / tmp/ios.bin admin@192.168.32.200: /ios.bin

    Step  # 3 Verify MD5 for "ios.bin" inside Flash0:
    import paramiko
    import time

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
