import sys
from scapy.all import sr1,IP,ICMP


def ICMPEchoRequest(input_dst, time_var):
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
    return False

    

