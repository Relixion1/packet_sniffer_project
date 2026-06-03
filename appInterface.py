import sys
from PySide6.QtWidgets import (QLineEdit, QLabel, QPushButton, QApplication,
    QVBoxLayout, QDialog)


class MainWidget(QDialog):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.edit = QLineEdit()
        self.button = QPushButton("Confirm")
        self.title = QLabel("Minh's Packet Sniffer Application")
        self.IPtext = QLabel("Enter the IP Address: ")
        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.IPtext)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.build_packet)



    def build_packet(self):
        print(f"Your IP Address is: {self.edit.text()}")
    
    

if __name__ == "__main__":
    app = QApplication([])
    widget = MainWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())