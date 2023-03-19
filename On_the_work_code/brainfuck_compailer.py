import sys
import tkinter as tk
import pyperclip

class BrainfuckCompiler(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Brainfuck Compiler")
        self.pack()

        # Initialize the user interface
        self.create_widgets()

    def create_widgets(self):
        # Create a text box for inputting Brainfuck code
        self.input_box = tk.Text(self, height=10, width=50)
        self.input_box.pack(side=tk.TOP, padx=10, pady=10)

        # Create a button for compiling the Brainfuck code
        self.compile_button = tk.Button(self, text="Compile", command=self.compile_code)
        self.compile_button.pack(side=tk.TOP, padx=10, pady=5)

        # Create a text box for displaying the compiled Brainfuck code
        self.output_box = tk.Text(self, height=10, width=50)
        self.output_box.pack(side=tk.TOP, padx=10, pady=10)

        # Create a button for copying the compiled Brainfuck code to the clipboard
        self.copy_button = tk.Button(self, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Create a button for printing the compiled Brainfuck code to the command prompt
        self.print_button = tk.Button(self, text="Print to Command Prompt", command=self.print_to_command_prompt)
        self.print_button.pack(side=tk.RIGHT, padx=10, pady=5)

    def compile_code(self):
        # Get the Brainfuck code from the input text box
        code = self.input_box.get("1.0", tk.END)

        # Compile the Brainfuck code
        compiled_code = self.compile(code)

        # Display the compiled Brainfuck code in the output text box
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, compiled_code)

    def copy_to_clipboard(self):
        # Get the compiled Brainfuck code from the output text box
        compiled_code = self.output_box.get("1.0", tk.END)

        # Copy the compiled Brainfuck code to the clipboard
        pyperclip.copy(compiled_code)

    def print_to_command_prompt(self):
        # Get the compiled Brainfuck code from the output text box
        compiled_code = self.output_box.get("1.0", tk.END)

        # Print the compiled Brainfuck code to the command prompt
        print(compiled_code)

    def compile(self, code):
        # Brainfuck commands
        commands = "><+-.,[]"

        # Strip all non-command characters from the code
        code = "".join(filter(lambda x: x in commands, code))

        # Initialize the compiled code string
        compiled_code = ""

        # Translate each command to its equivalent Brainfuck code
        for char in code:
            if char == ">":
                compiled_code += ">"
            elif char == "<":
                compiled_code += "<"
            elif char == "+":
                compiled_code += "+"
            elif char == "-":
                compiled_code += "-"
            elif char == ".":
                compiled_code += "."
            elif char == ",":
                compiled_code += ","
            elif char == "[":
                compiled_code += "["
            elif char == "]":
                compiled_code += "]"
        

        def interpret(code):
            array = [0]
            pointerLocation = 0
            i = 0
            c = 0
            print(code)
            while i < len(code):
                if code[i] == '<':
                    if pointerLocation > 0:
                        pointerLocation -= 1
                elif code[i] == '>':
                    pointerLocation += 1
                    if len(array) <= pointerLocation:
                        array.append(0)
                elif code[i] == '+':
                    array[pointerLocation] += 1
                elif code[i] == '-':
                    if array[pointerLocation] > 0:
                        array[pointerLocation] -= 1
                elif code[i] == '.':
                    print(array[pointerLocation], chr(array[pointerLocation]))
                elif code[i] == ',':
                    x = input("Input:")
                    try:
                        y = int(x)
                    except ValueError:
                        y = ord(x)
                    array[pointerLocation] = y
                elif code[i] == '[':
                    if array[pointerLocation] == 0:
                        open_braces = 1
                        while open_braces > 0:
                            i += 1
                            if code[i] == '[':
                                open_braces += 1
                            elif code[i] == ']':
                                open_braces -= 1
                elif code[i] == ']':
                    # you don't need to check array[pointerLocation] because the matching '[' will skip behind this instruction if array[pointerLocation] is zero
                    open_braces = 1
                    while open_braces > 0:
                        i -= 1
                        if code[i] == '[':
                            open_braces -= 1
                        elif code[i] == ']':
                            open_braces += 1
                    # i still gets incremented in your main while loop
                    i -= 1
        return interpret(compiled_code)

if __name__ == "__main__":
    # Create the tkinter window
    root = tk.Tk()

    # Create the BrainfuckCompiler object
    compiler = BrainfuckCompiler(root)

    # Start the main loop
    compiler.mainloop()

