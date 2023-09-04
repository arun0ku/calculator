import tkinter as tk
import customtkinter as ctk
# from tkinter import messagebox

def main():
    win = ctk.CTk()
    app = Calculator(win)
    win.mainloop()

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title('Calculator')
        self.root.resizable(0,0)
        self.input_limit = 15
        ctk.CTkFrame(self.root, width=325, height=410, fg_color='black').pack()

        self.result_var = tk.StringVar()
        self.result_var.set('0')
        self.lbl = ctk.CTkLabel(self.root, textvariable=self.result_var, width=315, fg_color='black', height=80, font=('Calibri',48), anchor='ne').place(x=5, y=5)

        self.result = tk.StringVar()
        self.result.set('0')
        ctk.CTkLabel(master=self.lbl, textvariable=self.result, width=315, height=50, fg_color='black', font=('Calibri',32), anchor='e', text='0', bg_color='black').place(x=5, y=55)

        ctk.CTkButton(self.root, text='AC', width=0, height=50, font=('Agency FB',22, 'bold'), hover_color='grey', text_color='black', fg_color='#BDBDBD', bg_color='black', corner_radius=80, command=self.clear).place(x=10, y=110)
        ctk.CTkButton(self.root, text='7', width=0, height=50, font=('Calibri',28), hover_color='grey', text_color='white', fg_color='#595959', bg_color='black', corner_radius=80, command=lambda :self.get_digit('7')).place(x=10, y=170)
        ctk.CTkButton(self.root, text='4', width=0, height=50, font=('Calibri',28), hover_color='grey', text_color='white', fg_color='#595959', bg_color='black', corner_radius=80, command=lambda :self.get_digit('4')).place(x=10, y=230)
        ctk.CTkButton(self.root, text='1', width=0, height=50, font=('Calibri',28), hover_color='grey', text_color='white', fg_color='#595959', bg_color='black', corner_radius=80, command=lambda :self.get_digit('1')).place(x=10, y=290)

        ctk.CTkButton(self.root, text='±', width=0, height=50, font=('Calibri',28), hover_color='grey', text_color='black', fg_color='#BDBDBD', bg_color='black', corner_radius=80, command=self.change_sign).place(x=92, y=110)
        ctk.CTkButton(self.root, text='8', width=0, height=50, font=('Calibri',28), hover_color='grey', text_color='white', fg_color='#595959', bg_color='black', corner_radius=80, command=lambda :self.get_digit('8')).place(x=90, y=170)
        ctk.CTkButton(self.root, text='5', width=0, height=50, font=('Calibri',28), hover_color='grey', text_color='white', fg_color='#595959', bg_color='black', corner_radius=80, command=lambda :self.get_digit('5')).place(x=90, y=230)
        ctk.CTkButton(self.root, text='2', width=0, height=50, font=('Calibri',28), hover_color='grey', text_color='white', fg_color='#595959', bg_color='black', corner_radius=80, command=lambda :self.get_digit('2')).place(x=90, y=290)

        ctk.CTkButton(self.root, text='%', width=0, height=50, font=('Calibri',24), hover_color='grey', text_color='black', fg_color='#BDBDBD', bg_color='black', corner_radius=80, command=lambda :self.get_digit('%')).place(x=170, y=110)
        ctk.CTkButton(self.root, text='9', width=0, height=50, font=('Calibri',28), hover_color='grey', text_color='white', fg_color='#595959', bg_color='black', corner_radius=80, command=lambda :self.get_digit('9')).place(x=170, y=170)
        ctk.CTkButton(self.root, text='6', width=0, height=50, font=('Calibri',28), hover_color='grey', text_color='white', fg_color='#595959', bg_color='black', corner_radius=80, command=lambda :self.get_digit('6')).place(x=170, y=230)
        ctk.CTkButton(self.root, text='3', width=0, height=50, font=('Calibri',28), hover_color='grey', text_color='white', fg_color='#595959', bg_color='black', corner_radius=80, command=lambda :self.get_digit('3')).place(x=170, y=290)

        ctk.CTkButton(self.root, text='÷', width=0, height=50, font=('Calibri',28), hover_color='#FFB93C', text_color='white', fg_color='#FFA522', bg_color='black', corner_radius=80, command=lambda :self.get_digit('/')).place(x=250, y=110)
        ctk.CTkButton(self.root, text='x', width=0, height=50, font=('Calibri',28), hover_color='#FFB93C', text_color='white', fg_color='#FFA522', bg_color='black', corner_radius=80, command=lambda :self.get_digit('*')).place(x=250, y=170)
        ctk.CTkButton(self.root, text='-', width=0, height=50, font=('Calibri',36), hover_color='#FFB93C', text_color='white', fg_color='#FFA522', bg_color='black', corner_radius=80, command=lambda :self.get_digit('-')).place(x=250, y=230)
        ctk.CTkButton(self.root, text='+', width=0, height=50, font=('Calibri',28), hover_color='#FFB93C', text_color='white', fg_color='#FFA522', bg_color='black', corner_radius=80, command=lambda :self.get_digit('+')).place(x=250, y=290)

        ctk.CTkButton(self.root, text='0', width=145,  height=50, font=('Calibri',36), hover_color='grey', text_color='white', fg_color='#595959', bg_color='black', corner_radius=50, command=lambda :self.get_digit('0')).place(x=10, y=350)
        ctk.CTkButton(self.root, text='.', width=65, height=50, font=('Calibri',36,'bold'), hover_color='grey', text_color='white', fg_color='#595959', bg_color='black', corner_radius=80, command=lambda :self.get_digit('.')).place(x=170, y=350)
        ctk.CTkButton(self.root, text='=', width=0, height=50, font=('Calibri',28), hover_color='#FFB93C', text_color='white', fg_color='#FFA522', bg_color='black', corner_radius=80, command=lambda :self.get_digit('=')).place(x=250, y=350)


    def clear(self):
        self.result_var.set('0')
        self.result.set('0')

    def get_digit(self, text):
        if text == "=":
            try:
                result = eval(self.result_var.get())
                rslt = round(result,2)
                self.result.set(rslt)
            except ZeroDivisionError:
                # messagebox.showerror('Calculator','Cannot be divided by 0!',parent=self.root)
                self.result.set('Cannot be divided by 0!')
            except SyntaxError:
                self.result_var.set('0')
            except Exception:
                self.result_var.set('0')
        elif text in '+-*/':
            current_text = self.result_var.get()
            if len(current_text) == 0:
                return
            elif current_text[-1] in "+-*/":
                return
            else:
                self.result_var.set(current_text + str(text))
        elif text == '%':
            current_text = self.result_var.get()
            try:
                percentage = float(current_text) / 100
                self.result.set(str(percentage))
            except Exception:
                self.result_var.set('0')
        else:
            if len(self.result_var.get()) < self.input_limit:
                if text == '.' and '.' in self.result_var.get():
                    return  # Only allow one dot
                if self.result_var.get() == '0' and text != '.':
                    self.result_var.set(text)
                else:
                    self.result_var.set(self.result_var.get() + text)

    def change_sign(self):
        current_value = self.result_var.get()
        if current_value and current_value[0] == "-":
            self.new_value = current_value[1:]
            self.result_var.set(self.new_value)
        else:
            self.new_value = "-" + current_value
            self.result_var.set(self.new_value)

if __name__ == '__main__':
    main()