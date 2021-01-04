

#SCRIPT#1 || NAPALM COMMIT CHANGE (NO CONFIRMATION REQUIRED)

    from napalm import get_network_driver
    import json

    driver = get_network_driver('ios')
    optional_args123 = {"secret":"cisco"}
    ios123 = driver('192.168.32.200', 'admin', 'cisco', optional_args=optional_args123)
    ios123.open()

    #start script
    ios123.load_replace_candidate(filename="config.txt") #replacing the config
    diff = ios123.compare_config()

    if len(diff):
        print(diff)
        print("Commit changes...")
        ios123.commit_config()
        print("done")
    else:
        print("NO CHANGE REQURIED")
        ios123.discard_config()

    answer = input("do you want to rollback?")
    if answer == "yes":
        ios123.rollback()
    else:
        print("No rollback required")

    ios123.close()

    # create new config.txt

    # !
    # ! Last configuration change at 16:21:59 UTC Sun Apr 26 2020 by admin
    # !
    # version 15.2
    # service timestamps debug datetime msec
    # service timestamps log datetime msec
    # no service password-encryption
    # service compress-config
    # !
    # hostname SW01
    # !
    # boot-start-marker
    # boot-end-marker
    # !
    # !
    # !
    # username admin privilege 15 password 0 cisco
    # username user4 secret 5 $1$HtZQ$SYdCK7ZBFFfgs0v.dng7n1
    # no aaa new-model
    # !
    # !
    # !
    # !
    # !
    # !
    # !
    # !
    # ip domain-name xyz.com
    # ip cef
    # no ipv6 cef
    # !
    # !
    # file prompt quiet
    # archive
    # path flash:archive
    # !
    # spanning-tree mode pvst
    # spanning-tree extend system-id
    # !
    # vlan internal allocation policy ascending
    # !
    # !
    # !
    # !
    # !
    # !
    # !
    # !
    # !
    # !
    # !
    # !
    # !
    # !
    # interface Loopback10
    # ip address 7.7.7.70 255.255.255.255
    # !
    # interface Loopback1
    # ip address 7.7.7.7 255.255.255.255
    # !
    # interface GigabitEthernet0/0
    # media-type rj45
    # negotiation auto
    # !
    # interface GigabitEthernet0/1
    # media-type rj45
    # negotiation auto
    # !
    # interface GigabitEthernet0/2
    # media-type rj45
    # negotiation auto
    # !
    # interface GigabitEthernet0/3
    # media-type rj45
    # negotiation auto
    # !
    # interface GigabitEthernet1/0
    # media-type rj45
    # negotiation auto
    # !
    # interface GigabitEthernet1/1
    # media-type rj45
    # negotiation auto
    # !
    # interface GigabitEthernet1/2
    # media-type rj45
    # negotiation auto
    # !
    # interface GigabitEthernet1/3
    # media-type rj45
    # negotiation auto
    # !
    # interface GigabitEthernet2/0
    # media-type rj45
    # negotiation auto
    # !
    # interface GigabitEthernet2/1
    # media-type rj45
    # negotiation auto
    # !
    # interface GigabitEthernet2/2
    # media-type rj45
    # negotiation auto
    # !
    # interface GigabitEthernet2/3
    # media-type rj45
    # negotiation auto
    # !
    # interface GigabitEthernet3/0
    # media-type rj45
    # negotiation auto
    # !
    # interface GigabitEthernet3/1
    # media-type rj45
    # negotiation auto
    # !
    # interface GigabitEthernet3/2
    # media-type rj45
    # negotiation auto
    # !
    # interface GigabitEthernet3/3
    # media-type rj45
    # negotiation auto
    # !
    # interface Vlan1
    # ip address 192.168.32.200 255.255.255.0
    # !
    # ip forward-protocol nd
    # !
    # no ip http server
    # no ip http secure-server
    # !
    # ip scp server enable
    # !
    # !
    # !
    # !
    # !
    # control-plane
    # !
    # line con 0
    # line aux 0
    # line vty 0 4
    # exec-timeout 0 10
    # login local
    # transport input all
    # !
    # !
    # end

    # #Enable Archive
    # cisco(conft)#
    # archive:
    # path flash:archive
    # write memory

#SCRIPT 2 || NAPALM MERGE CHANGE

    from napalm import get_network_driver

    driver = get_network_driver('ios')

    optional_args = {'secret': 'cisco'} #cisco is the enable password
    ios = driver('192.168.32.201', 'admin', 'cisco', optional_args=optional_args)
    ios.open()

    ios.load_merge_candidate('config.txt')

    diff = ios.compare_config()

    if len(diff) > 0:
        print(diff)
        answer = input('Commit changes?')
        if answer == 'yes':
            print('Commit changes...')
            ios.commit_config()
            print('Done')
        else:
            print('No changes required')
            ios.discard_config()

    ios.close()

    create config.txt
    logging host 2.2.2.2

#SCRIPT 3 || NAPALM MERGE CHANGE & IT PROMPTS FOR COMMIT OR NOT

    from napalm import get_network_driver

    driver = get_network_driver('ios')

    optional_args = {'secret': 'cisco'} #cisco is the enable password
    ios = driver('192.168.32.201', 'admin', 'cisco', optional_args=optional_args)
    ios.open()

    ios.load_merge_candidate('config.txt')

    diff = ios.compare_config()

    if len(diff) > 0:
        print(diff)
        answer = input('Commit changes?')
        if answer == 'yes':
            print('Commit changes...')
            ios.commit_config()
            print('Done')
        else:
            print('No changes required')
            ios.discard_config()

    ios.close()

    create config.txt
    logging host 2.2.2.2

#SCRIPT 3 || NAPALM MERGE CHANGE & IT PROMPTS FOR COMMIT OR NOT & ALSO ADDS ROLLBACK FEATURE

    from napalm import get_network_driver

    driver = get_network_driver('ios')

    optional_args = {'secret': 'cisco'} #cisco is the enable password
    ios123 = driver('192.168.32.132', 'admin', 'cisco', optional_args=optional_args)
    ios123.open()

    ios123.load_merge_candidate('config.txt')

    diff = ios123.compare_config()

    if len(diff) > 0:
        print(diff)
        answer = input('Commit changes?')
        if answer == 'yes':
            print('Commit changes...')
            ios123.commit_config()
            print('Done')
        else:
            print('No changes required')
            ios123.discard_config()

    answer = input('Rollback?')
    if answer == 'yes':
        print('Rolling back..')
        ios123.rollback()
        print('Done')

    ios123.close()

    create config.txt
    logging host 2.2.2.2
