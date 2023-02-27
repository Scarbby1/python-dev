from sys import argv

print("Задания 7.1-7.3b")
#Задание 7.1
with open('ospf.txt') as f:
    for line in f:
        line = line.split()
        o, prefix, admetric, via, nexthop, lastupdate, interface = line
        template = '{:20} {:15}'
        print(template.format('Prefix', prefix))
        print(template.format('AD/Metric', admetric.strip('[]')))
        print(template.format('Next-Hop', nexthop.strip(',')))
        print(template.format('Last update ', lastupdate.strip(',')))
        print(template.format('Outbound Interface', interface))

#Задание 7.2
'''r1 = argv[1]
with open(r1) as f:
    for line in f:
        if not line.startswith("!"):
            print(line.rstrip())'''

#Задание 7.2a
'''r1 = argv[1]
ignore = ["duplex", "alias", "configuration"]

with open(r1) as f:
    for line in f:
        for ignore_word in ignore:
            if ignore_word in line:
                ignore_use = 1
        if not line.startswith("!") and not ignore_use == 1:
            print(line.rstrip())
        ignore_use = 0
'''
#Задание 7.2b
ignore = ["duplex", "alias", "configuration"]

src_r1 = argv[1]
dst_r2 = argv[2]

with open(src_r1) as src, open(dst_r2, 'w') as dst:
    for line in src:
        words = line.split()
        words_intersect = set(words) & set(ignore)
        if not line.startswith("!") and not words_intersect:
            dst.write(line)
#Задание 7.3
with open('CAM_table.txt') as f:
    for line in f:
        words = line.split()
        template = '{:15} {:15} {:15}'
        if words and words[0].isdigit():
            vlan, mac, _,ports = words
#            print(template.format(vlan,mac,ports))
            print(f"{vlan:9}{mac:20}{ports}")

#Задание 7.3a
result = []
with open('CAM_table.txt') as f:
    for line in f:
        words = line.split()
        template = '{:15} {:15} {:15}'
        if words and words[0].isdigit():
            vlan, mac, _, ports = words
            result.append([int(vlan), mac, ports])
for vlan, mac, intf in sorted(result):
    print(f"{vlan:<9}{mac:20}{intf}")

#Задание 7.3b
result = []
vlan_input = input("Введите номер VLAN: ")
with open('CAM_table.txt') as f:
    for line in f:
        words = line.split()
        template = '{:15} {:15} {:15}'
        if words and words[0].isdigit():
            vlan, mac, _, ports = words
            result.append([int(vlan), mac, ports])
for vlan, mac, intf in sorted(result):
    if int(vlan_input) == vlan:
        print(f"{vlan:<9}{mac:20}{intf}")