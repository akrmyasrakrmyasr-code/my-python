import argparse

from tools.status_code import status_code
from tools.scan_paths import scan_paths
from tools.extract_ip import extract_ip

parses=argparse.ArgumentParser(description="PYTHON TOOLS NETWORK 2026")
parses.add_argument("command",choices=['ip','paths','code'],help='command run code')
args=parses.parse_args()

if args.command=='ip':
    extract_ip()

if args.command=='code':
    status_code()

if args.command=='paths':
    scan_paths()