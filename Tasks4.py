
print('Задание 4.5')
c1 =  "switchport trunk allowed vlan 1,2,3,5,8"
c2 =  "switchport trunk allowed vlan 1,3,8,9"

c1 = c1.split()[-1]
c2 = c2.split()[-1]

c1 = set(c1)
c2 = set(c2)

c1.remove(',')
c2.remove(',')

res = c1.intersection(c2)

res=list(res)

res = sorted(res)
print(res)

print('Задание 4.6')

 #ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_route = ospf_route.replace('[', '')
ospf_route = ospf_route.replace(']', '')
ospf_route = ospf_route.replace('via', '')
ospf_route = ospf_route.replace(',', '')
ospf_route = ospf_route.split()

text = "Prefix, AD/Metric, Next-Hop, Last update, Outbound Interface"
text = text.split(',')

print('Prefix', '             ', ospf_route[0])
print('AD/Mertric', '         ', ospf_route[1])
print('Next-Hop', '           ', ospf_route[2])
print('Last update','        ', ospf_route[3])
print('OI', '                 ',ospf_route[4])

print('Задание 4.8')
ip = '192.168.3.1'

ip = ip.replace('.', ' ')
ip = ip.split()

ip0 = int(ip[0])
ip1 = int(ip[1])
ip2 = int(ip[2])
ip3 = int(ip[3])

print(ip0, '        ', ip1, '        ' , ip2, '        ', ip3)

ip0 = bin(ip0)
ip0 = ip0.replace('0b', '')

ip1 = bin(ip1)
ip1 = ip1.replace('0b', '')

ip2 = bin(ip2)
ip2 = ip2.replace('0b', '')

ip3 = bin(ip3)
ip3 = ip3.replace('0b', '')

print(ip0,'   ', ip1, '   ', ip2, '       ', ip3)