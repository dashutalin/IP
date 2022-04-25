import sys
import ipaddress
import time

start_time = time.time()


def ip2bin(ip):
    '''
    Converts IP-address to binary number
    :param ip: IP-address IPv6
    :return: Binary number
    '''
    octets = list(ip.split('_'))
    binary = []
    for number in octets:
        number = int(number, 16)
        binary.append(number)
    binary_final = '{0:016b}{1:016b}{2:016b}{3:016b}{4:016b}{5:016b}{6:016b}{7:016b}'.format(*binary)
    return binary_final


list_of_ip = []

with open(file=sys.argv[1], mode="r") as file:
    lines = [line.strip() for line in file]
    for ip in lines:
        ip = format(ipaddress.IPv6Address(ip), '_x')
        ip = ip2bin(ip)
        list_of_ip.append(ip)


sorted_list = sorted(list_of_ip)
new_list = []
for number in sorted_list:
    number_1 = list(number)
    new_list.append(number_1)

type_1 = 0
type_2 = 0
last = len(new_list)

while new_list[last-2][type_1] == new_list[last-1][type_2]:
    type_1 += 1
    type_2 += 1
    continue
else:
    need = type_2


# net = str(sorted_list[0][0:need]) + (128-need)*'0'

net = 'Result net: ' + lines[0][0:6] + '/' + str(need)

print(net)

finish_time = time.time() - start_time

print(finish_time)