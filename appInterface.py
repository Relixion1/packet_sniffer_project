import sys
import packetSniff
import os, signal
from PySide6.QtWidgets import (QLineEdit, QLabel, QPushButton, QApplication,
    QVBoxLayout, QDialog)


class MainWidget(QDialog):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.edit = QLineEdit()
        self.edit1 = QLineEdit()
        self.button = QPushButton("Confirm")
        self.title = QLabel("Minh's Packet Sniffer Application")
        self.IPtext = QLabel("Enter the IP Address: ")
        self.IPtext1 = QLabel("Enter the duration: ")
        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.IPtext)
        layout.addWidget(self.edit)
        layout.addWidget(self.IPtext1)
        layout.addWidget(self.edit1)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.packet)



    def packet(self):
        print(f"Your IP Address is: {self.edit.text()}")
        packetSniff.ICMPEchoRequest(self.edit.text(), self.edit1.text())

    



    
    

if __name__ == "__main__":
    app = QApplication([])
    widget = MainWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())