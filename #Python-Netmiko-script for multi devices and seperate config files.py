
 # SCRIPT 1 (VARIANT_A) || NETMIKO SCRIPT “RUN MULTIPLE CLI COMMANDS” FROM “MULTIPLE CONFIG FILES” ON “MULTIPLE DEVICES”
 (using splitlines and .append)

  from netmiko import ConnectHandler

   with open('devices.txt') as f123:
        devices = f123.read().splitlines()
        # print(devices)
    device_list = list()
    # print(device_list)
    for ip in devices:
        cisco_device = {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': 'admin',
                'password': 'cisco',
                'port': 22,
                'secret': 'cisco',  # this is the enable password
                'verbose': True
        }
        device_list.append(cisco_device)
    # print(device_list)

    for device in device_list:
        print('Connecting to ' + device['ip'])
        connection123 = ConnectHandler(**device)  # create connection object

        print('Entering enable mode ...')
        connection123.enable()

        file = input('Enter configuration file(use
                                               a valid path) for ' + device['ip'] +': ')  # enter the configuration file

        print('Running commands from file:', file, 'to device:', device['ip'])
        output = connection123.send_config_from_file(file)
        print(output)

        connection123.disconnect()

    # devices.txt
    # 192.168.32.200
    # 192.168.32.201
    # 192.168.32.202

    # SW1.txt
    # int loopback 0
    # ip add 1.1.1.1 255.255.255.255
    # exit
    # router ospf 1
    # network 0.0.0.0 0.0.0.0 area 0
    # router-id 10.1.1.1

    # SW2.txt
    # int loopback 0
    # ip add 1.1.1.1 255.255.255.255
    # exit
    # router ospf 1
    # network 0.0.0.0 0.0.0.0 area 0
    # router-id 10.1.1.1

    # SW3.txt
    # int loopback 0
    # ip add 1.1.1.1 255.255.255.255
    # exit
    # router ospf 1
    # network 0.0.0.0 0.0.0.0 area 0
    # router-id 10.1.1.1

    # SCRIPT 1 (VARIANT_B) || NETMIKO SCRIPT “RUN MULTIPLE CLI COMMANDS” FROM “MULTIPLE CONFIG FILES” ON “MULTIPLE DEVICES”
    (without using splitlines and .append)

    from netmiko import ConnectHandler

    device_list = open("coredevices.txt")

    for device in device_list:
        cisco_device = {
            'device_type': 'cisco_ios',
            'ip': device,
            'username': 'admin',
            'password': 'cisco',
            'port': 22,
        }
        print('Connecting to ' + device)
        connection123 = ConnectHandler(**cisco_device)

        print('Entering enable mode ...')
        connection123.enable()

        file = input('Enter configuration file for ' + device + ':')

        output = connection123.send_config_from_file(file)
        print(output)

        connection123.disconnect()

    # devices.txt
    # 192.168.32.200
    # 192.168.32.201
    # 192.168.32.202

    # SW1.txt
    # int loopback 0
    # ip add 1.1.1.1 255.255.255.255
    # exit
    # router ospf 1
    # network 0.0.0.0 0.0.0.0 area 0
    # router-id 10.1.1.1

    # SW2.txt
    # int loopback 0
    # ip add 1.1.1.1 255.255.255.255
    # exit
    # router ospf 1
    # network 0.0.0.0 0.0.0.0 area 0
    # router-id 10.1.1.1

    # SW3.txt
    # int loopback 0
    # ip add 1.1.1.1 255.255.255.255
    # exit
    # router ospf 1
    # network 0.0.0.0 0.0.0.0 area 0
    # router-id 10.1.1.1
