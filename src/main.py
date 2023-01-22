import pendulum
import settings
import timer
import tkinter as tk


class App:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title('rezepinn/bmstu/pendulum.app')
        self.root.resizable(False, False)

        self.pendulum = pendulum.Pendulum(self.root)
        self.timer = timer.Timer(self.root, self.pendulum)
        self.settings = settings.Settings(self.root, self.pendulum)

        self.root.mainloop()


App()
