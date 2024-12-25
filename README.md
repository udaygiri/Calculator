# Calculator Project 🧮

Welcome to the **Python Calculator** project! 🎉 This is a simple yet powerful calculator application built using **Python** 🐍 and the **Tkinter** library. It features a sleek, user-friendly interface and supports basic arithmetic operations ➕➖✖️➗, as well as advanced functionalities like square root √ and percentage calculations 💯.

## Features ✨

- **Basic Arithmetic Operations**: Add, subtract, multiply, and divide ➕➖✖️➗.
- **Advanced Operations**: Square root and percentage calculations √💯.
- **Dynamic Theme Toggle**: Switch between light and dark themes 🌞🌙 for a better user experience.
- **Keyboard Support**: Use your keyboard ⌨️ for quick calculations.
- **Error Handling**: Handles errors like division by zero ⚠️ and invalid syntax ⚡ gracefully.

## Technologies Used ⚙️

- **Python 3.x** 🐍: The programming language used for the project.
- **Tkinter** 🖥️: Python's built-in GUI library for creating the graphical user interface.
- **Math Library** ➗: For advanced mathematical functions such as square root.

## Installation

To get started with the calculator, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/calculator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd calculator
   ```

3. Ensure you have Python 3.x installed on your machine.

4. Install the required dependencies (Tkinter comes pre-installed with Python, so no additional installation is required).

## Usage 🚀

To run the calculator, simply execute the Python script:

```bash
python calculator.py
```

## Interface Overview 🖥️

- **Display**: Shows the current expression and the total result 📝.
- **Buttons**: Includes digits (0-9) 🔢, operators (+, -, *, /) ➕➖✖️➗, and special buttons (clear, equals, square root, percentage) ❌✅√💯.
- **Theme Toggle**: Switch between light and dark themes using the "Toggle Theme" button 🌞🌙.

## Keyboard Shortcuts ⌨️

You can also interact with the calculator using your keyboard:

- **Digits**: Press number keys (0-9) 🔢 to input digits.
- **Operators**: Press +, -, *, / ➕➖✖️➗ to perform operations.
- **Evaluate**: Press = or Enter to evaluate the expression ✅.
- **Clear**: Press C to clear the current expression ❌.
- **Backspace**: Press Backspace to delete the last character ⬅️.
- **Exit**: Press Escape to close the calculator 🚪.

## Code Structure 🧩

- **Calculator Class**: The main class that handles the logic and UI components of the calculator.
- **create_button()**: Creates all the buttons for the calculator 🔲.
- **create_display_label()**: Creates the display area where the current and total expressions are shown 🖥️.
- **AddToExpression(), ClearState(), AppendOperator(), EvaluateExpression()**: Methods for handling basic calculator functionalities ➕➖✖️➗.
- **toggle_theme()**: Switches between light and dark themes 🌞🌙.
- **handle_square_root() and handle_percentage()**: Methods for advanced operations √💯.
- **Themes**: The calculator supports two themes: Light Theme 🌞 and Dark Theme 🌙. You can toggle between them using the "Toggle Theme" button.

## Example Usage 📝

Once you run the program, you'll see the following interface:

- **Display Area**: Shows the current input and the result 🖥️.
- **Buttons**: Buttons for digits, operators, and advanced operations 🔢➕➖✖️➗.
- **Toggle Button**: Switch between light and dark themes using the "Toggle Theme" button 🌞🌙.

### Example Calculation 📊:

1. Input `5 + 3 * 2` using the buttons or keyboard.
2. Press `=` or `Enter` to get the result `11` ✅.
3. You can also calculate the square root of a number by pressing the `√` button.

## Contributing 🤝

Feel free to fork this project, make improvements, and submit pull requests! Contributions are welcome 🌟.

## License 📜

This project is licensed under the MIT License - see the LICENSE file for details.

