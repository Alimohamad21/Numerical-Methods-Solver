import sys
import tkinter
import tkinter as tk
import tkinter.font as font
from tkinter.filedialog import askopenfilename

sys.path.append("/Numerical-Methods-Solver/lib/")
from root_solving_methods import *
import gauss_methods as gm

root_finding_methods = {'Fixed Point': fixed_point, 'Newton Raphson': newton_raphson, 'Bisection Method': bisection}


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_initial_guess2 = True
        self.create_extras = True
        self.mainwindow()
        self.loaded_file=False
        self.file_result=dict()
        #self.readFile()
        #self.create_widgets()

    def mainwindow(self):
        self.mainlabel = tk.Label(self, text='Please Choose Type Of Equation:', bg='white')
        self.mainlabel.grid(row=0, column=0, columnspan=10)
        self.rooteqs = tk.Button(self, text='Root Equations',
                                 command=lambda: [self.create_widgets(), self.lineareqs.destroy()], height=1,
                                 width=15, bg='#33FF4E')
        self.rooteqs.grid(row=1, column=0, columnspan=5)
        self.lineareqs = tk.Button(self, text='Linear Equations',
                                   command=lambda: [self.linear_eqs_menu(), self.rooteqs.destroy(),
                                                    self.mainlabel.destroy(), self.lineareqs.destroy()], height=1,
                                   width=15, bg='#33FF4E')
        self.lineareqs.grid(row=1, column=10, columnspan=5)

    def linear_eqs_menu(self):
        self.linear_label = tk.Label(self, text='Please Choose Linear Equations Method:', bg='white')
        self.linear_label.grid(row=0, column=0, columnspan=10)
        self.gauss_elim_button = tk.Button(self, text='Gauss Elimination',
                                           command=lambda: [self.gauss_eqs_number(), self.gauss_seidel_button.destroy(),
                                                            self.gauss_elim_button.destroy(),
                                                            self.linear_label.destroy()], height=1,
                                           width=15, bg='#33FF4E')
        self.gauss_elim_button.grid(row=1, column=0, columnspan=5)
        self.gauss_seidel_button = tk.Button(self, text='Gauss Seidel', command=lambda: [self.gauss_seidel_epsilon(),
                                                                                         self.gauss_elim_button.destroy(),
                                                                                         self.linear_label.destroy(),
                                                                                         self.gauss_seidel_button.destroy()],
                                             height=1,
                                             width=15, bg='#33FF4E')
        self.gauss_seidel_button.grid(row=1, column=10, columnspan=5)
        self.readfile=False

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
        self.file_button = tk.Button(self, text='Load File', command=self.load_file, font=self.my_font2, height=self.h,
                                     width=self.w * 2, bg='#33FAEA')
        self.file_button.grid(row=9, column=0, columnspan=5, pady=(10, 10))

    def parse(self):
        lines = self.file_contents['text'].split('\n')
        result=''
        equation = lines[0]
        method_name = lines[1]
        interval = lines[2].split(' ')
        iter_or_epsilon = lines[3]
        if iter_or_epsilon.find('.') == -1:
            iter_or_epsilon = int(iter_or_epsilon)
        else:
            iter_or_epsilon = float(iter_or_epsilon)
        if "bisection" in method_name.lower():
            if type(iter_or_epsilon) == float:
                result = root_finding_methods['Bisection Method'](equation, float(interval[0]), float(interval[1]), epsilon=iter_or_epsilon)
            else:
                result = root_finding_methods['Bisection Method'](equation, float(interval[0]), float(interval[1]), max_iterations=iter_or_epsilon)
        elif "newton" in method_name.lower():
            if type(iter_or_epsilon) == float:
                result = root_finding_methods['Newton Raphson'](equation, float(interval[0]), epsilon=iter_or_epsilon)
            else:
                result = root_finding_methods['Newton Raphson'](equation, float(interval[0]), max_iterations=iter_or_epsilon)
        elif "fixed" in method_name.lower():
            if type(iter_or_epsilon) == float:
                result = root_finding_methods['Fixed Point'](equation, float(interval[0]), epsilon=iter_or_epsilon)
            else:
                result = root_finding_methods['Fixed Point'](equation, float(interval[0]), max_iterations=iter_or_epsilon)
        self.file_result=result

    def load_file(self):
        self.file_name = tkinter.filedialog.askopenfilename()
        self.file_contents = tk.Label(self, text='', bg='white', font=self.my_font)
        self.file_contents.grid(row=10, column=0, columnspan=10)
        f = open(self.file_name)
        for line in f:
            self.file_contents['text'] += line
        self.loaded_file=True
        self.parse()
        self.show_file_result()



    def append_output_equation(self, input):
        self.output_equation['text'] += input

    def show_result(self):
        self.open_new_window()
        self.iterations = tk.Label(self.new_window, text='', bg='white', font=self.my_font)
        self.iterations.grid(row=0, column=0, columnspan=10)
        self.final_answer = tk.Label(self.new_window, text='', font=self.my_font)
        self.final_answer.grid(row=1, column=3, columnspan=5)
        self.execution_time = tk.Label(self.new_window, text='', font=self.my_font)
        self.execution_time.grid(row=2, column=3, columnspan=5)
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

    def show_file_result(self):
        self.open_new_window()
        self.iterations = tk.Label(self.new_window, text='', bg='white', font=self.my_font)
        self.iterations.grid(row=0, column=0, columnspan=10)
        self.final_answer = tk.Label(self.new_window, text='', font=self.my_font)
        self.final_answer.grid(row=1, column=3, columnspan=5)
        self.execution_time = tk.Label(self.new_window, text='', font=self.my_font)
        self.execution_time.grid(row=2, column=3, columnspan=5)
        self.iterations['text'] = self.file_result['Iterations']
        self.final_answer['text'] = 'Final Answer:' + self.file_result['Final Answer']
        self.execution_time['text'] = 'Execution Time:' + self.file_result['Execution Time']

    def popupmsg(self, msg):
        self.popup = tk.Toplevel(self)
        self.popup.wm_title("!")
        self.label = tk.Label(self.popup, text=msg)
        self.label.pack(side="top", fill="x", pady=10)
        self.B1 = tk.Button(self.popup, text="Okay", command=self.popup.destroy)
        self.B1.pack()
        self.popup.mainloop()

    def gauss_elimination(self,n):
        self.open_new_window()
        if self.readfile==False:
            list1=[]
            for i in range(len(self.entries)):
                list1.append(self.entries[i].get())
            x=gm.gauss_elimination_calc(self.new_window,list1,n)
        else:
             x=gm.gauss_elimination_calc(self.new_window,self.entries,n)
        for i in range(n):
            self.x = tk.Label(self.new_window, text='x{}={:.3f} '.format(i+1,x[i]), height=1, width=10)
            self.x.grid(row=12, column=0+i,sticky='nesw', pady=(10, 10))

    def gauss_seidel(self,epsilon):
        if self.readfile==False:
            self.x1=float(self.x1_entry.get())
            self.x2=float(self.x2_entry.get())
            self.x3=float(self.x3_entry.get())
            list1=[]
            for i in range(len(self.entries)):
                list1.append(self.entries[i].get())
            iterations=gm.gauss_seidel_calc(self,list1,epsilon,self.x1,self.x2,self.x3)
        else:
            iterations=gm.gauss_seidel_calc(self,self.entries,epsilon,self.x1,self.x2,self.x3)
        self.open_new_window()
        self.iterations = tk.Label(self.new_window, text=iterations, bg='white')
        self.iterations.grid(row=0, column=0, columnspan=10)

    def gauss_seidel_epsilon(self):
        self.x1,self.x2,self.x3=0,0,0
        self.epsilon_label = tk.Label(self, text='Please Insert Initial Values:', height=1, width=20)
        self.epsilon_label.grid(row=0, column=1, sticky='nesw', pady=(10, 10))
        self.x1_label = tk.Label(self, text='x1:')
        self.x1_label.grid(row=1, column=0, sticky='nesw', pady=(10, 10))
        self.x1_entry=tk.Entry(self)
        self.x1_entry.grid(row=1,column=1,pady=(10,10))
        self.x2_label = tk.Label(self, text='x2:')
        self.x2_label.grid(row=1, column=2, sticky='nesw', pady=(10, 10))
        self.x2_entry=tk.Entry(self)
        self.x2_entry.grid(row=1,column=3,pady=(10,10))
        self.x3_label = tk.Label(self, text='x3:')
        self.x3_label.grid(row=1, column=4, sticky='nesw', pady=(10, 10))
        self.x3_entry=tk.Entry(self)
        self.x3_entry.grid(row=1,column=5,pady=(10,10))
        self.epsilon1_label = tk.Label(self, text='epsilon:')
        self.epsilon1_label.grid(row=1, column=6, sticky='nesw', pady=(10, 10))
        self.epsilon1_entry=tk.Entry(self)
        self.epsilon1_entry.grid(row=1,column=7,pady=(10,10))
        self.epsilon_button = tk.Button(self, text='Confirm', command=lambda:[self.gauss(3,self.epsilon1_entry.get()),self.epsilon_label.destroy(),
                                self.x1_label.destroy(),self.x1_entry.grid(row=1,column=0,pady=(10,10)),
                                self.x2_label.destroy(),self.x2_entry.grid(row=1,column=0,pady=(10,10)),
                                self.x3_label.destroy(),self.x3_entry.grid(row=1,column=0,pady=(10,10)),self.epsilon_button.destroy()], height=1,
                                width=4 * 2, bg='#33FF4E')
        self.epsilon_button.grid(row=1,column=8,columnspan=5)

    def gauss_eqs_number(self):
        self.eqs_num_label = tk.Label(self, text='Please Insert Number of Equations:', height=1, width=30)
        self.eqs_num_label.grid(row=0, column=0, sticky='nesw', pady=(10, 10))
        self.eqs_entry=tk.Entry(self)
        self.eqs_entry.grid(row=0,column=10,columnspan=2,pady=(10,10))
        self.eqs_num_button = tk.Button(self, text='Confirm', command=lambda:[self.gauss(self.eqs_entry.get(),0),self.eqs_num_label.destroy(),
                                self.eqs_entry.destroy(),self.eqs_num_button.destroy()], height=1,
                                width=4 * 2, bg='#33FF4E')
        self.eqs_num_button.grid(row=0,column=15,columnspan=5)

    def gauss(self,n,epsilon):
        try:
            n=int(n)
        except:
            self.popupmsg("Please Insert Integer Value!")
        try:
            epsilon=float(epsilon)
        except:
            self.popupmsg("Please Insert Float Value!")
        self.toplabel = tk.Label(self, text='Please Insert Coefficients:', height=1, width=20)
        self.toplabel.grid(row=0, column=5, sticky='nesw', pady=(10, 10))
        self.entries=[]
        for i in range(n):
            for j in range(0,2*n,2):
                self.label1 = tk.Label(self, text='x{}:'.format(1+j//2), height=1, width=4)
                self.gauss_entry= tk.Entry(self)
                self.entries.append(self.gauss_entry)
                self.label1.grid(row=1+i, column=j, sticky='nesw', pady=(10, 10))
                self.gauss_entry.grid(row=1+i, column=j+1, columnspan=2, pady=(10, 10))
            self.label1 = tk.Label(self, text='=', height=1, width=4)
            self.gauss_entry = tk.Entry(self)
            self.entries.append(self.gauss_entry)
            self.label1.grid(row=1+i, column=j+2, sticky='nesw', pady=(10, 10))
            self.gauss_entry.grid(row=1+i, column=j+3,columnspan=2, pady=(10, 10))
        if epsilon==0:
            self.confirm = tk.Button(self, text='Calculate', command=lambda:self.gauss_elimination(n), height=1,
                                width=4 * 2, bg='#33FF4E') 
        else: 
            self.confirm = tk.Button(self, text='Calculate', command=lambda:self.gauss_seidel(epsilon), height=1,
                                width=4 * 2, bg='#33FF4E') 
        self.confirm.grid(row=1+i,column=15,columnspan=5)

    def show_extra_buttons(self):
        try:
            self.file_button.destroy()
            self.file_contents.destroy()
        except:
            pass
        if self.choices.get() == 'Bisection Method':
            if self.create_initial_guess2:
                self.label4 = tk.Label(self, font=self.my_font2, text='guess 2:', height=self.h, width=self.w)
                self.initial_guess2 = tk.Entry(self, font=self.my_font2)
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
            self.initial_guess = tk.Entry(self, font=self.my_font2)
            self.label2 = tk.Label(self, font=self.my_font2, text='iterations:', height=self.h, width=self.w * 2)
            self.max_iterations = tk.Entry(self, font=self.my_font2)
            self.label3 = tk.Label(self, font=self.my_font2, text='epsilon:', height=self.h, width=self.w)
            self.epsilon = tk.Entry(self, font=self.my_font2)
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

    def open_new_window(self):
        self.new_window = tk.Toplevel(self)
        self.new_window.title("Results")
        self.new_window.geometry("1100x550")
    def readFile(self):
        file1=open("TextFileName.txt","r")
        list1=file1.readlines()
        self.entries=[]
        self.readfile=True
        #coefflist=[]
        for i in range(int(list1[0])):
            coefflist=list1[i+2].split()
            for j in range(int(list1[0])):
                if chr(ord('`')+j+1) in list1[i+2]:
                    for k in range(len(coefflist)):
                        if chr(ord('`')+j+1) in coefflist[k]:
                            end = coefflist[k].find("{}".format(chr(ord('`')+j+1)))
                            if coefflist[k][0:end-1]=='':
                                self.entries.append(1)
                            else:
                                self.entries.append(float(coefflist[k][0:end-1]))
                            break
                else:
                    self.entries.append(0)
            print(coefflist[-1])
            self.entries.append(float(coefflist[-1]))
        list1[1]=list1[1].split()[0]
        if list1[1]=='Gaussian-elimination':
            list1[0]=list1[0].split()[0]
            self.gauss_elimination(int(list1[0]))
        else:
            s=list1[-1].split()
            self.x1=float(s[0])
            self.x2=float(s[1])
            self.x3=float(s[2])
            self.gauss_seidel(0.00001)


root = tk.Tk()
root.geometry('700x550')
app = Application(master=root)
app.mainloop()

