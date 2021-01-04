
from datetime import datetime
import threading
from getpass import getpass
from netmiko import Netmiko
from netmiko.snmp_autodetect import SNMPDetect
# SCRIPT   1 || TO CHECK NETMIKO SNMP STRING V2C


device = {"host": "192.168.32.200",
          "username": "admin", "password": "cisco"}

snmp_community = getpass("Enter SNMP community: ")
my_snmp = SNMPDetect(
    "192.168.32.200", snmp_version="v2c", community=snmp_community)
device_type = my_snmp.autodetect()
print(device_type)
device["device_type"] = device_type

net_connect = Netmiko(**device)
print(net_connect.find_prompt())

# ”pysnmp” pycharm library

# SW01(config)#snmp-server community cisco123snmp

# SCRIPT  2 || TO CHECK SNMP V3


device = {"host": "192.168.32.200",
          "username": "admin", "password": "cisco"}

snmp_key = getpass("Enter SNMP community: ")

my_snmp = SNMPDetect(
    "192.168.32.200",
    snmp_version="v3",
    user="snmpuser123",
    auth_key=snmp_key,
    encrypt_key=snmp_key,
    auth_proto="sha",
    encrypt_proto="aes128",
)
device_type = my_snmp.autodetect()
print(device_type)

device["device_type"] = device_type
net_connect = Netmiko(**device)
print(net_connect.find_prompt())

# snmp-server group group3 v3 priv
# snmp-server user snmpuser123 group3 v3 auth sha cisco123snmp priv aes 128 cisco123snmp

# SCRIPT  3 || Netmiko Multiple Threading

 from netmiko import ConnectHandler
  from my_devices import device_list as devices

   def show_version(a_device):
        """Execute show version command using Netmiko."""
        remote_conn = ConnectHandler(**a_device)
        print()
        print("#" * 80)
        print(remote_conn.send_command_expect("show version"))
        print("#" * 80)
        print()

    def main():
        """
        Use threads and Netmiko to connect to each of the devices. Execute
        'show version' on each device. Record the amount of time required to do this.
        """
        start_time = datetime.now()

        for a_device in devices:
            my_thread = threading.Thread(target=show_version, args=(a_device,))
            my_thread.start()

        main_thread = threading.currentThread()
        for some_thread in threading.enumerate():
            if some_thread != main_thread:
                print(some_thread)
                some_thread.join()

        print("\nElapsed time: " + str(datetime.now() - start_time))

    if __name__ == "__main__":
        main()

    create my_devices.py
    oct_rtr1 = {“device_type”: “cisco_ios”,
                “ip”: “192.168.32.132”,
                “username”: “admin”,
                “password”: “cisco”
                }

    oct_rtr2 = {“device_type”: “cisco_ios”,
                “ip”: “192.168.32.133”,
                “username”: “admin”,
                “password”: “cisco”
                }

    oct_sw1 = {“device_type”: “cisco_ios”,
               “ip”: “192.168.32.138”,
               “username”: “admin”,
               “password”: “cisco”
               }

    oct_sw2 = {“device_type”: “cisco_ios”,
               “ip”: “192.168.32.139”,
               “username”: “admin”,
               “password”: “cisco”
               }

    oct_sw3 = {“device_type”: “cisco_ios”,
               “ip”: “192.168.32.140”,
               “username”: “admin”,
               “password”: “cisco”
               }

    oct_w4 = {“device_type”: “cisco_ios”,
              “ip”: “192.168.32.141”,
              “username”: “admin”,
              “password”: “cisco”
              }

    device_list = [
        oct_rtr1,
        oct_rtr2,
        oct_sw1,
        oct_sw2,
        oct_sw3,
        oct_sw4,
    ]

    # SCRIPT  4 || Netmiko Single Processing

    """
    Use processes and Netmiko to connect to each of the devices. Execute
    'show version' on each device. Use a queue to pass the output back to the parent process.
    Record the amount of time required to do this.
    """
    from multiprocessing import Process, Queue

    from datetime import datetime
    from netmiko import ConnectHandler
    from my_devices import device_list as devices

    def show_version_queue(a_device, output_q):
        """
        Use Netmiko to execute show version. Use a queue to pass the data back to
        the main process.
        """
        output_dict = {}
        remote_conn = ConnectHandler(**a_device)
        hostname = remote_conn.base_prompt
        output = ("#" * 80) + "\n"
        output += remote_conn.send_command("show ip int br | ex unass") + "\n"
        output += ("#" * 80) + "\n"
        output_dict[hostname] = output
        output_q.put(output_dict)

    def main():
        """
        Use processes and Netmiko to connect to each of the devices. Execute
        'show version' on each device. Use a queue to pass the output back to the parent process.
        Record the amount of time required to do this.
        """
        start_time = datetime.now()
        output_q = Queue(maxsize=20)

        procs = []
        for a_device in devices:
            my_proc = Process(target=show_version_queue,
                              args=(a_device, output_q))
            my_proc.start()
            procs.append(my_proc)

        # Make sure all processes have finished
        for a_proc in procs:
            a_proc.join()

        while not output_q.empty():
            my_dict = output_q.get()
            for k, val in my_dict.items():
                print(k)
                print(val)

        print("\nElapsed time: " + str(datetime.now() - start_time))

    if __name__ == "__main__":
        main()

    create my_devices.py
    oct_rtr1 = {“device_type”: “cisco_ios”,
                “ip”: “192.168.32.132”,
                “username”: “admin”,
                “password”: “cisco”
                }

    oct_rtr2 = {“device_type”: “cisco_ios”,
                “ip”: “192.168.32.133”,
                “username”: “admin”,
                “password”: “cisco”
                }

    oct_sw1 = {“device_type”: “cisco_ios”,
               “ip”: “192.168.32.138”,
               “username”: “admin”,
               “password”: “cisco”
               }

    oct_sw2 = {“device_type”: “cisco_ios”,
               “ip”: “192.168.32.139”,
               “username”: “admin”,
               “password”: “cisco”
               }

    oct_sw3 = {“device_type”: “cisco_ios”,
               “ip”: “192.168.32.140”,
               “username”: “admin”,
               “password”: “cisco”
               }

    oct_w4 = {“device_type”: “cisco_ios”,
              “ip”: “192.168.32.141”,
              “username”: “admin”,
              “password”: “cisco”
              }

    device_list = [
        oct_rtr1,
        oct_rtr2,
        oct_sw1,
        oct_sw2,
        oct_sw3,
        oct_sw4,
    ]

