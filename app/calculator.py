""" Module contains all the available operations for basic and scientific calculator.
"""

# Importing modules
import math
import re
import logging

# Create and configure logger
logging.basicConfig(filename="logFile.log",
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s',
                    filemode='w')
# Creating an object
logger = logging.getLogger('calculatorLogs')

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)


def convert_number(func):
    """ Custom Decorator to convert string values either in integer or float value,
        based on the condition
    """
    def inner(*args, **kwargs):
        arg_list = list(args)
        args = []
        for arg in arg_list:
            args.append(int(arg) if arg.isdigit() else float(arg))
        return func(*args, **kwargs)
    return inner


class Calculator:
    """ Base class for calculator which performs all arithmetic operations
    """
    def perform_operation(self, operator, first_num, second_num):
        """ Main method for base calculator to perform arithmetic operation
            based on the provided inputs.

            Args:
                 operator(str): operator symbol to perform the requested operation
                 first_num(str): first input operand for the operation
                 second_num(str): second input operand for the operation
        """
        # logging the input operator and operands
        self.initial_logging_statements(operator, first_num, second_num)

        # get the method name from the operator
        operation_method = self.get_operators().get(operator)

        # validation check for empty inputs
        if first_num == '' or second_num == '':
            display_operation = 'Please provide valid input.'
            logger.warning(display_operation)
            return '', display_operation

        # validation check for the invalid input values
        if ((first_num and not re.search(r'[^ a-zA-z\s\t.(){}]+', first_num)) or
                                second_num and not re.search(r'[^ a-zA-z\s\t.(){}]+', second_num)):
            display_operation = 'Please provide valid input.'
            logger.warning(display_operation)
            return '', display_operation

        # get the output data and message for the performed operation
        output_data, message = getattr(self, operation_method)(first_num, second_num)
        logger.info("Output: %s", str(output_data))

        # If error occurs, log the warning
        if message:
            display_operation = message
            logger.warning(display_operation)
        else:
            display_operation = 'Operation Performed: {}{}{}={}'.format(
                first_num,
                operator,
                second_num,
                str(output_data)
            )
            logger.info(display_operation)

        return output_data, display_operation

    @staticmethod
    def get_operators():
        """ Mapping to get operator function based on the provided operator
        """
        mapping = {
            '+': '_add',
            '-': '_subtract',
            '*': '_multiply',
            '/': '_division',
        }
        return mapping

    @staticmethod
    def initial_logging_statements(operator, first_num, second_num):
        """ Utility function for logging the details of operators and operands

            Args:
                 operator(str): operator symbol to perform the requested operation
                 first_num(str): first input operand for the operation
                 second_num(str): second input operand for the operation
        """
        logger.info("Input 1: %s", first_num)
        logger.info("Input 2: %s", second_num)
        logger.info("Operator selected: %s", operator)


    @staticmethod
    @convert_number
    def _add(input1, input2):
        """ Perform the arithmetic addition operation for input values

            Args:
                input1(int/float): first input value
                input2(int/float): second input value
        """
        message = None
        operation = input1 + input2
        return operation, message

    @staticmethod
    @convert_number
    def _subtract(input1, input2):
        """ Perform the arithmetic subtraction operation for input values

            Args:
                input1(int/float): first input value
                input2(int/float): second input value
        """
        message = None
        operation = input1 - input2
        return operation, message

    @staticmethod
    @convert_number
    def _multiply(input1, input2):
        """ Perform the arithmetic multiplication operation for input values

            Args:
                input1(int/float): first input value
                input2(int/float): second input value
        """
        message = None
        operation = input1 * input2
        return operation, message

    @staticmethod
    @convert_number
    def _division(input1, input2):
        """ Perform the arithmetic division operation for input values

            Args:
                input1(int/float): first input value
                input2(int/float): second input value
        """
        message = None
        try:
            operation = input1 / input2
        except ZeroDivisionError:
            # Handle division by zero error
            operation = ''
            message = "Number 2 can't be zero. Please provide correct input."
        return operation, message


class ScientificCalculator(Calculator):
    """ Class for calculator which performs all scientific operations
    """
    def perform_scientific_operation(self, operator, first_num=None, second_num=None,
     arith_operator=None):
        """ Main method for to perform scientific operation
            based on the provided inputs.

            Args:
                 operator(str): operator symbol to perform the requested operation
                 first_num(str): first input operand for the operation
                 second_num(str): second input operand for the operation
        """
        # logging the input operator and operands
        self.initial_logging_statements(operator, first_num, second_num)

        # Mapping to get operator function based on the provided operator
        mapping = {
            'sin': '_sin',
            'cos': '_cos',
            'tan': '_tan',
            'log': '_log',
        }

        # get the method name from the operator
        operation_method = mapping.get(operator)

        # validation check for empty inputs
        if first_num == '' and second_num == '':
            display_operation = 'Please provide valid input.'
            logger.warning(display_operation)
            return '', display_operation

        # validation check for the invalid input values
        if ((first_num and not re.search(r'[^ a-zA-z\s\t.(){}]+', first_num)) or
                                second_num and not re.search(r'[^ a-zA-z\s\t.(){}]+', second_num)):
            display_operation = 'Please provide valid input.'
            logger.warning(display_operation)
            return '', display_operation

        # If both the input values are provided, perform the arithmetic operation
        if first_num and second_num:
            input_data, _ = self.perform_operation(
                arith_operator,
                first_num,
                second_num,
            )
        # If single input value is provided, then directly perform the scientific operation
        elif first_num or second_num:
            input_data = first_num or second_num

        # get the output data for the performed operation
        output_data = getattr(self, operation_method)(str(input_data))
        logger.info("Output: %s", str(output_data))

        # Create the message for displaying it on the window
        if arith_operator:
            display_operation = 'Operation Performed: {}{}{}{}={}'.format(
                operator,
                first_num,
                arith_operator,
                second_num,
                str(output_data)
            )
        else:
            display_operation = 'Operation Performed: {}{}={}'.format(
                operator,
                input_data,
                str(output_data)
            )
        logger.info(display_operation)
        return output_data, display_operation

    @staticmethod
    @convert_number
    def _sin(input1):
        """ Get the sine value for input number

            Args:
                input1(int/float): input value
        """
        operation = math.sin(input1)
        return operation

    @staticmethod
    @convert_number
    def _cos(input1):
        """ Get the cosine value for input number

            Args:
                input1(int/float): input value
        """
        operation = math.cos(input1)
        return operation

    @staticmethod
    @convert_number
    def _tan(input1):
        """ Get the tangent value for input number

            Args:
                input1(int/float): input value
        """
        operation = math.tan(input1)
        return operation

    @staticmethod
    @convert_number
    def _log(input1):
        """ Get the logarithmic value for input number

            Args:
                input1(int/float): input value
        """
        operation = math.log(input1)
        return operation
