import sys
import time

start_time = time.time()


def ip2bin(ip):
    '''
    Converts IP-address to binary number
    :param ip: IP-address IPv4
    :return: Binary number
    '''
    octets = map(int, ip.split('.'))
    binary = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(*octets)
    return binary


list_of_ip = []

with open(file=sys.argv[1], mode="r") as file:
    lines = [line.strip() for line in file]
    for ip in lines:
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

net = str(sorted_list[0][0:need]) + (32-need)*'0'

net = 'Result net: ' + str(int(net[0:8], 2)) + '.' + str(int(net[8:16], 2)) + '.' + str(int(net[16:24], 2)) + '.' + str(int(net[24:], 2)) + '/' + str(need)

print(net)

finish_time = time.time() - start_time