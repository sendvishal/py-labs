

# SCRIPT 1 || {ADVANCE} NETMIKO SCRIPT FOR ENABLE “ADMIN DOWN” INTERFACES USING REGEX QUERY SEARCH AND WHILE INFINITE LOOP ITERATIONS

from netmiko import ConnectHandler

 import re
  regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

   def check(Ip):
        if (re.search(regex, Ip)):
            print("Valid Ip address")
        else:
            print("Invalid Ip address")
    if __name__ == '__main__':
        Ip = input("Enter your IP address:")
        check(Ip)

    cisco_device123 = {
        "device_type": "cisco_ios",
        "ip": Ip,
        "username": "admin",
        "password": "cisco",
        "port": 22
    }

    net_connect123 = ConnectHandler(**cisco_device123)

    var = 1
    while var == 1:
        interface123 = input("enter the interface you want to enable:")
        output123 = net_connect123.send_command("show ip int " + interface123)
        if 'Invalid input detected' in output123:
            print('You entered and invalid interface')

        else:
            first_line123 = output123.splitlines()[0]
            print(first_line123)
            if not "up" in first_line123:
                print("Interface is down, enabling this interface...")
                commands = ["interface " + interface123, "no shutdown", "exit"]
                output123 = net_connect123.send_config_set(commands)
                print(output123)
            else:
                print("interface " + interface123 + " is already up")

    net_connect123.disconnect()

# SCRIPT 2 {ADVANCE}NETMIKO SCRIPT TO CONNECT “TERMINAL SERVER” FIRST AND THEN GOTO SSH CISCO_IOS

    import time
    from netmiko import ConnectHandler, redispatch
    from getpass import getpass
    net_connect = ConnectHandler(
        device_type="terminal_server",
        ip="192.168.32.131",
        username="network-automation",
        password="cisco",
    )

    output = net_connect.send_command("ifconfig")
    print(output)

    IP = [" 192.168.32.132", " 192.168.32.133"]

    for x in IP:
        username123 = input("enter your username for device" + x + ":")
        net_connect.write_channel("ssh -l " + username123 + x + "\r\n")
        time.sleep(1)

        max_loops = 4
        i = 1
        while i <= max_loops:
            output = net_connect.read_channel()

            if "Password" in output:
                print("Connecting to device" + x)
                net_connect.write_channel(getpass() + "\r\n")
                time.sleep(0.5)
                output = net_connect.read_channel()
                if ">" in output or "#" in output:
                    break
            time.sleep(0.5)
            i += 1
        redispatch(net_connect, device_type="cisco_ios")
        new_output = net_connect.send_command("show ip int brief")
        print(new_output)
