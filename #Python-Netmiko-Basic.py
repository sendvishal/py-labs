
# SCRIPT  1 BASIC NETMIKO SCRIPT WITHOUT “CONNECTHANDLER”
from netmiko import ConnectHandler  # connecthandler = functions
from netmiko import Netmiko


net_connect = Netmiko(host="192.168.32.200", username="admin",
                      password="cisco", device_type="cisco_ios")

output = net_connect.send_command("show ip int brief")
print(output)

net_connect.disconnect()

# SCRIPT  2 NETMIKO SCRIPT USING “CONNECTHANDLER”


# connection = Netmiko(host='10.1.1.1', username='admin', password='cisco', device_type='cisco_ios')
cisco_device = {  # cisco_devices = called as classes in the format of python_dictionary
    'device_type': 'cisco_ios',
    'ip': '192.168.32.200',
    'username': 'admin',
    'password': 'cisco',
    'port': 22,
    'secret': 'cisco',
    'verbose': True
}

# connection = variable object, ** = is used to call dictionary inside function
connection = ConnectHandler(**cisco_device)
output = connection.send_command('show run')
print(output)

# SCRIPT  3  NETMIKO SCRIPT USING “CONNECTHANDLER” FOR HANDLING ADDITIONAL “PROMPTING”


# connection = Netmiko(host='10.1.1.1', username='admin', password='cisco', device_type='cisco_ios')
cisco_device = {  # cisco_devices = called as classes
    'device_type': 'cisco_ios',
    'ip': '192.168.32.200',
     'username': 'admin',
    'password': 'cisco',
        'port': 22,
        'secret': 'cisco123',  # no username admin pri 15  // # enable secret cisco123
        'verbose': True,
    }

# connection123 = object, ** = dictionary used to call function
connection123 = ConnectHandler(**cisco_device)

 prompt = connection123.find_prompt()
  print(prompt)
   if '>' in prompt:
        connection123.enable()
    # mode = connection123.check_enable_mode()
    # print(mode)
    output = connection123.send_command('show ip int br')
    print(output)

    mode = connection123.check_config_mode()
    # print(mode)
    if not mode:
        connection123.config_mode()
    # mode = connection123.check_config_mode()
    # print(mode)
    output = connection123.send_command('username joy password python123')
    output = connection123.send_command('do show run | i user')
    print(output)
