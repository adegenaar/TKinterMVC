"""
TKinter View
"""
import tkinter as tk
from tkinter import ttk
from lib.event import post_event


class View(ttk.Frame):  # pylint: disable=too-many-ancestors
    """
    View View for the Application

    Args:
        ttk (Frame): Frame for the view
    """

    def __init__(self, parent):
        """
        __init__ Initializer

        Args:
            parent ([type]): parent of the view
        """
        super().__init__(parent)

        # create widgets
        # label
        self.label = ttk.Label(self, text="Email:")
        self.label.grid(row=1, column=0)

        # email entry
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(self, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=1, column=1, sticky=tk.NSEW)

        # save button
        self.save_button = ttk.Button(self, text="Save", command=self.save_button_clicked)
        self.save_button.grid(row=1, column=3, padx=10)

        # message
        self.message_label = ttk.Label(self, text="", foreground="red")
        self.message_label.grid(row=2, column=1, sticky=tk.W)

        # layout the view in a grid
        self.grid(row=0, column=0, padx=10, pady=10)

    def save_button_clicked(self):
        """
        Handle button click event
        """
        post_event("save_button_clicked", self.email_var.get())

    def show_error(self, message: ValueError):
        """
        Show an error message
        """
        self.message_label["text"] = message
        self.message_label["foreground"] = "red"
        self.message_label.after(3000, self.hide_message)
        self.email_entry["foreground"] = "red"

    def show_success(self, message: str):
        """
        Show a success message
        """
        self.message_label["text"] = message
        self.message_label["foreground"] = "green"
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.email_entry["foreground"] = "black"
        self.email_var.set("")

    def hide_message(self):
        """
        Hide the message
        """
        self.message_label["text"] = ""
