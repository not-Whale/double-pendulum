import tkinter as tk


class App:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title('rezepinn/bmstu/pendulum.app')
        self.root.resizable(False, False)

        self.root.mainloop()


App()
