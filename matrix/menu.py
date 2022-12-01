from tkinter import*
from tkinter.constants import BOTH
import multi
import trans
import add

window = Tk()
window.geometry('200x200')
window.title('Menu')
window.resizable(False, False)
frame_window = Frame(window, highlightbackground='black', highlightthickness=1, bg='pink')
frame_window.pack(fill=BOTH, expand=True, padx=5, pady=5)


class Menu:
    def __init__(self):
        label = Label(frame_window, text="Choose Operation:", pady=10, font=('arial', 10, 'bold'))

        ad = Button(frame_window, text="Add", padx=40, pady=5, command=add.Add)
        tran = Button(frame_window, text="Transpose", padx=28, pady=5, command=trans.Trans)
        mlt = Button(frame_window, text="Multiply", padx=22, pady=5, command=multi.Multi)

        label.pack()
        mlt.pack()
        ad.pack()
        tran.pack()

        window.mainloop()
