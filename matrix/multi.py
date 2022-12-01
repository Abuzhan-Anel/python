from tkinter import *
from tkinter.constants import BOTH
import menu

alphabet = 'abcdefghijklmnopqrstuvwxyz'


class Multi:
    def back_to_menu(self):
        self.gui_multi_output.destroy()
        menu.window.deiconify()

    def compute_product(self):
        try:
            for i in range(self.rows_a):
                for j in range(self.cols_a):
                    self.matrix_a[i][j] = int(self.matrix_a[i][j])

            for i in range(self.rows_b):
                for j in range(self.cols_b):
                    self.matrix_b[i][j] = int(self.matrix_b[i][j])

            self.product_matrix =  [[sum(a*b for a,b in zip(self.matrix_a_row,self.matrix_b_col)) for self.matrix_b_col in zip(*self.matrix_b)] for self.matrix_a_row in self.matrix_a]

        except (TypeError, Exception):
            pass

        try:
            list_mat = [str(i) for i in self.product_matrix]
            for i in range(len(list_mat)):
                list_mat[i] = list_mat[i][1:-1]

            return list_mat

        except (NameError, TypeError, Exception):
            pass

    def output_matrix(self):
        self.gui_multi_input.destroy()
        self.gui_multi_output = Toplevel()
        self.gui_multi_output.title("Multiply")
        self.gui_multi_output.resizable(False, False)

        self.frame_multi_output = Frame(self.gui_multi_output, highlightbackground='black', highlightthickness=1)
        self.frame_multi_output.pack(fill=BOTH, expand=True, padx=5, pady=5)

        Button(self.frame_multi_output, text="Back", width=4, command=self.back_to_menu).grid(row=self.rows_a + self.rows_b + 10,column=1)
        
        Label(self.frame_multi_output, text='Matrix A:', font=('arial', 10, 'bold')).grid(row=1, column=1)

        for i in range(self.rows_a):
            for j in range(self.cols_a):
                Label(self.frame_multi_output, text=self.matrix_a[i][j], bd=5).grid(row=i + 1, column=j + 2)

        Label(self.frame_multi_output, text='Matrix B:', font=('arial', 10, 'bold')).grid(row=1, column=self.cols_a + 2)

        for i in range(self.rows_b):
            for j in range(self.cols_b):
                Label(self.frame_multi_output, text=self.matrix_b[i][j], bd=5).grid(row=i + 1, column=j + self.cols_a * 2 + 2)

        Label(self.frame_multi_output, text='Product:', font=('arial', 10, 'bold')).grid(row=self.rows_a * 2,column=1)


        self.product_matrix = self.compute_product()

        for i in range(len(self.product_matrix)):
            Label(self.frame_multi_output, text=self.product_matrix[i], bd=5).grid(row=i + self.rows_a * 2, column=2, columnspan=5, sticky='w  ')

        self.gui_multi_output.protocol("WM_DELETE_WINDOW", menu.window.destroy)
        self.gui_multi_output.mainloop()

    def input_matrix(self):
        self.multiply.destroy()
        self.gui_multi_input = Toplevel()
        self.gui_multi_input.title("Multiply")
        self.gui_multi_input.resizable(False, False)

        self.frame_multi_input = Frame(self.gui_multi_input, highlightbackground='black', highlightthickness=1,bg='pink')
        self.frame_multi_input.pack(fill=BOTH, expand=True, padx=5, pady=5)

        Label(self.frame_multi_input, text="Enter matrix A:", font=('arial', 10, 'bold')).grid(row=1, column=1)
        text_var = []
        entries = []

        self.rows_a, self.cols_a = (self.ma_rows.get(), self.ma_cols.get())

        for i in range(self.rows_a):
            text_var.append([])
            entries.append([])
            for j in range(self.cols_a):
                if i == 1:
                    Label(self.frame_multi_input, text=alphabet[j]).grid(row=1, column=j + 2)

                text_var[i].append(StringVar())

                entries[i].append(Entry(self.frame_multi_input, textvariable=text_var[i][j], width=3))

                entries[i][j].grid(row=i + 2, column=j + 2)

                Label(self.frame_multi_input, text=i + 1).grid(row=i + 2, column=1, sticky='e')

        Label(self.frame_multi_input, text="Enter matrix B:", font=('arial', 10, 'bold')).grid(row=self.rows_a * 2,column=1)

        text_var_b = []
        entries_b = []

        self.rows_b, self.cols_b = (self.ma_cols.get(), self.mb_cols.get())
        for i in range(self.rows_b):
            text_var_b.append([])
            entries_b.append([])
            for j in range(self.cols_b):
                if i == 1:
                    Label(self.frame_multi_input, text=alphabet[j]).grid(row=self.rows_a * 2, column=j + 2)
                text_var_b[i].append(StringVar())
                entries_b[i].append(Entry(self.frame_multi_input, textvariable=text_var_b[i][j], width=3))
                entries_b[i][j].grid(row=i + self.rows_a + 5, column=j + 2)
                Label(self.frame_multi_input, text=i + 1).grid(row=i + self.rows_a + 5, column=1, sticky='e')

        def get_mat_a():
            self.matrix_a = []
            for i2 in range(self.rows_a):
                self.matrix_a.append([])
                for j2 in range(self.cols_a):
                    self.matrix_a[i2].append(text_var[i2][j2].get())

        def get_mat_b():
            self.matrix_b = []
            for i3 in range(self.rows_b):
                self.matrix_b.append([])
                for j3 in range(self.cols_b):
                    self.matrix_b[i3].append(text_var_b[i3][j3].get())

        def get_mat():
            try:
                get_mat_a()
                get_mat_b()
                self.output_matrix()
            except (ValueError, Exception):
                pass
            
        Button(self.frame_multi_input, text="Enter", width=8, command=get_mat).grid(row=self.cols_a + self.cols_b + 10,column=1)

        self.gui_multi_input.protocol("WM_DELETE_WINDOW", menu.window.destroy)
        self.gui_multi_input.mainloop()

    def __init__(self):
        self.product_matrix = None
        self.matrix_a, self.matrix_b = None, None
        self.matrix = None
        self.gui_multi_input = None
        self.frame_multi_input = None
        self.rows_a, self.cols_a = None, None
        self.rows_b, self.cols_b = None, None
        self.gui_multi_output = None
        self.frame_multi_output = None

        menu.window.withdraw()
        self.multiply = Toplevel()
        self.multiply.title("Multiply")
        self.multiply.resizable(False, False)

        self.frame_multiply = Frame(self.multiply, highlightbackground='black', highlightthickness=1)
        self.frame_multiply.pack(fill=BOTH, expand=True, padx=5, pady=5)

        Label(self.frame_multiply, text='Matrix A dimensions:', font=('arial', 10, 'bold')).grid(row=3, column=1,columnspan=1)
        Label(self.frame_multiply, text='Matrix B dimensions:', font=('arial', 10, 'bold')).grid(row=4, column=1,columnspan=1)

        self.ma_rows = IntVar()
        self.ma_rows.set(2)

        OptionMenu(self.frame_multiply, self.ma_rows, *range(2, 5)).grid(row=3, column=2)

        Label(self.frame_multiply, text='x').grid(row=3, column=3)

        self.ma_cols = IntVar()
        self.ma_cols.set(2)
        OptionMenu(self.frame_multiply, self.ma_cols, *range(2, 5)).grid(row=3, column=4)

        self.mb_rows = IntVar()
        Label(self.frame_multiply, text="[n]", font=('arial', 10, 'bold'), padx=5, pady=5).grid(row=4, column=2)

        Label(self.frame_multiply, text='x').grid(row=4, column=3)

        self.mb_cols = IntVar()
        self.mb_cols.set(2)
        OptionMenu(self.frame_multiply, self.mb_cols, *range(2, 5)).grid(row=4, column=4)

        Button(self.frame_multiply, text='Enter', padx=16, pady=5, command=self.input_matrix).grid(row=5, column=4)
        self.multiply.protocol("WM_DELETE_WINDOW", menu.window.destroy)
        self.multiply.mainloop()