# SCRIPT  5 || Netmiko Multi Processing

    """
    Use processes and Netmiko to connect to each of the devices. Execute
    'show version' on each device. Record the amount of time required to do this.
    """
    from __future__ import print_function, unicode_literals
    from multiprocessing import Process

    from datetime import datetime
    from netmiko import ConnectHandler
    from my_devices import device_list as devices

    def show_version(a_device):
        """Execute show version command using Netmiko."""
        remote_conn = ConnectHandler(**a_device)
        print()
        print("#" * 80)
        print(remote_conn.send_command("show version"))
        print("#" * 80)
        print()

    def main():
        """
        Use processes and Netmiko to connect to each of the devices. Execute
        'show version' on each device. Record the amount of time required to do this.
        """
        start_time = datetime.now()

        procs = []
        for a_device in devices:
            my_proc = Process(target=show_version, args=(a_device,))
            my_proc.start()
            procs.append(my_proc)

        for a_proc in procs:
            print(a_proc)
            a_proc.join()

        print("\nElapsed time: " + str(datetime.now() - start_time))

    if __name__ == "__main__":
        main()

    create my_devices.py
    oct_rtr1 = {“device_type”: “cisco_ios”,
                “ip”: “192.168.32.132”,
                “username”: “admin”,
                “password”: “cisco”
                }

    oct_rtr2 = {“device_type”: “cisco_ios”,
                “ip”: “192.168.32.133”,
                “username”: “admin”,
                “password”: “cisco”
                }

    oct_sw1 = {“device_type”: “cisco_ios”,
               “ip”: “192.168.32.138”,
               “username”: “admin”,
               “password”: “cisco”
               }

    oct_sw2 = {“device_type”: “cisco_ios”,
               “ip”: “192.168.32.139”,
               “username”: “admin”,
               “password”: “cisco”
               }

    oct_sw3 = {“device_type”: “cisco_ios”,
               “ip”: “192.168.32.140”,
               “username”: “admin”,
               “password”: “cisco”
               }

    oct_w4 = {“device_type”: “cisco_ios”,
              “ip”: “192.168.32.141”,
              “username”: “admin”,
              “password”: “cisco”
              }

    device_list = [
        oct_rtr1,
        oct_rtr2,
        oct_sw1,
        oct_sw2,
        oct_sw3,
        oct_sw4,
    ]

# SCRIPT  6 || Netmiko Multi Threading to run “show arp”

    import time
    import concurrent.futures
    from netmiko import ConnectHandler

    hosts_info = []

    starting_time = time.perf_counter()

    with open('threadingdevices.txt', 'r') as devices:
        for line in devices:
            deviceip = line.strip()
            host = {
                'device_type': 'cisco_ios',
                'ip': deviceip,
                'username': 'admin',
                'password': 'cisco',
                'secret': 'cisco'
            }
            hosts_info.append(host)

    def open_connection(host):
        try:
            connection = ConnectHandler(**host)
            print('Connection Established to Host:', host['ip'])
            connection.enable()
            sendcommand = connection.send_command('sh arp')
            return sendcommand + ' ' + 'For Device:' + host['ip']
        except:
            print('Connection Failed to host', host['ip'])

    if __name__ == '__main__':
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = executor.map(open_connection, hosts_info)
            for result in results:
                print(result)

        finish = time.perf_counter()
        print('Time Elapsed:', finish - starting_time)

    create threadingdevices.txt
    192.168.32.132
    192.168.32.133
    192.168.32.138
    192.168.32.139
    192.168.32.140
    192.168.32.141
