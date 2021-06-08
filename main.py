import tkinter as tk
import tkinter.font as font
from tkinter.ttk import *
from root_solving_methods import *

root_finding_methods = {'Fixed Point': fixed_point, 'Newton Raphson': newton_raphson, 'Bisection Method': bisection}


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_initial_guess2 = True
        self.create_extras = True
        self.create_widgets()

    def create_operands(self):
        self.zero = tk.Button(self, text='0', command=lambda: self.append_output_equation('0'), font=self.my_font,
                              height=self.h, width=self.w, bg='blue')
        self.zero.grid(row=1, column=0, sticky='nesw')
        self.one = tk.Button(self, text='1', command=lambda: self.append_output_equation('1'), font=self.my_font,
                             height=self.h, width=self.w, bg='blue')
        self.one.grid(row=1, column=1, sticky='nesw')
        self.two = tk.Button(self, text='2', command=lambda: self.append_output_equation('2'), font=self.my_font,
                             height=self.h, width=self.w, bg='blue')
        self.two.grid(row=1, column=2, sticky='nesw')
        self.three = tk.Button(self, text='3', command=lambda: self.append_output_equation('3'), font=self.my_font,
                               height=self.h, width=self.w, bg='blue')
        self.three.grid(row=1, column=3, sticky='nesw')
        self.four = tk.Button(self, text='4', command=lambda: self.append_output_equation('4'), font=self.my_font,
                              height=self.h, width=self.w, bg='blue')
        self.four.grid(row=1, column=4, sticky='nesw')
        self.five = tk.Button(self, text='5', command=lambda: self.append_output_equation('5'), font=self.my_font,
                              height=self.h, width=self.w, bg='blue')
        self.five.grid(row=2, column=0, sticky='nesw')
        self.six = tk.Button(self, text='6', command=lambda: self.append_output_equation('6'), font=self.my_font,
                             height=self.h, width=self.w, bg='blue')
        self.six.grid(row=2, column=1, sticky='nesw')
        self.seven = tk.Button(self, text='7', command=lambda: self.append_output_equation('7'), font=self.my_font,
                               height=self.h, width=self.w, bg='blue')
        self.seven.grid(row=2, column=2, sticky='nesw')
        self.eight = tk.Button(self, text='8', command=lambda: self.append_output_equation('8'), font=self.my_font,
                               height=self.h, width=self.w, bg='blue')
        self.eight.grid(row=2, column=3, sticky='nesw')
        self.nine = tk.Button(self, text='9', command=lambda: self.append_output_equation('9'), font=self.my_font,
                              height=self.h, width=self.w, bg='blue')
        self.nine.grid(row=2, column=4, sticky='nesw')
        self.cos = tk.Button(self, text='cos', command=lambda: self.append_output_equation('cos('), font=self.my_font,
                             height=self.h, width=self.w, bg='purple')
        self.cos.grid(row=3, column=0, sticky='nesw')
        self.sin = tk.Button(self, text='sin', command=lambda: self.append_output_equation('sin('), font=self.my_font,
                             height=self.h, width=self.w, bg='purple')
        self.sin.grid(row=3, column=1, sticky='nesw')
        self.tan = tk.Button(self, text='tan', command=lambda: self.append_output_equation('tan('), font=self.my_font,
                             height=self.h, width=self.w, bg='purple')
        self.tan.grid(row=3, column=2, sticky='nesw')
        self.e = tk.Button(self, text='e', command=lambda: self.append_output_equation('exp('), font=self.my_font,
                           height=self.h, width=self.w, bg='purple')
        self.e.grid(row=3, column=3, sticky='nesw')
        self.x = tk.Button(self, text='x', command=lambda: self.append_output_equation('x'), font=self.my_font,
                           height=self.h, width=self.w, bg='purple')
        self.x.grid(row=3, column=4, sticky='nesw')
        self.ln = tk.Button(self, text='ln', command=lambda: self.append_output_equation('ln('), font=self.my_font,
                            height=self.h, width=self.w, bg='purple')
        self.ln.grid(row=4, column=0, sticky='nesw')

    def create_operations(self):
        self.plus = tk.Button(self, text='+', command=lambda: self.append_output_equation('+'), font=self.my_font,
                              height=self.h, width=self.w, bg='orange')
        self.plus.grid(row=4, column=1, sticky='nesw')
        self.minus = tk.Button(self, text='-', command=lambda: self.append_output_equation('-'), font=self.my_font,
                               height=self.h, width=self.w, bg='orange')
        self.minus.grid(row=4, column=2, sticky='nesw')
        self.multipy = tk.Button(self, text='*', command=lambda: self.append_output_equation('*'), font=self.my_font,
                                 height=self.h, width=self.w, bg='orange')
        self.multipy.grid(row=4, column=3, sticky='nesw')
        self.divide = tk.Button(self, text='/', command=lambda: self.append_output_equation('/'), font=self.my_font,
                                height=self.h, width=self.w, bg='orange')
        self.divide.grid(row=4, column=4, sticky='nesw')
        self.power = tk.Button(self, text='^', command=lambda: self.append_output_equation('^'), font=self.my_font,
                               height=self.h, width=self.w, bg='orange')
        self.power.grid(row=5, column=0, sticky='nesw')
        self.bracket = tk.Button(self, text='(', command=lambda: self.append_output_equation('('), font=self.my_font,
                                 height=self.h, width=self.w, bg='orange')
        self.bracket.grid(row=5, column=1, sticky='nesw')
        self.bracket2 = tk.Button(self, text=')', command=lambda: self.append_output_equation(')'), font=self.my_font,
                                  height=self.h, width=self.w, bg='orange')
        self.bracket2.grid(row=5, column=2, sticky='nesw')

    def create_widgets(self):
        self.h = 1
        self.w = 4
        self.size = 12
        self.my_font = font.Font(family='Helvetica', size=self.size, weight='bold')
        self.my_font2 = font.Font(family='Helvetica', size=self.size - 2, weight='bold')
        self.my_font3 = font.Font(family='Helvetica', size=self.size - 5, weight='bold')
        self.output_equation = tk.Label(self, bg='white', font=self.my_font, width=self.w * 6, height=self.h + 1)
        self.output_equation.grid(row=0, column=0, columnspan=6, pady=(5, 5))
        self.create_operands()
        self.create_operations()
        self.delete_button = tk.Button(self, text='DEL', command=self.delete_output, font=self.my_font, height=self.h,
                                       width=self.w, bg='red')
        self.delete_button.grid(row=5, column=3, sticky='nesw')
        self.clear_button = tk.Button(self, text='AC', command=self.clear_output, font=self.my_font, height=self.h,
                                      width=self.w, bg='red')
        self.clear_button.grid(row=5, column=4, sticky='nesw')
        self.method = tk.Label(self, font=self.my_font2, text='Method:', height=self.h, width=self.w)
        self.method.grid(row=7, column=0, sticky='nesw', pady=(10, 10))
        self.choices = tk.StringVar(self)
        self.choices.set('Fixed Point')
        self.root_method = tk.OptionMenu(self, self.choices, *root_finding_methods.keys())
        self.root_method.config(font=self.my_font2, bg='#338EFF')
        self.root_method.grid(row=7, column=1, columnspan=5, pady=(10, 10))
        self.solve = tk.Button(self, text='solve', command=self.show_extra_buttons, font=self.my_font2, height=self.h,
                               width=self.w + 2, bg='#33FF4E')
        self.solve.grid(row=8, column=0, columnspan=5)
        self.iterations = tk.Label(self, text='', bg='white', font=self.my_font)
        self.iterations.grid(row=14, column=0, columnspan=5)
        self.final_answer = tk.Label(self, text='', bg='white', font=self.my_font)
        self.final_answer.grid(row=15, column=0, columnspan=5)
        self.execution_time = tk.Label(self, text='', bg='white', font=self.my_font)
        self.execution_time.grid(row=16, column=0, columnspan=5)

    def append_output_equation(self, input):
        self.output_equation['text'] += input

    def show_result(self):
        epsilon = self.epsilon.get()
        iterations = self.max_iterations.get()
        if iterations == '':
            iterations = 50
        else:
            iterations = int(iterations)
        if self.epsilon.get() == '':
            epsilon = 0.00001
        else:
            epsilon = float(epsilon)
        args = [self.output_equation['text'], float(self.initial_guess.get())]
        if self.choices.get() == 'Bisection Method':
            args.append(float(self.initial_guess2.get()))
        args.append(epsilon)
        args.append(iterations)
        result = root_finding_methods[self.choices.get()](*args)
        self.iterations['text'] = result['Iterations']
        self.final_answer['text'] = 'Final Answer:' + result['Final Answer']
        self.execution_time['text'] = 'Execution Time:' + result['Execution Time']

    def show_extra_buttons(self):
        if self.choices.get() == 'Bisection Method':
            if self.create_initial_guess2:
                self.label4 = tk.Label(self, font=self.my_font2, text='guess 2:', height=self.h, width=self.w)
                self.initial_guess2 = tk.Entry(self,font=self.my_font2)
                self.label4.grid(row=10, column=0, sticky='nesw', pady=(10, 10))
                self.initial_guess2.grid(row=10, column=1, columnspan=5, pady=(10, 10))
                self.create_initial_guess2 = False
        else:
            try:
                self.initial_guess2.destroy()
                self.label4.destroy()
                self.create_initial_guess2 = True
            except:
                pass
        if self.create_extras:
            self.label1 = tk.Label(self, font=self.my_font2, text='guess:', height=self.h, width=self.w)
            self.initial_guess = tk.Entry(self,font=self.my_font2)
            self.label2 = tk.Label(self, font=self.my_font2, text='iterations:', height=self.h, width=self.w * 2)
            self.max_iterations = tk.Entry(self,font=self.my_font2)
            self.label3 = tk.Label(self, font=self.my_font2, text='epsilon:', height=self.h, width=self.w)
            self.epsilon = tk.Entry(self,font=self.my_font2)
            self.confirm = tk.Button(self, text='Confirm', command=self.show_result, font=self.my_font2, height=self.h,
                                     width=self.w * 2, bg='#33FF4E')
            self.label1.grid(row=9, column=0, sticky='nesw', pady=(10, 10))
            self.initial_guess.grid(row=9, column=1, columnspan=5, pady=(10, 10))
            self.label2.grid(row=11, column=0, sticky='nesw', pady=(10, 10))
            self.max_iterations.grid(row=11, column=1, columnspan=5, pady=(10, 10))
            self.label3.grid(row=12, column=0, sticky='nesw', pady=(10, 10))
            self.epsilon.grid(row=12, column=1, columnspan=5, pady=(10, 10))
            self.confirm.grid(row=13, column=0, columnspan=5)
            self.create_extras = False

    def delete_output(self):
        self.output_equation['text'] = self.output_equation['text'][:-1]

    def clear_output(self):
        self.output_equation['text'] = ''


root = tk.Tk()
root.geometry('700x550')
app = Application(master=root)
app.mainloop()