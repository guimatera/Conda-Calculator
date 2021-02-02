# Author: Guilherme Matera

# Importing required packages.
import PySimpleGUI as sg

# Selecting a theme for calculator.
sg.theme('LightGreen3')

# Screen dimensons and fonts.
SCR_H = 15
font_input = 22
font = 20
style = 'Calibri'
size_buttons = 3

# Creating calculator object.
class calculator:
    def __init__(self):
        # Declaring lists of button keys.
        self.button_keys = ['DISP','PERCENT','SQRT','ALLCLEAR','BACKSPACE','SUM','MINUS','TIMES','DIVISION','DOT','EQUAL']
        self.button_numbers = ['SEVEN','EIGHT','NINE','ZERO','FOUR','FIVE','SIX','ONE','TWO','THREE']
        self.number = ['7','8','9','0','4','5','6','1','2','3']
        self.button_op = self.button_keys[1:3] + self.button_keys[5:9]
        self.op_symb = ['%','√','+','-','x','÷']
        # Layout.
        layout = [
            # Calculator ROW 1.
            [sg.Input('0', size = (SCR_H,2), font = (style, font_input), key = self.button_keys[0])],
            # Calculator ROW 2.
            [sg.Button('%', size = (size_buttons,0), font = (style, font), key = self.button_keys[1]),
            sg.Button('√', size = (size_buttons,0), font = (style, font), key = self.button_keys[2]),
            sg.Button('C', size = (size_buttons,0), font = (style, font), key = self.button_keys[3]),
            sg.Button('<', size = (size_buttons,0), font = (style, font), key = self.button_keys[4])],
            # Calculator ROW 3.
            [sg.Button('+', size = (size_buttons,0), font = (style, font), key = self.button_keys[5]),
            sg.Button('-', size = (size_buttons,0), font = (style, font), key = self.button_keys[6]),
            sg.Button('x', size = (size_buttons,0), font = (style, font), key = self.button_keys[7]),
            sg.Button('÷', size = (size_buttons,0), font = (style, font), key = self.button_keys[8])],
            # Calculator ROW 4.
            [sg.Button('7', size = (size_buttons,0), font = (style, font), key = self.button_numbers[0]),
            sg.Button('8', size = (size_buttons,0), font = (style, font), key = self.button_numbers[1]),
            sg.Button('9', size = (size_buttons,0), font = (style, font), key = self.button_numbers[2]),
            sg.Button('0', size = (size_buttons,0), font = (style, font), key = self.button_numbers[3])],
            # Calculator ROW 5.
            [sg.Button('4', size = (size_buttons,0), font = (style, font), key = self.button_numbers[4]),
            sg.Button('5', size = (size_buttons,0), font = (style, font), key = self.button_numbers[5]),
            sg.Button('6', size = (size_buttons,0), font = (style, font), key = self.button_numbers[6]),
            sg.Button('.', size = (size_buttons,0), font = (style, font), key = self.button_keys[9])],
            # Calculator ROW 6.
            [sg.Button('1', size = (size_buttons,0), font = (style, font), key = self.button_numbers[7]),
            sg.Button('2', size = (size_buttons,0), font = (style, font), key = self.button_numbers[8]),
            sg.Button('3', size = (size_buttons,0), font = (style, font), key = self.button_numbers[9]),
            sg.Button('=', size = (size_buttons,0), font = (style, font), key = self.button_keys[10])] 
        ]
        # Window
        self.windows = sg.Window('Conda Calculator').Layout(layout)
        # Auxiliar variables from class.
        self.answer = 0
        self.operations = ''
        # Timeout.
        self.windows.Read(timeout=1)
    # Declaring method of operations.
    def operation(self):
        if self.operations == '%':
            return float(self.answer)/100
        elif self.operations == '√':
            if float(self.answer) >= 0:
                return pow(float(self.answer),0.5)
            else:
                return 'ERROR: INV NUMB'
            return pow(float(self.answer), 0.5)
        elif self.operations == '+':
             return float(self.answer) + float(self.val[self.button_keys[0]])
        elif self.operations == '-':
            return float(self.answer) - float(self.val[self.button_keys[0]])
        elif self.operations == 'x':
            return float(self.answer) * float(self.val[self.button_keys[0]])
        elif self.operations == '÷':
            if float(self.val[self.button_keys[0]])!= 0:
                return float(self.answer) / float(self.val[self.button_keys[0]])
            else:
                return 'ERROR: DIV#/0'

    # Declaring method of program initialization.
    def running(self):
        while True:
            clicking, self.val = self.windows.Read()
            if clicking in (None, sg.WIN_CLOSED): # Closing app.
                break

            elif clicking in self.button_numbers: # NUMBERS button.
                for i in range(0,len(self.button_numbers)):
                    if clicking == self.button_numbers[i]:
                        if self.val[self.button_keys[0]] == '0':
                            self.windows[self.button_keys[0]].update(value = self.number[i])
                            break
                        else:
                            self.windows[self.button_keys[0]].update(value = self.val[self.button_keys[0]] + self.number[i])
            
            elif clicking in self.button_op[0:2]: # OPERATIONS (%,√) button.
                    self.answer = self.val[self.button_keys[0]]
                    self.windows[self.button_keys[0]].update(value = '')
                    for i in range(0,len(self.button_op)):
                        if clicking == self.button_op[i]:
                            self.operations = self.op_symb[i]
                            self.answer = calculator.operation(self)
                    self.windows[self.button_keys[0]].update(value = self.answer)
                    self.operations = ''
                    self.answer = 0

            elif clicking in self.button_op[2:]: # Any other OPERATIONS button.
                if self.operations != '':
                    self.answer = calculator.operation(self)
                else:
                    for i in range(0,len(self.button_op)):
                        if clicking == self.button_op[i]:
                            self.operations = self.op_symb[i]
                            self.answer = self.val[self.button_keys[0]]
                            self.windows[self.button_keys[0]].update(value = '')

            elif clicking in self.button_keys[10]: # EQUAL button.
                self.answer = calculator.operation(self)
                self.windows[self.button_keys[0]].update(value = self.answer)
                self.operations = ''
                self.answer = 0

            elif clicking == self.button_keys[3]: # ALLCLEAR button.
                self.answer = 0
                self.windows[self.button_keys[0]].update(value = self.answer)

            elif clicking == self.button_keys[4]: # BACKSPACE button.
                if self.val[self.button_keys[0]] != '0':
                    self.windows[self.button_keys[0]].update(value = self.val[self.button_keys[0]][:-1])

            else: # DOT button.
                if '.'  not in self.val[self.button_keys[0]]:
                    self.windows[self.button_keys[0]].update(value = self.val[self.button_keys[0]] + '.')
    
# Defining a variable as calculator object.
calcul = calculator()
# Running program.
calcul.running()
