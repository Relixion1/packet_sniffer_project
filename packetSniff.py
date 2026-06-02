import sys
from scapy.all import sr1,IP,ICMP

input_dst = input("Please enter an IP address: ")

p=sr1(IP(dst=input_dst)/ICMP())
if p:
    p.show()

