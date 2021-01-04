

# SCRIPT1  NETMIKO SCRIPT FOR ENABLE “ADMIN DOWN” INTERFACES

from netmiko import ConnectHandler

cisco_device123 = {
     'device_type': 'cisco_ios',
     'ip': '192.168.32.200',
      'username': 'admin',
     'password': 'cisco',
            'port': 22,  # optional, default 22
            'secret': 'cisco',  # optional, default ''
            'verbose': True  # optional, default False
     }

 net_connect123 = ConnectHandler(**cisco_device123)
  prompter = net_connect123.find_prompt()
   if '>' in prompter:
        net_connect123.enable()

    interface = input('Enter the enterface you want to enable:')
    # check the interface status
    output123 = net_connect123.send_command('sh ip interface ' + interface)

    # if an invalid interface has been entered
    if 'Invalid input detected' in output123:
        print('You entered and invalid interface')
    else:
        # 1st line of the sh ip interface command output
        first_line = output123.splitlines()[0]
        print(first_line)
        if not 'up' in first_line:  # if the interface is not up
            print('The interface is down. Enabling the interface ...')
            commands = ['interface ' + interface,
                        'no shut', 'exit']  # enabling the interface
            output123 = net_connect123.send_config_set(commands)
            print(output123)
            print('#' * 40)
            print('The interface has been enabled')
        else:  # if the interface is already enabled
            print('Interface ' + interface + ' is already enabled')

    net_connect123.disconnect()

# SCRIPT 2  BASIC NETMIKO SCRIPT FOR “PROMPT”

    from netmiko import Netmiko
    from getpass import getpass

    net_connect = Netmiko(
        "192.168.32.132",
        username="admin",
        password=getpass(),
        device_type="cisco_ios",
    )

    print(net_connect.find_prompt())

# SCRIPT 3 NETMIKO SCRIPT TO CONNECT “TERMINAL SERVER” FIRST AND THEN GOTO SSH CISCO_IOS

    import time
    from netmiko import ConnectHandler, redispatch

    net_connect = ConnectHandler(
        device_type="terminal_server",
        ip="192.168.32.131",
        username="network-automation",
        password="cisco",
    )

    output = net_connect.send_command("ifconfig")
    print(output)

    net_connect.write_channel("ssh -l admin 192.168.32.132\r\n")
    time.sleep(1)

    max_loops = 10
    i = 5
    while i <= max_loops:
        output = net_connect.read_channel()

        if "Password" in output:
            net_connect.write_channel(net_connect.password + "\r\n")
            time.sleep(0.5)
            output = net_connect.read_channel()
            if ">" in output or "#" in output:
                break
        time.sleep(0.5)
        i += 1

    redispatch(net_connect, device_type="cisco_ios")

    new_output = net_connect.send_command("show ip int brief")
    print(new_output)
