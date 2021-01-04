 #Telnet for-loops
 
   # Script 1 Telnet Script to configure “VLANS” in CLI Commands

    import getpass
    import telnetlib

    HOST = "172.16.221.106"
    user = input("Enter your telnet username: ")
    password = getpass.getpass()

    tnoctbatch = telnetlib.Telnet(HOST)

    tnoctbatch.read_until(b"Username: ")
    tnoctbatch.write(user.encode('utf8') + b"\n")
    tnoctbatch.read_until(b"Password: ")
    tnoctbatch.write(password.encode('utf8') + b"\n")

    tnoctbatch.write(b"conf t\n")
    tnoctbatch.write(b"vlan 2\n")
    tnoctbatch.write(b"name Python_2\n")
    tnoctbatch.write(b"vlan 3\n")
    tnoctbatch.write(b"name Python_3\n")
    tnoctbatch.write(b"vlan 4\n")
    tnoctbatch.write(b"name Python_4\n")
    tnoctbatch.write(b"end\n")
    tnoctbatch.write(b"exit\n")

    print(tnoctbatch.read_all().decode('utf8'))

    #Script 2 Telnet Script to configure “VLANS” in “FOR LOOP”

    import getpass
    import telnetlib

    HOST = "172.16.221.106"
    user = input("Enter your telnet username: ")
    password = getpass.getpass()

    tnoctbatch = telnetlib.Telnet(HOST)

    tnoctbatch.read_until(b"Username: ")
    tnoctbatch.write(user.encode('utf8') + b"\n")
    tnoctbatch.read_until(b"Password: ")
    tnoctbatch.write(password.encode('utf8') + b"\n")

    tnoctbatch.write(b"conf t\n")
    for n in range (2,30):
        tnoctbatch.write(b"vlan " + str(n).encode('utf8') + b"\n")
        tnoctbatch.write(b"name Python_VLAN " + str(n).encode('utf8') + b"\n")

    tnoctbatch.write(b"end\n")
    tnoctbatch.write(b"wr\n")
    tnoctbatch.write(b"exit\n")

    print(tnoctbatch.read_all().decode('utf8'))

    #Script 3 Telnet Script to configure “VLANS” in “FOR LOOP” for Multiple Devices placed in LIST format

    import getpass
    import telnetlib

    user = input("Enter your telnet username: ")
    password = getpass.getpass()

    HOST = ["192.168.32.200", "192.168.32.201"]
    for multipledevices in HOST:
        print("Creating_Vlan_on " + multipledevices)
        tnoctbatch = telnetlib.Telnet(multipledevices)
        tnoctbatch.read_until(b"Username: ")
        tnoctbatch.write(user.encode('utf8') + b"\n")
        tnoctbatch.read_until(b"Password: ")
        tnoctbatch.write(password.encode('utf8') + b"\n")

        tnoctbatch.write(b"conf t\n")
        for n in range (2,30):
            tnoctbatch.write(b"vlan " + str(n).encode('utf8') + b"\n")
            tnoctbatch.write(b"name Python_VLAN " + str(n).encode('utf8') + b"\n")

        tnoctbatch.write(b"end\n")
        tnoctbatch.write(b"wr\n")
        tnoctbatch.write(b"exit\n")

        print(tnoctbatch.read_all().decode('utf8'))

#Script 4 Telnet Script to configure “VLANS” in “FOR LOOP” for Multiple Devices placed in LIST format with Same Username/Password on All Devices

import getpass
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass()

HOST = ["192.168.32.200", "192.168.32.201"]
for multipledevices in HOST:
    print("Creating_Vlan_on " + multipledevices)
    tnoctbatch = telnetlib.Telnet(multipledevices)
    tnoctbatch.read_until(b"Username: ")
    tnoctbatch.write(user.encode('utf8') + b"\n")
    tnoctbatch.read_until(b"Password: ")
    tnoctbatch.write(password.encode('utf8') + b"\n")

    tnoctbatch.write(b"conf t\n")
    for n in range (2,30):
        tnoctbatch.write(b"vlan " + str(n).encode('utf8') + b"\n")
        tnoctbatch.write(b"name Python_VLAN " + str(n).encode('utf8') + b"\n")

    tnoctbatch.write(b"end\n")
    tnoctbatch.write(b"wr\n")
    tnoctbatch.write(b"exit\n")

    print(tnoctbatch.read_all().decode('utf8'))

#Script 5 Telnet Script to configure “VLANS” in “FOR LOOP” for Multiple Devices placed in “FOR LOOP” with “Different” Username/Password

import getpass
import telnetlib

HOST = ["192.168.32.200", "192.168.32.201"]
for multipledevices in HOST:
    print("Creating_Vlan_on " + multipledevices)
    user = input("Enter your telnet username: ")
    password = getpass.getpass()
    tnoctbatch = telnetlib.Telnet(multipledevices)
    tnoctbatch.read_until(b"Username: ")
    tnoctbatch.write(user.encode('utf8') + b"\n")
    tnoctbatch.read_until(b"Password: ")
    tnoctbatch.write(password.encode('utf8') + b"\n")

    tnoctbatch.write(b"conf t\n")
    for manyvlans in range (2,30):
        tnoctbatch.write(b"vlan " + str(manyvlans).encode('utf8') + b"\n")
        tnoctbatch.write(b"name Python_VLAN " + str(manyvlans).encode('utf8') + b"\n")

    tnoctbatch.write(b"end\n")
    tnoctbatch.write(b"wr\n")
    tnoctbatch.write(b"exit\n")

    print(tnoctbatch.read_all().decode('utf8'))
