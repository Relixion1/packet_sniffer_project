import sys
import packetSniff
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QLineEdit, QLabel, QPushButton, QApplication,
    QVBoxLayout, QDialog, QTableWidget, QTableWidgetItem)


class MainWidget(QDialog, QTableWidget, QTableWidgetItem):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.table = QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Network Access Layer", "Internet Layer", "Transport Layer/Request", "Application Layer"])
        self.table.setColumnWidth(2, 500)
        self.table.setColumnWidth(0, 200)
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
        layout.addWidget(self.table)
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
        with open("terminal_log.txt", "r") as file:
            for line_count, line in enumerate(file):
                self.table.setRowCount(line_count + 1)
                stripped_line = line.strip()
                slash_count = 0
                text_array = []
                for char in stripped_line:
                    if char == "/":
                        print("".join(text_array))
                        item_packet = QTableWidgetItem("".join(text_array))
                        self.table.setItem(line_count, slash_count, item_packet)
                        slash_count += 1
                        text_array = []
                    else:
                        text_array.append(char)
                item_packet = QTableWidgetItem("".join(text_array))
                self.table.setItem(line_count, slash_count, item_packet)

                        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.resize(1000, 780)
    widget.show()
    sys.exit(app.exec())