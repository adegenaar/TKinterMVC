"""
Application file
"""

import tkinter as tk

from controller import Controller
from model import Model
from view import View


class App(tk.Tk):
    """
    App Email application

    Args:
        tk (Tk): TKinter
    """

    def __init__(self) -> None:
        """
        __init__ Initializer
        """
        super().__init__()

        self.title("Tkinter MVC Demo")

        # create a model
        model: Model = Model("hello@pythontutorial.net")

        # create a view and place it on the root window
        view: View = View(self)

        # create a controller
        controller: Controller = Controller(model, view)
        controller.setup_event_handlers()


if __name__ == "__main__":
    app: App = App()
    app.mainloop()
