import ipaddress
import sys
import argparse


def createParser(args=None):
    parser = argparse.ArgumentParser(description='This code finds the minimum subnet for a set of IP-addresses')
    parser.add_argument('file', help='first argument is file with IP-addresses', type=argparse.FileType())
    parser.add_argument('version', help='second argument is version of IP', type=str)
    return parser.parse_args()


def ip2bin4(ip):
    '''
    Converts IP-address to binary number
    :param ip: IP-address IPv4
    :return: Binary number
    '''
    octets = map(int, ip.split('.'))
    binary = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(*octets)
    return binary


def ip2bin6(ip):
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

if sys.argv[-1] == '4' or sys.argv[-1] == 'IPv4':
    for ip in lines:
        ip = ip2bin4(ip)
        list_of_ip.append(ip)
elif sys.argv[-1] == '6' or sys.argv[-1] == 'IPv6':
    for ip in lines:
        ip = format(ipaddress.IPv6Address(ip), '_x')
        ip = ip2bin6(ip)
        list_of_ip.append(ip)
else:
    print('You can use only 4 or 6 version of IP')

sorted_list = sorted(list_of_ip)
new_list = []
for number in sorted_list:
    number_1 = list(number)
    if number_1 not in new_list:
        new_list.append(number_1)

type_1 = 0
type_2 = 0
last = len(new_list) - 1

while type_1 <= last:
    while new_list[-2][type_1] == new_list[-1][type_2]:
        type_1 += 1
        type_2 += 1
        continue
    else:
        need = type_2

net = ''

if sys.argv[-1] == '4' or sys.argv[-1] == 'IPv4':
    net = str(sorted_list[0][0:need]) + (32 - need) * '0'
    net = 'Result net: ' + str(int(net[0:8], 2)) + '.' + str(int(net[8:16], 2)) + '.' + str(
        int(net[16:24], 2)) + '.' + str(int(net[24:], 2)) + '/' + str(need)
elif sys.argv[-1] == '6' or sys.argv[-1] == 'IPv6':
    net = 'Result net: ' + lines[0][0:6] + '/' + str(need)

print(net)


if __name__ == '__main__':
    parser = createParser()
    # args = parser.parse_args(sys.argv[1:])
