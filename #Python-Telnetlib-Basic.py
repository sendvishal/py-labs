# telnetlib basic script
import getpass
import telnetlib

HOST = “192.168.32.200”
user = “admin”
password = “cisco”

tn = telnetlib.Telnet(HOST)

tn.read_until(b”Username: “)
tn.write(user.encode(“ascii”) + b”\n”)
tn.read_until(b”Password: “)
tn.write(password.encode(“ascii”) + b”\n”)
# successful telnet connection

tn.write(b”terminal length 0\n”)
tn.write(b”show version\n”)

print(tn.read_all().decode(‘ascii’))

# Variant1 of  Telnetlib script


tnoctbatch = telnetlib.Telnet(b"192.168.32.200")

tnoctbatch.read_until(b"Username: ")
tnoctbatch.write(b"admin" + b"\n")
tnoctbatch.read_until(b"Password: ")
tnoctbatch.write(b"cisco" + b"\n")
# telnet established
tnoctbatch.write(b"show clock\n")

print(tnoctbatch.read_all().decode("utf8"))

# Variant 2 of Telnetlib script


HOST = "192.168.32.200"
user = "admin"
password = "cisco"

tnoctbatch = telnetlib.Telnet(HOST)

tnoctbatch.read_until(b"Username: ")
tnoctbatch.write(user.encode("utf8") + b"\n")
tnoctbatch.read_until(b"Password: ")
tnoctbatch.write(password.encode("utf8") + b"\n")
# telnet established
tnoctbatch.write(b"show clock\n")

print(tnoctbatch.read_all().decode("utf8"))


# Variant 3 of Telnetlib script, keeping empty () bydefault considers it to be “utf8” encoding


HOST = "192.168.32.200"
user = "admin"
password = "cisco"

tnoctbatch = telnetlib.Telnet(HOST)

tnoctbatch.read_until(b"Username: ")
tnoctbatch.write(user.encode() + b"\n")
tnoctbatch.read_until(b"Password: ")
tnoctbatch.write(password.encode() + b"\n")
# telnet established
tnoctbatch.write(b"show clock\n")

print(tnoctbatch.read_all().decode())

# Variant 4 Telnetlib script, encoding UTF-8 and UTF8 are the same


HOST = "192.168.32.200"
user = "admin"
password = "cisco"

tnoctbatch = telnetlib.Telnet(HOST)

tnoctbatch.read_until(b"Username: ")
tnoctbatch.write(user.encode("utf-8") + b"\n")
tnoctbatch.read_until(b"Password: ")
tnoctbatch.write(password.encode("utf-8") + b"\n")
# telnet established
tnoctbatch.write(b"show clock\n")

print(tnoctbatch.read_all().decode("utf-8"))

# Variant 5 of Telnetlib script, “ascii” is older encoding mechanism. Preferrable is “utf-8”


HOST = "192.168.32.200"
user = "admin"
password = "cisco"

tnoctbatch = telnetlib.Telnet(HOST)

tnoctbatch.read_until(b"Username: ")
tnoctbatch.write(user.encode("ascii") + b"\n")
tnoctbatch.read_until(b"Password: ")
tnoctbatch.write(password.encode("ascii") + b"\n")
# telnet established
tnoctbatch.write(b"show clock\n")

print(tnoctbatch.read_all().decode("ascii"))

# Script 1 Telnet Script to configure “OSPF” “LOOPBACK” || Password “INCLUDED” within Script


HOST = "192.168.32.200"
user = "admin"
password = "cisco"

tnoctbatch = telnetlib.Telnet(HOST)  # to open telnet connection

tnoctbatch.read_until(b"Username: ")
tnoctbatch.write(user.encode('utf8') + b"\n")
tnoctbatch.read_until(b"Password: ")
tnoctbatch.write(password.encode('utf8') + b"\n")

tnoctbatch.write(b"enable\n")  # \n represents end of line
tnoctbatch.write(b"cisco\n")
tnoctbatch.write(b"term len 0\n")
tnoctbatch.write(b"sh run\n")
tnoctbatch.write(b"conf t\n")
tnoctbatch.write(b"int loop 0\n")
tnoctbatch.write(b"ip address 1.1.1.1 255.255.255.255\n")
tnoctbatch.write(b"int loop 1\n")
tnoctbatch.write(b"ip address 2.2.2.2 255.255.255.255\n")
tnoctbatch.write(b"router ospf 1\n")
tnoctbatch.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
tnoctbatch.write(b"end\n")
tnoctbatch.write(b"exit\n")  # to close the connection

