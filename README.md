# SimpleCalculator
This user-friendly calculator lets you add, subtract, multiply, and divide with clear input fields and a comprehensive history.

## Key Features:
- **Simple Interface:** Effortless calculation with intuitive buttons and clear display.
- **Error Handling:** Get notified of invalid input and division by zero attempts.
- **Calculation History:** Track all your past calculations for easy reference.
- **Save History (Optional):** Save your calculation history to a file for future use.

## Main Window
The main window consists of several sections:
- **Display:** This area shows the current result of the calculation.
- **Input Fields:**
  - **Number 1:** Enter the first number for the calculation.
  - **Number 2:** Enter the second number for the calculation.
- **History:** This text box displays the history of your previous calculations.
- **Buttons:**
  - **Sum ( + ):** Calculates the sum of Number 1 and Number 2.
  - **Difference ( - ):** Calculates the difference between Number 1 and Number 2 (Number 1 - Number 2).
  - **Product ( * ):** Calculates the product of Number 1 and Number 2 (Number 1 * Number 2).
  - **Quotient ( / ):** Calculates the quotient of Number 1 and Number 2 (Number 1 / Number 2).
  - **History Save:** Saves the current history to a text file.
  - **Input Clear:** Clears the values in both Number 1 and Number 2 input fields.
  - **History Clear:** Clears the text box containing the history of calculations.
  - **Exit:** Closes the application.
 
## Using the Calculator
1. Enter the first number in the "Number 1" field.

   ![](https://github.com/hrosicka/PyQtSimpleCalculator/blob/master/doc/MainWindow1.PNG)
3. Enter the second number in the "Number 2" field.

   ![](https://github.com/hrosicka/PyQtSimpleCalculator/blob/master/doc/MainWindow2.PNG)
5. Click the button corresponding to the desired operation (Sum, Difference, Product, or Quotient).
6. The result of the calculation will be displayed in the display area.
   
   ![](https://github.com/hrosicka/PyQtSimpleCalculator/blob/master/doc/ResultsAndHistory.PNG)
8. The calculation will be added to the history box along with the formula used (e.g., "5 + 3 = 8").
9. You can perform multiple calculations and view their history.

## Saving History
1. Click the "History Save" button.
2. A dialog box will appear, allowing you to choose a location and filename to save the history as a text file.
3. Once you select a location and filename, the history will be saved to the chosen file.

## Clearing Input and History
- Click the "Input Clear" button to clear the values in both Number 1 and Number 2 input fields.
- Click the "History Clear" button to clear the text box containing the history of calculations.

## Error Handling
- The application performs basic input validation. If you enter a non-numeric value in the input fields, an error message will be displayed, and the input fields will be highlighted in pink.
  
  ![](https://github.com/hrosicka/PyQtSimpleCalculator/blob/master/doc/InputError.PNG)
- Division by zero is not allowed. If you attempt to divide by zero, an error message will be displayed, and the Number 2 input field will be highlighted in pink.
  
  ![](https://github.com/hrosicka/PyQtSimpleCalculator/blob/master/doc/ErrorDividedByZero.PNG)

## Additional Notes
- Tooltips are available for most buttons, providing a brief description of their functionality.
  ![](https://github.com/hrosicka/PyQtSimpleCalculator/blob/master/doc/Tooltip.png)
- The application uses a dark blue color scheme for buttons and message boxes, enhancing readability.

## Unit tests
### Class TestCalculator
Class TestCalculator contains unit tests for the Calculator class.

These tests verify the functionality of the calculator's basic arithmetic operations (addition, subtraction, multiplication, and division) for various inputs, including:
- Positive and negative numbers
- Mixed combinations of positive and negative numbers
- Zero values
- Limit cases with very large or very small numbers
The tests also ensure that division by zero raises a CalculatorError.


