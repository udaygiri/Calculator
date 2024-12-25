import tkinter as tk
import math  # For square root calculation

LIGHT_THEME = {
    "bg": "#f5f5f5",        # Background color
    "fg": "#333333",        # Text color
    "button_bg": "#ffffff", # Button background color
    "button_fg": "#333333", # Button text color
    "button_active_bg": "#adfffe", # Active button background color
    "button_active_fg": "#333333", # Active button text color
}

DARK_THEME = {
    "bg": "#333333",        # Background color
    "fg": "#ffffff",        # Text color
    "button_bg": "#444444", # Button background color
    "button_fg": "#ffffff", # Button text color
    "button_active_bg": "#555555", # Active button background color
    "button_active_fg": "#ffffff", # Active button text color
}

class Calculator:
    def __init__(self):
        """
        Initialize the Calculator class.

        This method sets up the calculator window, theme, display, buttons, and key bindings.

        Parameters:
        None

        Returns:
        None
        """
        self.window = tk.Tk()
        self.window.geometry("400x550")
        self.window.title("Calculator")
        self.window.resizable(0, 0)

        # Set initial theme to light mode
        self.current_theme = LIGHT_THEME

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()
        self.total_label, self.current_label = self.create_display_label()
        self.buttons_frame = self.create_buttons_frame()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            ".": (4, 1), 0: (4, 2)
        }

        self.operations = {
            "/": "\u00F7",
            "*": "\u00D7",
            "-": "-",
            "+": "+"
        }

        for i in range(5):
            if i == 0:
                self.buttons_frame.rowconfigure(i, weight=1)

            else:
                self.buttons_frame.rowconfigure(i, weight=1)
                self.buttons_frame.columnconfigure(i, weight=1)

        self.create_button()
        self.create_toggle_button()
        self.BindKey()


    def BindKey(self):
        """
        Bind keyboard events to the calculator window.

        This method sets up the key binding for keyboard input.

        Parameters:
        None

        Returns:
        None
        """
        self.window.bind("<Key>", self.KeyBorderInput)
    def KeyBorderInput(self, event):
        """
        Handle keyboard input events.

        This method processes keyboard input and performs corresponding calculator actions.

        Parameters:
        event (tk.Event): The keyboard event object.

        Returns:
        None
        """
        key = event.char
        if key.isdigit() or key == ".":
            self.AddToExpression(key)
        elif key in self.operations:
            self.AppendOperator(key)
        elif key == "=" or key == "\r":
            self.EvaluateExpression()
        elif key == "c" :
            self.ClearState()
        elif key == "BackSpace" or key == "\x08":
            self.current_expression = self.current_expression[:-1]
            self.UpdateCurrentState()
        elif key == "Escape":
            self.window.quit()
    def create_button(self):
        """
        Create all buttons for the calculator.

        This method calls other methods to create different types of buttons.

        Parameters:
        None

        Returns:
        None
        """
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_equals_button()
        self.create_clear_button()
        self.create_advanced_buttons()

    def create_display_label(self):
        total_label = tk.Label(self.display_frame, 
                               text=self.total_expression, 
                               anchor="e", 
                               bg=self.current_theme["bg"], 
                               fg=self.current_theme["fg"], 
                               padx=25, 
                               font=("Arial", 25))

        total_label.pack(expand=True, fill="both")

        current_label = tk.Label(self.display_frame, 
                                 text=self.current_expression, 
                                 anchor="e",
                                 bg=self.current_theme["bg"], 
                                 fg=self.current_theme["fg"], 
                                 padx=25, 
                                 font=("Arial", 40))

        current_label.pack(expand=True, fill="both")

        return total_label, current_label

    def create_display_frame(self):
        frame = tk.Frame(self.window, 
                         height=100, 
                         bg=self.current_theme["bg"])

        frame.pack(expand=True, fill="both")

        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)

        frame.pack(expand=True, fill="both")

        return frame

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame,
                                text=str(digit), 
                                bg=self.current_theme["button_bg"], 
                                fg=self.current_theme["button_fg"], 
                                font=("Arial", 25),
                                borderwidth=0,
                                activebackground=self.current_theme["button_active_bg"],
                                activeforeground=self.current_theme["button_active_fg"],
                                command=lambda x=digit: self.AddToExpression(value=x))

            button.grid(row=grid_value[0], 
                        column=grid_value[1], 
                        sticky=tk.NSEW)

    def UpdateCurrentState(self) -> str:
        self.current_label.config(text=self.current_expression)
        return "Current State Updated"

    def UpdateTotalState(self) -> str:
        self.total_label.config(text=self.total_expression)
        return "Total State Updated"

    def AddToExpression(self, value) -> None:
        self.current_expression += str(value)
        self.UpdateCurrentState()

    def ClearState(self):
        self.current_expression = ""
        self.total_expression = ""
        self.UpdateCurrentState()
        self.UpdateTotalState()

    def AppendOperator(self, operator) -> None:
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.UpdateCurrentState()
        self.UpdateTotalState()

    def EvaluateExpression(self):
        self.total_expression += self.current_expression
        self.UpdateTotalState()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except ZeroDivisionError:
            self.current_expression = "Division by zero is not allowed"
        except SyntaxError:
            self.current_expression = "Invalid syntax"
        except Exception as e:
            self.current_expression = f"Error: {str(e)}"
        finally:
            self.UpdateCurrentState()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame,
                               text=symbol,
                               bg=self.current_theme["button_bg"],
                               fg=self.current_theme["button_fg"],
                               font=("Arial", 25),
                               borderwidth=0,
                               activebackground=self.current_theme["button_active_bg"],
                               activeforeground=self.current_theme["button_active_fg"],
                               command=lambda x=operator: self.AppendOperator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame,
                           text="=",
                           bg=self.current_theme["button_active_bg"],
                           fg=self.current_theme["button_fg"],
                           font=("Arial", 25),
                           borderwidth=0,
                           activebackground=self.current_theme["button_active_bg"],
                           activeforeground=self.current_theme["button_active_fg"],
                           command=self.EvaluateExpression)
        button.grid(row=4,
                    column=3, 
                    columnspan=2, 
                    sticky=tk.NSEW)

    def create_clear_button(self):
        # Set the "Clear" button to have a fixed light red background
        button = tk.Button(self.buttons_frame,
                           text="C",
                           bg="#facfcf",  # Light red background color
                           fg=self.current_theme["button_fg"],
                           font=("Arial", 25),
                           borderwidth=0,
                           activebackground="#facfcf",  # Light red active background
                           activeforeground=self.current_theme["button_fg"],
                           command=self.ClearState)
        button.grid(row=0,
                    column=1,
                    sticky=tk.NSEW)

    def create_advanced_buttons(self):
        button = tk.Button(self.buttons_frame,
                           text="√",
                           bg=self.current_theme["button_bg"],
                           fg=self.current_theme["button_fg"],
                           font=("Arial", 25),
                           borderwidth=0,
                           activebackground=self.current_theme["button_active_bg"],
                           activeforeground=self.current_theme["button_active_fg"],
                           command=self.handle_square_root)
        button.grid(row=0, 
                    column=2, 
                    sticky=tk.NSEW)

        button = tk.Button(self.buttons_frame,
                           text="%",
                           bg=self.current_theme["button_bg"],
                           fg=self.current_theme["button_fg"],
                           font=("Arial", 25),
                           borderwidth=0,
                           activebackground=self.current_theme["button_active_bg"],
                           activeforeground=self.current_theme["button_active_fg"],
                           command=self.handle_percentage)
        button.grid(row=0,
                    column=3,
                    sticky=tk.NSEW)

    def handle_square_root(self):
        try:
            self.current_expression = str(math.sqrt(float(self.current_expression)))
        except ValueError:
            self.current_expression = "Error"
        self.UpdateCurrentState()

    def handle_percentage(self):
        try:
            self.current_expression = str(float(self.current_expression) / 100)
        except ValueError:
            self.current_expression = "Error"
        self.UpdateCurrentState()

    def create_toggle_button(self):
        toggle_button = tk.Button(self.window,
                                  text="Toggle Theme",
                                  bg=self.current_theme["button_bg"],
                                  fg=self.current_theme["button_fg"],
                                  font=("Arial", 20),
                                  command=self.toggle_theme)
        toggle_button.pack(pady=10)

    def toggle_theme(self):
        if self.current_theme == LIGHT_THEME:
            self.current_theme = DARK_THEME
        else:
            self.current_theme = LIGHT_THEME

        # Update the entire UI to reflect the new theme
        self.update_ui()

    def update_ui(self):
        # Update display and labels with the new theme
        self.window.configure(bg=self.current_theme["bg"])
        self.display_frame.configure(bg=self.current_theme["bg"])
        self.total_label.configure(bg=self.current_theme["bg"], fg=self.current_theme["fg"])
        self.current_label.configure(bg=self.current_theme["bg"], fg=self.current_theme["fg"])

        # Update buttons with the new theme except for Equals and Clear buttons
        for widget in self.buttons_frame.winfo_children():
            if widget["text"] != "=" and widget["text"] != "C":
                widget.configure(bg=self.current_theme["button_bg"], 
                                 fg=self.current_theme["button_fg"],
                                 activebackground=self.current_theme["button_active_bg"],
                                 activeforeground=self.current_theme["button_active_fg"])

    def run(self):
        """
        Start the main event loop for the calculator application.

        This method initiates the Tkinter main loop, which handles all GUI events
        and keeps the application window open until it is closed by the user.

        Parameters:
        None

        Returns:
        None
        """
        self.window.mainloop()


# Create and run the calculator
calculator = Calculator()
calculator.run()
