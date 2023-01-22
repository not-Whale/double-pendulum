import pendulum
import settings
import timer
import tkinter as tk


class App:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title('rezepinn/bmstu/pendulum.app')
        self.root.resizable(False, False)

        self.timer = timer.Timer(self.root)
        self.settings = settings.Settings(self.root)
        self.pendulum = pendulum.Pendulum(self.root)

        self.root.mainloop()


App()
