#!/usr/bin/env python3
import sys
import socket


def get_accessible_ports(address, min_port, max_port):
	found_ports = []
	for port in range(min_port, max_port + 1):
		s = socket.socket()
		if s.connect_ex((address, port)) == 0:
			found_ports.append(port)
			print(s.recv(port))
	return found_ports


def main():
	address = "localhost"
	min_port = int(20050)
	max_port = int(20150)
	ports = get_accessible_ports(address, min_port, max_port)
	for p in ports:
		print(p)

main()

# This makes sure the main function is not called immediatedly
# when TMC imports this module
#if __name__ == "__main__": 
#	if len(sys.argv) != 4:
#		print('usage: python %s address min_port max_port' % sys.argv[0])
#	else:
#		main(sys.argv)
