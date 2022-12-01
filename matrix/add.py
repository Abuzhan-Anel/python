from tkinter import*
from tkinter.constants import BOTH
import menu

alphabet = 'abcdefghijklmnopqrstuvwxyz'


class Add:
    def back_to_menu(self):
        self.add_output.destroy()
        menu.window.deiconify()

    def compute_sum(self):
        try:
            for i in range(self.rows_get):
                for j in range(self.cols_get):
                    self.matrix_a[i][j] = int(self.matrix_a[i][j])
            for i in range(self.rows_get):
                for j in range(self.cols_get):
                    self.matrix_b[i][j] = int(self.matrix_b[i][j])

            self.sum_matrix = ([[a + b for a, b in zip(j, l)] for j, l in zip(self.matrix_a, self.matrix_b)])

        except (TypeError, Exception):
            pass

        try:
            list_mat = [str(i) for i in self.sum_matrix]

            for i in range(len(list_mat)):
                list_mat[i] = list_mat[i][1:-1]

            return list_mat

        except (NameError, TypeError, Exception):
            pass

    def output_matrix(self):
        self.add_input.destroy()
        self.add_output = Toplevel()
        self.add_output.title("Add")
        self.add_output.resizable(False, False)

        self.frame_add_output = Frame(self.add_output, highlightbackground='black', highlightthickness=1)
        self.frame_add_output.pack(fill=BOTH, expand=True, padx=5, pady=5)

        Button(self.frame_add_output, text="Back", width=4, command=self.back_to_menu).grid(
            row=self.rows_get + self.rows_get + 10, column=1)

        Label(self.frame_add_output, text='Matrix A:', font=('arial', 10, 'bold')).grid(row=1, column=1)

        for i in range(self.rows_get):
            for j in range(self.cols_get):
                Label(self.frame_add_output, text=self.matrix_a[i][j], bd=5).grid(row=i+1, column=j+2)

        Label(self.frame_add_output, text='Matrix B:', font=('arial', 10, 'bold')).grid(row=1, column=self.cols_get+2)

        for i in range(self.rows_get):
            for j in range(self.cols_get):
                Label(self.frame_add_output, text=self.matrix_b[i][j], bd=5).grid(row=i+1, column=j+self.cols_get*2+2)

        Label(self.frame_add_output, text='Sum:', font=('arial', 10, 'bold')).grid(row=self.rows_get * 2,column=1)
        
        self.sum_matrix = self.compute_sum()

        for i in range(len(self.sum_matrix)):
            Label(self.frame_add_output, text=self.sum_matrix[i], bd=5).grid(
                row=i + self.rows_get * 2, column=2, columnspan=5, sticky='w  ')

        self.add_output.protocol("WM_DELETE_WINDOW", menu.window.destroy)
        self.add_output.mainloop()

    def input_matrix(self):
        self.add_menu.destroy()
        self.add_input = Toplevel()
        self.add_input.title("Add")
        self.add_input.resizable(False, False)

        self.frame_add_input = Frame(self.add_input, highlightbackground='black', highlightthickness=1)
        self.frame_add_input.pack(fill=BOTH, expand=True, padx=5, pady=5)

        Label(self.frame_add_input, text="Enter matrix A:", font=('arial', 10, 'bold')).grid(row=1, column=1)

        text_var = []
        entries = []

        self.rows_get, self.cols_get = (self.rows.get(), self.cols.get())

        for i in range(self.rows_get):
            text_var.append([])
            entries.append([])

            for j in range(self.cols_get):
                if i == 1:
                    Label(self.frame_add_input, text=alphabet[j]).grid(row=1, column=j + 2)

                text_var[i].append(StringVar())

                entries[i].append(Entry(self.frame_add_input, textvariable=text_var[i][j], width=3))

                entries[i][j].grid(row=i + 2, column=j + 2)


                Label(self.frame_add_input, text=i + 1).grid(row=i + 2, column=1, sticky='e')

        Label(self.frame_add_input, text="Enter matrix B:", font=('arial', 10, 'bold')).grid(row=self.rows_get * 2,column=1)
        text_var_b = []
        entries_b = []

        for i in range(self.rows_get):
            text_var_b.append([])
            entries_b.append([])
            for j in range(self.cols_get):
                if i == 1:
                    Label(self.frame_add_input, text=alphabet[j]).grid(row=self.rows_get * 2, column=j + 2)
                text_var_b[i].append(StringVar())
                entries_b[i].append(Entry(self.frame_add_input, textvariable=text_var_b[i][j], width=3))
                entries_b[i][j].grid(row=i + self.rows_get + 5, column=j + 2)
                Label(self.frame_add_input, text=i + 1).grid(row=i + self.rows_get + 5, column=1, sticky='e')

        def get_mat_a():
            self.matrix_a = []
            for i2 in range(self.rows_get):
                self.matrix_a.append([])
                for j2 in range(self.cols_get):
                    self.matrix_a[i2].append(text_var[i2][j2].get())

        def get_mat_b():
            self.matrix_b = []
            for i3 in range(self.rows_get):
                self.matrix_b.append([])
                for j3 in range(self.cols_get):
                    self.matrix_b[i3].append(text_var_b[i3][j3].get())

        def get_mat():
            try:
                get_mat_a()
                get_mat_b()
                self.output_matrix()
            except (ValueError, Exception):
                pass

        Button(self.frame_add_input, text="Enter", width=8, command=get_mat).grid(row=self.cols_get + self.cols_get + 10, column=1)

        self.add_input.protocol("WM_DELETE_WINDOW", menu.window.destroy)
        self.add_input.mainloop()

    def __init__(self):
        self.add_input = None
        self.frame_add_input = None
        self.rows_get, self.cols_get = None, None
        self.matrix_a, self.matrix_b = None, None
        self.add_output = None
        self.frame_add_output = None
        self.sum_matrix = None

        menu.window.withdraw()
        self.add_menu = Toplevel()
        self.add_menu.title("Add")
        self.add_menu.resizable(False, False)

        self.frame_add_menu = Frame(self.add_menu, highlightbackground='black', highlightthickness=1)
        self.frame_add_menu.pack(fill=BOTH, expand=True, padx=5, pady=5)

        Label(self.frame_add_menu, text='Matrix dimensions:', font=('arial', 10, 'bold')).grid(row=3, column=1, columnspan=1)


        self.rows = IntVar()
        self.rows.set(2)

        OptionMenu(self.frame_add_menu, self.rows, *range(2, 5)).grid(row=3, column=2)

        Label(self.frame_add_menu, text='x').grid(row=3, column=3)
        
        self.cols = IntVar()
        self.cols.set(2)

        OptionMenu(self.frame_add_menu, self.cols, *range(2, 5)).grid(row=3, column=4)

        Button(self.frame_add_menu, text='Enter', padx=16, pady=5, command=self.input_matrix).grid(row=5, column=4)

        self.add_menu.protocol("WM_DELETE_WINDOW", menu.window.destroy)
        self.add_menu.mainloop()
