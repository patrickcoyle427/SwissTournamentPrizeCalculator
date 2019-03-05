#!/bin/usr/python3

import sys

from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLineEdit,
                             QVBoxLayout, QPushButton, QLabel, QWidget,
                             QComboBox)

from PyQt5.QtCore import Qt

class CalcWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        ### Widget Layout ###

        self.layout = QVBoxLayout()

        self.layout.setAlignment(Qt.AlignCenter)
        
        self.setLayout(self.layout)
        
        round_label = QLabel('Choose the number of rounds:')

        self.layout.addWidget(round_label)

        self.round_choice = QComboBox(self)

        self.layout.addWidget(self.round_choice)

        self.round_choice.setMaximumWidth(50)

        self.round_choice.addItem('')
        self.round_choice.addItem('3')
        self.round_choice.addItem('4')
        self.round_choice.addItem('5')
        self.round_choice.addItem('6')

        self.round_choice.activated.connect(self.add_round_options)

        ### Misc Window Settings ###

        self.setGeometry(300, 200, 400, 500)

        self.setFixedSize(400, 500)

        self.setWindowTitle('Swiss Tournament Profit Calculator')

        self.show()

    def add_round_options(self, choice):

        # adds Qlabels and Qline edits based on the number of rounds
        # the user selected with the round_choice combo box

        if choice != '':

            for option in range(int(choice)):

                self.test_label = QLabel('Test')

                self.layout.addWidget(self.test_label)

                

        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    calc = CalcWindow()
    sys.exit(app.exec_())

    
