# import sys
#
# version = sys.argv[2]
import argparse
parser = argparse.ArgumentParser(description='This code finds the minimum subnet for a set of IP-addresses')
parser.add_argument('file', help='first argument is file with IP-addresses')
parser.add_argument('version', help='second argument is version of IP')
args = parser.parse_args()

if args.version == '4' or args.version == 'IPv4':
    import IPv4
elif args.version == '6' or args.version == 'IPv6':
    import IPv6
else:
    print('You can use only 4 or 6 version of IP')