""" Main UI module for basic and scientific calculator
"""

# Importing modules
import sys
from PyQt5 import QtWidgets

from calculator import ScientificCalculator


class CalulatorUi(QtWidgets.QWidget):
    """ Main UI class for calculator
    """
    # pylint: disable=too-many-instance-attributes
    def __init__(self):
        super().__init__()

        self.calculator = ScientificCalculator()

        # setting title
        self.setWindowTitle("Calculator")

        # setting geometry
        self.setGeometry(100, 100, 160, 150)

        # calling method
        self.ui_components()


    def ui_components(self):
        """ Method for initializing widgets and placing widget on window
        """
        # Initializing and setting grid layout for the window
        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)

        # Creating label for first input
        self.first_input_lbl = QtWidgets.QLabel('Number 1', self)
        # Adding label in the layout
        layout.addWidget(self.first_input_lbl, 0, 0)

        # Creating a line edit for getting input value from the user
        self.first_input_text = QtWidgets.QLineEdit(self)
        # Adding line edit in the layout
        layout.addWidget(self.first_input_text, 0, 3)

        # Creating label for second input
        self.second_input_lbl = QtWidgets.QLabel('Number 2', self)
        # Adding label in the layout
        layout.addWidget(self.second_input_lbl, 1, 0)

        # Creating a line edit for getting input value from the user
        self.second_input_text = QtWidgets.QLineEdit(self)
        # Adding line edit in the layout
        layout.addWidget(self.second_input_text, 1, 3)

        # Creating a button for add operator
        self.add_btn = QtWidgets.QPushButton('+', self)
        # Adding button in the layout
        layout.addWidget(self.add_btn, 2, 0)

        # Creating a button for subtraction operator
        self.sub_btn = QtWidgets.QPushButton('-', self)
        # Adding button in the layout
        layout.addWidget(self.sub_btn, 2, 1)

        # Creating a button for multiplication operator
        self.mul_btn = QtWidgets.QPushButton('*', self)
        # Adding button in the layout
        layout.addWidget(self.mul_btn, 2, 2)

        # Creating a button for division operator
        self.div_btn = QtWidgets.QPushButton('/', self)
        # Adding button in the layout
        layout.addWidget(self.div_btn, 2, 3)

        # Creating a button for sine function
        self.sin_btn = QtWidgets.QPushButton('sin', self)
        # Adding button in the layout
        layout.addWidget(self.sin_btn, 3, 0)

        # Creating a button for cos function
        self.cos_btn = QtWidgets.QPushButton('cos', self)
        # Adding button in the layout
        layout.addWidget(self.cos_btn, 3, 1)

        # Creating a button for tan function
        self.tan_btn = QtWidgets.QPushButton('tan', self)
        # Adding button in the layout
        layout.addWidget(self.tan_btn, 3, 2)

        # Creating a button for log function
        self.log_btn = QtWidgets.QPushButton('log', self)
        # Adding button in the layout
        layout.addWidget(self.log_btn, 3, 3)

        # Creating a label for displaying operation result
        self.disp_operation_lbl = QtWidgets.QLabel('', self)
        # Adding label in the layout
        layout.addWidget(self.disp_operation_lbl, 4, 0, 1, 4)

        # Creating a label for displaying output
        self.output_lbl = QtWidgets.QLabel('Output', self)
        # Adding label in the layout
        layout.addWidget(self.output_lbl, 5, 0)

        # Creating a text field for displaying the output
        self.output_text = QtWidgets.QLineEdit(self)
        # Adding text field in the layout
        layout.addWidget(self.output_text, 5, 3)

        # Creating a button for clearing the text fields
        self.clear_btn = QtWidgets.QPushButton("Clear", self)
        # Adding button in the layout
        layout.addWidget(self.clear_btn, 6, 0, 1, 4)


        # Adding action to each of the button
        self.add_btn.clicked.connect(self.display_operation)
        self.sub_btn.clicked.connect(self.display_operation)
        self.mul_btn.clicked.connect(self.display_operation)
        self.div_btn.clicked.connect(self.display_operation)

        self.sin_btn.clicked.connect(self.display_scientific_operation)
        self.cos_btn.clicked.connect(self.display_scientific_operation)
        self.tan_btn.clicked.connect(self.display_scientific_operation)
        self.log_btn.clicked.connect(self.display_scientific_operation)

        self.clear_btn.clicked.connect(self.clear)

    def display_operation(self):
        """ Button slot to perform the arithmetic operation
        """
        operator = self.sender().text()
        first_input = self.first_input_text.text()
        second_input = self.second_input_text.text()

        # Call the calculator class to perform the arithmetic operation
        output_data, display_operation = self.calculator.perform_operation(
            operator,
            first_input,
            second_input
        )

        self.disp_operation_lbl.setText(display_operation)
        self.output_text.setText(str(output_data))

    def display_scientific_operation(self):
        """ Button slot to perform the scientific operation
        """
        operator = self.sender().text()
        first_input = self.first_input_text.text()
        second_input = self.second_input_text.text()
        arith_operator = None

        # If both the input values are provided, perform the arithmetic operation
        if first_input and second_input:
            # Get the list of arithmetic operators
            operator_lists = self.calculator.get_operators()
            # Display an input dialog box to get the operator
            # for performing the arithmetic operation
            arith_operator_symbol, operator_success = QtWidgets.QInputDialog.getItem(
              self, 'Input Operator', 'Select operator for scientific calculation:', operator_lists)
            if operator_success:
                arith_operator = arith_operator_symbol
            else:
                # Do not perform any operation
                return

        # Call the calculator class to perform the scientific operation
        output_data, display_operation = self.calculator.perform_scientific_operation(
            operator,
            first_input,
            second_input,
            arith_operator
        )
        self.disp_operation_lbl.setText(display_operation)
        self.output_text.setText(str(output_data))


    def clear(self):
        """ Button slot to clear all the text fields on the window
        """
        self.first_input_text.setText('')
        self.second_input_text.setText('')
        self.disp_operation_lbl.setText('')
        self.output_text.setText('')


def main():
    """ Main function to launch the calculator window
    """
    # create pyqt5 app
    app = QtWidgets.QApplication(sys.argv)

    # create the instance of our Window
    window = CalulatorUi()
    # show all the widgets of the window
    window.show()

    # start the app
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
