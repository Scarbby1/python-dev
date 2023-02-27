print("Задания 6.1-6.3")
#задание 6.1
mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
res = []
for l in mac:
    res.append(l.replace(':', '.'))
print(res)
#задание 6.2
ip = input("Введите IP: ")
ip_list = ip.split(".")
oct1, oct2, oct3, oct4 = [
    int(ip_list[0]),
    int(ip_list[1]),
    int(ip_list[2]),
    int(ip_list[3]),
]
if oct1 >= 1 and oct1 <223:
    print("unicast")
elif oct1 >=224 and oct1 <=239:
    print("multicast")
elif ip == '255.255.255.255':
    print("broadcast")
elif ip == '0.0.0.0':
    print("unassigned")
else:
    print("unused")

#задание6.2a
ip_good = True
ip = input("Введите IP: ")
ip_list = ip.split(".")
if len(ip_list) != 4:
    ip_good = False
for oct in ip_list:
    if not (oct.isdigit() and int(oct) in range(255)):
        ip_good = False

if not ip_good:
    print ("Неправильный IP")
else:
    oct1, oct2, oct3, oct4 = [
        int(ip_list[0]),
        int(ip_list[1]),
        int(ip_list[2]),
        int(ip_list[3]),
    ]
    if oct1 >= 1 and oct1 <= 223:
        print("unicast")
    elif oct1 >= 224 and oct1 <= 239:
        print("multicast")
    elif ip == '255.255.255.255':
        print("local broadcast")
    elif ip == '0.0.0.0':
        print("unassigned")
    else:
        print("unused")
#Задание 6.2b
ip_good = False
while not ip_good:
    ip_good = True
    ip = input("Введите IP: ")
    ip_list = ip.split(".")
    if len(ip_list) != 4:
        ip_good = False

    for oct in ip_list:
        if not (oct.isdigit() and int(oct) in range(255)):
            ip_good = False

    if not ip_good:
        print("Неправильный IP")
    else:
        oct1, oct2, oct3, oct4 = [
            int(ip_list[0]),
            int(ip_list[1]),
            int(ip_list[2]),
            int(ip_list[3]),
        ]
        if oct1 >= 1 and oct1 <= 223:
            print("unicast")
        elif oct1 >= 224 and oct1 <= 239:
            print("multicast")
        elif ip == '255.255.255.255':
            print("local broadcast")
        elif ip == '0.0.0.0':
            print("unassigned")
        else:
            print("unused")
#Задание 6.3
access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}

for intf, vlan in access.items():
    print("interface FastEthernet" + intf)
    for command in access_template:
        if command.endswith("access vlan"):
            print(f" {command} {vlan}")
        else:
            print(f" {command}")


for intf, value in trunk.items():
    print ("interface FastEthernet" + intf)
    action = value[0]
#    print (value)
    for command in trunk_template:
        if command.endswith('allowed vlan'):
            vlans = ",".join(value[1:])
#            print (action)
            if action == "add":
                print(f" {command} add {vlans}")
            elif action == "only":
                print(f" {command} {vlans}")
            elif action == "del":
                print(f" {command} remove {vlans}")
        else:
            print(f" {command}")