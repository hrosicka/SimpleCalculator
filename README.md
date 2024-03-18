# PyQtSimpleCalculator
Simple calculator with history and saving results in PyQt
### Functions
- Operations
  - 4 basics: + - * /
- History view
- History save
  - create file history_calc.txt
- Input clear
- History clear

### Enter inputs
- Enter number 1:
  
![](https://github.com/hrosicka/PyQtSimpleCalculator/blob/master/doc/MainWindow1.PNG)

- Enter number 2:
  
![](https://github.com/hrosicka/PyQtSimpleCalculator/blob/master/doc/MainWindow2.PNG)

- Every button has tooltip:
  
![](https://github.com/hrosicka/PyQtSimpleCalculator/blob/master/doc/Tooltip.png)

- Input can be only a number:
  
![](https://github.com/hrosicka/PyQtSimpleCalculator/blob/master/doc/InputError.PNG)

- Numbers can not be devided by zero:

![](https://github.com/hrosicka/PyQtSimpleCalculator/blob/master/doc/ErrorDividedByZero.PNG)

### Results
![](https://github.com/hrosicka/PyQtSimpleCalculator/blob/master/doc/ResultsAndHistory.PNG)


## Unit tests
### Class TestCalculator
Class TestCalculator contains unit tests for the Calculator class.

These tests verify the functionality of the calculator's basic arithmetic operations (addition, subtraction, multiplication, and division) for various inputs, including:
- Positive and negative numbers
- Mixed combinations of positive and negative numbers
- Zero values
- Limit cases with very large or very small numbers
The tests also ensure that division by zero raises a CalculatorError.


