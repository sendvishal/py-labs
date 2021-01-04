# Telnet strip()
import time
import telnetlib
import getpass
Script 1: Configure Vlans(using “for” loops) on Multiple Switches(using “for” loops)


for manyvlans in range(106, 109):
    print("Telnet to 172.16.221." + str(manyvlans))
    HOST = "172.16.221." + str(manyvlans)

    user = input("Enter your telnet username: ")
    password = getpass.getpass()

     tnoctbatch = telnetlib.Telnet(HOST)

      tnoctbatch.read_until(b"Username: ")
       tnoctbatch.write(user.encode('ascii') + b"\n")
        tnoctbatch.read_until(b"Password: ")
         tnoctbatch.write(password.encode('ascii') + b"\n")

          tnoctbatch.write(b"conf t\n")
           for n in range(2, 30):
                tnoctbatch.write(b"vlan " + str(n).encode('ascii') + b"\n")
                tnoctbatch.write(b"name Python_VLAN " +
                                 str(n).encode('ascii') + b"\n")

            tnoctbatch.write(b"end\n")
            tnoctbatch.write(b"wr\n")
            tnoctbatch.write(b"exit\n")

            print(tnoctbatch.read_all().decode('ascii'))

# Script 2: Configure Vlans(using “for” loops) on Multiple Switches(device lists on seperate text file) and Save the output(customized File path)

user = input("Enter your telnet username: ")
password = getpass.getpass()
externaldevices = open("PRODSWITCHES ")
for IP in externaldevices:
    IP = IP.strip()
    print("configuring switch " + (IP))
    tnoctbatch = telnetlib.Telnet(IP)
    tnoctbatch.read_until(b"Username: ")
    tnoctbatch.write(user.encode('ascii') + b"\n")
     tnoctbatch.read_until(b"Password: ")
      tnoctbatch.write(password.encode('ascii') + b"\n")
       tnoctbatch.write(b"conf t\n")

        for n in range(2, 30):
            tnoctbatch.write(b"vlan " + str(n).encode('ascii') + b"\n")
            tnoctbatch.write(b"name Python_VLAN " +
                             str(n).encode('ascii') + b"\n")

        tnoctbatch.write(b"end\n")
        tnoctbatch.write(b"wr\n")
        tnoctbatch.write(b"exit\n")

        # save the output
        readoutput = tnoctbatch.read_all().decode("ascii")
        filepath = b"C:\Users\Sagar\Downloads\OUTPUT\New_Vlan_"
        device_name = filepath.decode("ascii")
        opennotepad123 = open(device_name + IP + ".txt", "w")
        opennotepad123.write(str(readoutput))
        print(readoutput)
        opennotepad123.close()
        tnoctbatch.close()

# Script 3: Save Backup(default path) for Multiple Switches(device lists on seperate text file)

user = input("Enter your telnet username: ")
password = getpass.getpass()
externaldevices = open("PRODSWITCHES ")
for line in externaldevices:
    HOST = line.strip()
    print("Getting running config from devices " + line)
    # 23 for telnet port, 5 for socket
    tnoctbatch = telnetlib.Telnet(HOST, 23, 5)
    tnoctbatch.read_until(b"Username:")
     tnoctbatch.write(user.encode("ascii") + b"\n")
      tnoctbatch.read_until(b"Password:")
       tnoctbatch.write(password.encode("ascii") + b"\n")

        tnoctbatch.write(b"conf t\n")
        time.sleep(1)
        tnoctbatch.write(b"hostname Router3725\n")
        time.sleep(1)
        tnoctbatch.write(b"exit\n")
        time.sleep(1)
        tnoctbatch.write(b"terminal length 0\n")
        time.sleep(1)
        tnoctbatch.write(b"show run\n")
        time.sleep(1)
        tnoctbatch.write(b"exit\n")

        readoutput = tnoctbatch.read_all().decode("ascii")
        opennotepad123 = open("device_" + HOST + ".txt", "w")
        opennotepad123.write(readoutput)
        print(readoutput)
        opennotepad123.close()
