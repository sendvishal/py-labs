# Telnet for Arista switch, ASA firewall

import telnetlib  # calling python module telnetlib

HOST = "192.168.32.238"  # defining ip address on arista switch
user123 = "network"  # username of your arista switch
password123 = "automation"  # password of your arista switch

tnoctbatch = telnetlib.Telnet(HOST)  # taking telnet connection

tnoctbatch.read_until(b"Username: ")
tnoctbatch.write(user123.encode() + b"\n")
tnoctbatch.read_until(b"Password: ")
tnoctbatch.write(password123.encode() + b"\n")

tnoctbatch.write(b"enable\n")
tnoctbatch.write(b"show run\n")  # sending arista switch cli command

print(tnoctbatch.read_all().decode())  # getting output on pycharm console

Script 2: Telnet for Cisco ASA Firewall

# ciscoasa(config)#
# interface GigabitEthernet0/0
# nameif INSIDE
# security-level 100
# ip address dhcp
# no shutdown
# username network password automation privilege 15
# aaa authentication telnet console LOCAL
# telnet 0.0.0.0 0.0.0.0 INSIDE
# telnet timeout 1

------------------
1st method:
    ------------------
    import telnetlib  # calling python module telnetlib
    import time  # calling time module

    HOST = "192.168.32.251"  # defining ip address on cisco asa firewall
    user123 = "network"  # username of your asa firewall
    password123 = "automation"  # password of your asa firewall

    tnoctbatch = telnetlib.Telnet(HOST)  # taking telnet connection

    tnoctbatch.read_until(b"Username: ")
    tnoctbatch.write(user123.encode() + b"\n")
    tnoctbatch.read_until(b"Password: ")
    tnoctbatch.write(password123.encode() + b"\n")

    tnoctbatch.write(b"enable\n")  # sending cisco asa cli command
    time.sleep(1)  # Wait for 1 seconds between commands.
    tnoctbatch.write(b"\n")
    time.sleep(1)
    tnoctbatch.write(b"terminal page 0\n")
    time.sleep(1)
    tnoctbatch.write(b"show run\n")
    time.sleep(1)

    # getting output on pycharm console
    print(tnoctbatch.read_very_eager().decode())

    ------------------
    2nd way(optional)
    ------------------
    import telnetlib  # calling python module telnetlib
    HOST = "192.168.32.251"  # defining ip address on cisco asa firewall
    user123 = "network"  # username of your asa firewall
    password123 = "automation"  # password of your asa firewall

    tnoctbatch = telnetlib.Telnet(HOST)  # taking telnet connection

    tnoctbatch.read_until(b"Username: ")
    tnoctbatch.write(user123.encode() + b"\n")
    tnoctbatch.read_until(b"Password: ")
    tnoctbatch.write(password123.encode() + b"\n")

    tnoctbatch.write(b"enable\n")  # sending cisco asa cli command
    tnoctbatch.write(b"\n")
    tnoctbatch.write(b"terminal page 0\n")
    tnoctbatch.write(b"show run\n")
    tnoctbatch.write(b"exit")  # define
    print(tnoctbatch.read_until(b"exit").decode("ascii"))
