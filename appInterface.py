import sys
import packetSniff
import os, signal
from PySide6.QtWidgets import (QLineEdit, QLabel, QPushButton, QApplication,
    QVBoxLayout, QDialog)


class MainWidget(QDialog):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.FieldIPAddress = QLineEdit()
        self.FieldDuration = QLineEdit()
        self.FieldPacketAmount = QLineEdit()
        self.FieldVariableName = QLineEdit()
        self.button = QPushButton("Send Echo Request")
        self.button1 = QPushButton("Sniff!")
        self.title = QLabel("Minh's Packet Sniffer Application")
        self.title1 = QLabel("ICMP Echo Request")
        self.title2 = QLabel("Sniff Incoming Traffic")
        self.Fieldtext = QLabel("Enter the IP Address: ")
        self.Fieldtext1 = QLabel("Enter the duration: ")
        self.Fieldtext2 = QLabel("Enter the amount of packets")
        self.Fieldtext3 = QLabel("Enter the variable name: ")
        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.title2)
        layout.addWidget(self.Fieldtext2)
        layout.addWidget(self.FieldPacketAmount)
        layout.addWidget(self.Fieldtext3)
        layout.addWidget(self.FieldVariableName)
        layout.addWidget(self.button1)
        layout.addWidget(self.title1)
        layout.addWidget(self.Fieldtext)
        layout.addWidget(self.FieldIPAddress)
        layout.addWidget(self.Fieldtext1)
        layout.addWidget(self.FieldDuration)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.echo)
        self.button1.clicked.connect(self.sniff)



    def echo(self):
        print(f"Your IP Address is: {self.FieldIPAddress.text()}")
        packetSniff.ICMPEchoRequest(self.FieldIPAddress.text(), self.FieldDuration.text())

    def sniff(self):
        print(f"Your packet count is: {self.FieldPacketAmount.text()}")
        print(f"Your variable name is: {self.FieldVariableName.text()}")
        packetSniff.Sniff(self.FieldPacketAmount.text(), self.FieldVariableName.text())

    



    
    

if __name__ == "__main__":
    app = QApplication([])
    widget = MainWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())