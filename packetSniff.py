import sys
import subprocess
from scapy.all import sr1,IP,ICMP
from scapy.all import *



def Sniff(count_var, var_name):
    sys.stdout = open("terminal_log.txt", "w")
    count_var = int(count_var)
    sniff(count=count_var, prn=lambda var_name: var_name.summary())
    sys.stdout.close()
    sys.stdout = sys.__stdout__

def ICMPEchoRequest(input_dst, time_var):
    sys.stdout = open("terminal_log.txt", "w")
    if time_var == "" or input_dst == "":
        print(False)
        return False
    time_var = int(time_var)
    p=sr1(IP(dst=input_dst)/ICMP(), timeout=time_var)
    if p:
        p.show()
        print(True)
        return True
    print(False)
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    return False
    

