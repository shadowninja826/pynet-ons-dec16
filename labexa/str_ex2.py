#!/usr/env python

ip_addr = raw_input("Please input the IP address: ")
ip_addr = ip_addr.split(".")

print
print "{:<12} {:<12} {:<12} {:<12}".format(*ip_addr)
print