print(tnoctbatch.read_all().decode('utf8'))

# Script 2 Telnet Script to configure “OSPF” “LOOPBACK” || Password “EXCLUDED”


HOST = "172.16.221.106"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tnoctbatch = telnetlib.Telnet(HOST)  # to open telnet connection

tnoctbatch.read_until(b"Username: ")
tnoctbatch.write(user.encode('utf8') + b"\n")
tnoctbatch.read_until(b"Password: ")
tnoctbatch.write(password.encode('utf8') + b"\n")

tnoctbatch.write(b"enable\n")  # \n represents end of line
tnoctbatch.write(b"cisco\n")
tnoctbatch.write(b"term len 0\n")
tnoctbatch.write(b"sh run\n")
tnoctbatch.write(b"conf t\n")
tnoctbatch.write(b"int loop 0\n")
tnoctbatch.write(b"ip address 1.1.1.1 255.255.255.255\n")
tnoctbatch.write(b"int loop 1\n")
tnoctbatch.write(b"ip address 2.2.2.2 255.255.255.255\n")
tnoctbatch.write(b"router ospf 1\n")
tnoctbatch.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
tnoctbatch.write(b"end\n")
tnoctbatch.write(b"exit\n")  # to close the connection

print(tnoctbatch.read_all().decode('utf8'))

# Script 3 Telnet Script to configure “OSPF” “LOOPBACK” || Password “EXCLUDED” || SAVE BACKUP in DEFAULT “.TXT”


HOST = "192.168.32.200"
user = "admin"
password = "cisco"

tnoctbatch = telnetlib.Telnet(HOST)

tnoctbatch.read_until(b"Username: ")
tnoctbatch.write(user.encode("utf8") + b"\n")
tnoctbatch.read_until(b"Password:")
tnoctbatch.write(password.encode("utf8") + b"\n")

tnoctbatch.write(b"conf t\n")
tnoctbatch.write(b"hostnoctbatchame SWITCH-PYTHON\n")
tnoctbatch.write(b"exit\n")
tnoctbatch.write(b"terminal length 0\n")
tnoctbatch.write(b"show run\n")
tnoctbatch.write(b"exit\n")

# Save method
backup123 = tnoctbatch.read_all().decode("utf8")
opennotepad123 = open("backup_config_of_" + HOST + ".txt", "w")
opennotepad123.write(str(backup123))
# closes the opened file. A closed file cannot be read or written any more.
opennotepad123.close()
tnoctbatch.close()

# Script 4 Telnet Script to save “BACKUP” in Customized Location


HOST = "192.168.32.167"
user = input("Enter your telnet: ")
password = getpass.getpass()

tnoctbatch = telnetlib.Telnet(HOST)

tnoctbatch.read_until(b"Username: ")
tnoctbatch.write(user.encode('utf8') + b"\n")
tnoctbatch.read_until(b"Password: ")
tnoctbatch.write(password.encode('utf8') + b"\n")
tnoctbatch.write(b"show ip int br\n")
tnoctbatch.write(b"show ip prot summ\n")
tnoctbatch.write(b"show run | sec vty\n")
tnoctbatch.write(b"show run | sec hostnoctbatchame\n")

# save output
backup123 = tnoctbatch.read_all().decode("utf8")
filepath123 = "/Users/vishalgajjar/Downloads/Test"  # path used as string
#device_name = filepath123.decode("utf8")
opennotepad123 = open(filepath123 + HOST + ".txt", "w")
opennotepad123.write(backup123)
opennotepad123.close()
print(backup123)

tnoctbatch.close()

ADDON:
    # save output
    backup123 = tnoctbatch.read_all().decode("utf8")
    filepath123 = b"/Users/vishalgajjar/Downloads/Test"
    device_name = filepath123.decode("utf8")
    opennotepad123 = open(filepath123 + HOST + ".txt", "w")
    opennotepad123.write(backup123)
    opennotepad123.close()
    print(backup123)

    tnoctbatch.close()
