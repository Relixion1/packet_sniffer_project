import sys
from PySide6.QtCore import (QObject, QRunnable, Signal, Slot, QThreadPool)
from scapy.all import sr1,IP,ICMP
from scapy.all import *

class sniffTask(QObject, QRunnable):
    finished = Signal(str)
    packet_sniffed = Signal(str)
    error = Signal(str)
    stop_condition = False
    def __init__(self, count_var, parent=None):
        QObject.__init__(self, parent)
        QRunnable.__init__(self)
        self.count_var = int(count_var)
    @Slot()
    def cancel(self):
        self.error.emit(f"Task was cancelled!")
    def run(self):
        print("runnin")
        sniff(prn=lambda x: self.packet_sniffed.emit(x.summary()), count=self.count_var, stop_filter=self.stop_condition)
        self.finished.emit(f"Tasks is completed with {self.count_var} packets sniffed!")

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
    

