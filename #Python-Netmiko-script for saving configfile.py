 # SCRIPT  1 || NETMIKO SCRIPT TO SAVE “BACKUP” USING HOSTNAME

  from netmiko import ConnectHandler
   with open('devices.txt') as f:
        devices = f.read().splitlines()

    for ip in devices:
        cisco_device = {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': 'admin',
            'password': 'cisco',
                'port': 22,
                'secret': 'cisco',
                'verbose': True
        }
        print('Connecting to ' + ip)
        connection = ConnectHandler(**cisco_device)

        print('Entering enable mode ...')
        connection.enable()

        output = connection.send_command('show run')
        print(output)

        prompt = connection.find_prompt()
        # print(prompt)
        hostname = prompt[:-1]
        # print(hostname)

        list = output.split('\n')
        list = list[3:]
        config = '\n'.join(list)
        # print(config)
        import datetime
        now = datetime.datetime.now()
        today = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
        file = today + '-' + hostname + '.txt'

        with open(file, 'w') as backup:
            backup.write(config)
            print('Backup of ' + hostname + ' completed successfully')
            # print('#' * 30)

        connection.disconnect()

    create devices.txt
    192.168.32.132
    192.168.32.133

    # SCRIPT  2 || NETMIKO SCRIPT FOR LINUX OS

    from netmiko import ConnectHandler

    linux123 = {
        'device_type': 'linux',
        'ip': '192.168.32.169',
        'username': 'network-automation',
        ƒexpˀ        'port': 22,
        'secret': 'cisco',  # sudo password
            'verbose': True
    }
    # linux123 here called as dictionary
    connection123 = ConnectHandler(**linux123)

    connection123.enable()
    output123 = connection123.send_command(
        "sudo apt-get update && apt-get -y install apache10")
    # output123 = connection123.send_command("sudo useradd -m -d /home/user33 -s /bin/bash user33")
    # output123 = connection123.send_command("cat /etc/passwd")

    print(output123)

    connection123.disconnect()

    Validations:
    For package installation:
    sudo su
    dpkg - -get-selections | grep apache10

    # SCRIPT  3 || NETMIKO SCRIPT TO ENABLE “LOGGING”

    from netmiko import ConnectHandler  # connecthandler = functions
    import logging
    logging.basicConfig(filename='test.log', level=logging.DEBUG)
    logger = logging.getLogger("netmiko")

    cisco_device123 = {  # cisco_devices = called as classes
        'device_type': 'cisco_ios',
        'ip': '192.168.32.200',
        'username': 'admin',
        'password': 'cisco',
            'port': 22,
            'secret': 'cisco',
            'verbose': True
    }

    connection123 = ConnectHandler(**cisco_device123)
    output123 = connection123.send_command('show ip int br')
    print(output123)
