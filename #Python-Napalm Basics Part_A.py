# SCRIPT 1 || BASIC NAPALM SCRIPT

from napalm import get_network_driver

driver = get_network_driver('ios')

# optional_args123 = {'secret': 'cisco'} #cisco is the enable password #dictionary
ios123 = driver('192.168.32.200', 'admin123', 'cisco',
                optional_args=optional_args123)
ios123.open()

print(dir(ios123))

ios123.close()

# SCRIPT 2 || NAPALM TO TAKE “SHOW RUN” / “GATHER INFORMATION”

#import json

driver123 = get_network_driver('ios')

optional_args123 = {'secret': 'cisco'}
ios123 = driver123('192.168.32.200', 'admin', 'cisco',
                    optional_args=optional_args123)
 ios123.open()

  # start your code here
  output123 = ios123.get_arp_table()
   for result123 in output123:
        print(result123)
    # stop your code here

    # dump123 = json.dumps(output123, sort_keys=True, indent=4) #arguments
    # print(dump123)

    # with open('arp.txt', 'w') as f:
        # f.write(dump123)

    ios123.close()

# SCRIPT 3 || NAPALM RETRIEVING INFORMATION (FACTS, INTERFACE, ARP TABLE)

    from napalm import get_network_driver
    import json

    driver = get_network_driver('ios')
    optional_args123 = {'secret': 'cisco'}
    ios123 = driver('192.168.32.200', 'admin', 'cisco',
                    optional_args=optional_args123)
    ios123.open()

    output123 = ios123.get_facts()

    #output123 = ios123.get_arp_table()
    #output123 = ios123.get_interfaces_counters()
    #output123 = ios123.get_interfaces()

    #output123 = ios123.get_users()
    dump123 = json.dumps(output123, sort_keys=True, indent=4)  # arguments
    print(dump123)

    ios123.close()

# SCRIPT 4 || NAPALM “CONNECTIVITY” TEST USING “PING”

    from napalm import get_network_driver
    import json

    driver = get_network_driver('ios')
    optional_args123 = {'secret': 'cisco'}
    ios123 = driver('192.168.32.200', 'admin', 'cisco',
                    optional_args=optional_args123)
    ios123.open()
    # start code
    output123 = ios123.ping(destination="192.168.32.1",
                            count=10, source="192.168.32.200")
    dump123 = json.dumps(output123, sort_keys=True, indent=4)
    print(dump123)

    ios123.close()
