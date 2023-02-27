print("Задания 5.1-5.1d")
london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}
#задание 5.1
device = input('Введите имя устройства: ')
print(london_co[device])
#задание 5.1a
device = input('Введите имя устройства: ')
parameters = (','.join(london_co[device].keys()))
parameter = input(f'Введите имя параметра({parameters}):')
print(london_co[device][parameter])

#задание 5.1b
device = input('Введите имя устройства: ')
parameters = (','.join(london_co[device].keys()))

parameter = input(f'Введите имя параметра({parameters}):')
print(london_co[device][parameter])
#задание 5.1c
device = input('Введите имя устройства: ')
parameters = (','.join(london_co[device].keys()))
parameter = input(f'Введите имя параметра({parameters}):')
print(london_co[device].get(parameter,'Такого параметра нет'))
#задание 5.1d
device = input('Введите имя устройства: ')
parameters = (','.join(london_co[device].keys()))
parameter = input(f'Введите имя параметра({parameters}):')
parameter = parameter.lower()
print(london_co[device].get(parameter,'Такого параметра нет'))

print("Задания5.2-5.2a")

network = input("Введите ip: ")

ip, mask = network.split("/")
ip_list = ip.split(".")
mask = int(mask)

oc1, oc2, oc3, oc4 = [
    int(ip_list[0]),
    int(ip_list[1]),
    int(ip_list[2]),
    int(ip_list[3]),
]

bin_mask = "1" * mask + "0" * (32 - mask)
m1, m2, m3, m4 = [
    int(bin_mask[0:8], 2),
    int(bin_mask[8:16], 2),
    int(bin_mask[16:24], 2),
    int(bin_mask[24:32], 2),
]
print (bin_mask)
print(m1, m2, m3, m4)

ip_output = """
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}"""

mask_output = """
Mask:
/{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
"""

print(ip_output.format(oc1, oc2, oc3, oc4))
print(mask_output.format(mask, m1, m2, m3, m4))


network = input("Введите ip: ")

ip, mask = network.split("/")
ip_list = ip.split(".")
mask = int(mask)

oc1, oc2, oc3, oc4 = [
    int(ip_list[0]),
    int(ip_list[1]),
    int(ip_list[2]),
    int(ip_list[3]),
]

bin_ip= '{:08b}{:08b}{:08b}{:08b}'.format(oc1, oc2, oc3, oc4)
bin_network = bin_ip[0:mask] + "0" * (32 - mask)

network_oc1, network_oc2, network_oc3, network_oc4 = [
    int(bin_network[0:8], 2),
    int(bin_network[8:16], 2),
    int(bin_network[16:24], 2),
    int(bin_network[24:32], 2),
]

print(oc1, oc2, oc3, oc4)
print(bin_ip)
print(bin_network)

bin_mask = "1" * mask + "0" * (32 - mask)
m1, m2, m3, m4 = [
    int(bin_mask[0:8], 2),
    int(bin_mask[8:16], 2),
    int(bin_mask[16:24], 2),
    int(bin_mask[24:32], 2),
]
print (bin_mask)
print(m1, m2, m3, m4)




ip_out = """
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}"""

mask_out = """
Mask:
/{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
"""

print(ip_out.format(network_oc1, network_oc2, network_oc3, network_oc4))
print(mask_out.format(mask, m1, m2, m3, m4))

print("Задания 5.3-5.3a")

access_template = [
    "switchport mode access", "switchport access vlan {}",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "switchport trunk encapsulation dot1q", "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]

template = {'access': access_template, 'trunk': trunk_template}

mode = input("Введите режим работы (access/trunk): ")
interface = input("Введите интерфейс: ")
vlan = input("Введите номер VLAN: ")

print(f"interface {interface}")
print('\n'.join(template[mode]).format(vlan))