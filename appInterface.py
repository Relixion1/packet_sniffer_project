import sys
import packetSniff
from scapy.all import sr1,IP,ICMP
from scapy.all import *
from PySide6.QtWidgets import (QWidget,QMainWindow, QLineEdit, QLabel, QPushButton, QApplication,
    QVBoxLayout, QDialog, QTableWidget, QTableWidgetItem)
from PySide6.QtCore import (QObject, QRunnable, QThreadPool,Signal, Slot)


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.threadpool = QThreadPool()
        self.threadpool.setMaxThreadCount(3)
        self.table = QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Network Access Layer", "Internet Layer", "Transport Layer/Request", "Application Layer"])
        self.table.setColumnWidth(2, 500)
        self.table.setColumnWidth(0, 200)
        self.FieldPacketAmount = QLineEdit()
        self.button1 = QPushButton("Sniff!")
        self.button2 = QPushButton("Clear Table")
        self.button3 = QPushButton("Cancel")
        self.button4 = QPushButton("Open Echo Request Window")
        self.button3.setEnabled(False)
        self.title = QLabel("Minh's Packet Sniffer Application")
        self.title2 = QLabel("Sniff Incoming Traffic")
        self.Fieldtext2 = QLabel("Enter the amount of packets")
        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.title2)
        layout.addWidget(self.Fieldtext2)
        layout.addWidget(self.FieldPacketAmount)
        layout.addWidget(self.button1)
        layout.addWidget(self.button3)
        layout.addWidget(self.button2)
        layout.addWidget(self.table)
        layout.addWidget(self.button4)
        self.setLayout(layout)
        self.button1.clicked.connect(self.start_sniff)
        self.button2.clicked.connect(self.clear)
        self.button3.clicked.connect(self.stop_sniff)
        self.button4.clicked.connect(self.open_er_window)
        self.task = None
    
        
    
    def start_sniff(self):
        if self.FieldPacketAmount.text() == "":
            return
        self.button1.setEnabled(False)
        self.button3.setEnabled(True)
        self.task = packetSniff.sniffTask(self.FieldPacketAmount.text())
        self.task.finished.connect(self.sniff_success)
        self.task.packet_sniffed.connect(self.writePacket)
        self.task.error.connect(self.sniff_error)
        self.threadpool.start(self.task)

    def writePacket(self, message : str):
        slash_count = 0
        text_array = []
        rowCount = self.table.rowCount()
        self.table.setRowCount(rowCount + 1)
        for char in message:
            if char == "/":
                item_packet = QTableWidgetItem("".join(text_array))
                self.table.setItem(rowCount, slash_count, item_packet)
                slash_count += 1
                text_array = []
            else:
                text_array.append(char)
        item_packet = QTableWidgetItem("".join(text_array))
        self.table.setItem(rowCount, slash_count, item_packet)


    def stop_sniff(self):
        if self.task:
            self.task.cancel()

    def sniff_success(self):
        self.button1.setEnabled(True)
        self.button3.setEnabled(False)

    def sniff_error(self):
        self.button1.setEnabled(True)
        self.button3.setEnabled(False)


    def clear(self):
        self.table.setRowCount(0)
        #open("terminal_log.txt" , "w").close()

    def open_er_window(self):
        subwidget.show()

class SubWidget(QWidget):
    def __init__(self, parent=None):
        super(SubWidget, self).__init__(parent)
        self.button = QPushButton("Send Echo Request")
        self.button1 = QPushButton("Close Window")
        self.FieldIPAddress = QLineEdit()
        self.FieldDuration = QLineEdit()
        self.title1 = QLabel("ICMP Echo Request")
        self.Fieldtext = QLabel("Enter the IP Address: ")
        self.Fieldtext1 = QLabel("Enter the duration (in seconds): ")
        layout = QVBoxLayout()
        layout.addWidget(self.title1)
        layout.addWidget(self.Fieldtext)
        layout.addWidget(self.FieldIPAddress)
        layout.addWidget(self.Fieldtext1)
        layout.addWidget(self.FieldDuration)
        layout.addWidget(self.button)
        layout.addWidget(self.button1)
        self.setLayout(layout)
        self.button.clicked.connect(self.echo)
        self.button1.clicked.connect(self.Close)
    def echo(self):
        packetSniff.ICMPEchoRequest(self.FieldIPAddress.text(), self.FieldDuration.text())
    def Close(self):
        self.hide()


                        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.resize(1000, 780)
    subwidget = SubWidget()
    subwidget.resize(500, 250)
    widget.show()
    sys.exit(app.exec())