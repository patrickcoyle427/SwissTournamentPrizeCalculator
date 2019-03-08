#!/bin/usr/python3

'''
TO DO:

create cost of event and cost of prizes labels and buttons

Get info from tournament result calculator into this calculator

Add label for prize input section

Add buttons to accept the input

Use user input to calculate the cost of the event.

have results exported to csv file

create graph of profitability?

Calculate profitability by:

cost = cost of prizes * prizes given out
example: 2.05 * 21

money taken in = entry fee * players

profit = money taken in - cost

profit % = profit / money taken in

Create a GUI


'''

import sys

from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLineEdit,
                             QVBoxLayout, QPushButton, QLabel, QWidget,
                             QComboBox, QGridLayout)

from PyQt5.QtCore import Qt

class CalcWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        ### Widget Layout ###
        
        layout = QGridLayout()
        # layout for the widget itself

        layout.setColumnStretch(0,1)
        layout.setColumnStretch(3,1)
        
        layout.setRowStretch(0,1)
        layout.setRowStretch(3,1)
        
        self.setLayout(layout)

        self.round_grid = QGridLayout()
        # Grid layout that labels and line edits are added to, which is then added
        # to the widget's grid layout.

        layout.addLayout(self.round_grid, 2, 1)

        ### Line Edits and their labels ###

        # The following QLabels and QLineEdits are not visible until
        # they are selected by the QComboBox Below

        self.tr_3_0_lab = QLabel('3-0 Record')
        self.tr_2_1_lab = QLabel('2-1 Record')
        self.tr_1_2_lab = QLabel('1-2 Record')
        self.tr_0_3_lab = QLabel('0-3 Record')
        # QLabels for the 3 round tournament option
        # tr stands for three rounds, lab is label
        # Each of the numbers corresponds to the number of wins and losses
        # a player could have. Example: 3_0 is three wins and 0 losses

        self.tr_3_0_le = QLineEdit()
        self.tr_2_1_le = QLineEdit()
        self.tr_1_2_le = QLineEdit()
        self.tr_0_3_le = QLineEdit()
        # QLineEdits for the 3 round tournament option
        # tr stands for three rounds, le is line edit


        self.fr_4_0_lab = QLabel('4-0 Record')
        self.fr_3_1_lab = QLabel('3-1 Record')
        self.fr_2_2_lab = QLabel('2-2 Record')
        self.fr_1_3_lab = QLabel('1-3 Record')
        self.fr_0_4_lab = QLabel('0-4 Record')
        # QLabels for the 4 round tournament option
        # fr stands for four rounds

        self.fr_4_0_le = QLineEdit()
        self.fr_3_1_le = QLineEdit()
        self.fr_2_2_le = QLineEdit()
        self.fr_1_3_le = QLineEdit()
        self.fr_0_4_le = QLineEdit()
        # QLineEdits for the 4 round tournament option
        # fr stands for four rounds

        ### Number of Rounds Combobox ###
        
        round_label = QLabel('Choose the number of rounds:')

        #self.layout.addWidget(round_label)
        layout.addWidget(round_label, 1, 1)

        self.round_choice = QComboBox(self)
        layout.addWidget(self.round_choice, 1, 2)

        self.round_choice.setMaximumWidth(50)

        self.round_choice.addItem('')
        self.round_choice.addItem('3')
        self.round_choice.addItem('4')

        self.round_choice.activated.connect(self.add_round_options)

        ### Cost of event and price of prizes ###

        

        ### Misc Window Settings ###

        #self.setGeometry(300, 200, 400, 500)

        self.setFixedSize(300, 400)

        self.setWindowTitle('Swiss Tournament Profit Calculator')

        self.show()

    def add_round_options(self, mode):

        # adds Qlabels and Qline edits based on the number of rounds
        # the user selected with the round_choice combo box

        for i in reversed(range(self.round_grid.count())):

            self.round_grid.itemAt(i).widget().setParent(None)

        # Loop to switch which line edits and labels are displayed.

        three_rounds = {
            (0, 0): self.tr_3_0_lab,
            (0, 1): self.tr_3_0_le,
            (1, 0): self.tr_2_1_lab,
            (1, 1): self.tr_2_1_le,
            (2, 0): self.tr_1_2_lab,
            (2, 1): self.tr_1_2_le,
            (3, 0): self.tr_0_3_lab,
            (3, 1): self.tr_0_3_le
            }
        
        four_rounds = {
            
            (0, 0): self.fr_4_0_lab,
            (0, 1): self.fr_4_0_le,
            (1, 0): self.fr_3_1_lab,
            (1, 1): self.fr_3_1_le,
            (2, 0): self.fr_2_2_lab,
            (2, 1): self.fr_2_2_le,
            (3, 0): self.fr_1_3_lab,
            (3, 1): self.fr_1_3_le,
            (4, 0): self.fr_0_4_lab,
            (4, 1): self.fr_0_4_le
            }

        display_options = {
            0: 0,
            1: 3,
            2: 4
            }

        choice = display_options[mode]

        if choice == 3:

            for pos, obj in three_rounds.items():

                x, y = pos

                self.round_grid.addWidget(obj, x, y)

        elif choice == 4:

            for pos, obj in four_rounds.items():

                x, y = pos

                self.round_grid.addWidget(obj, x, y)
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    calc = CalcWindow()
    sys.exit(app.exec_())

    
