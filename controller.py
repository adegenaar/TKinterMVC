"""
Controller for the Tkinter app
"""
from model import Model
from view import View
from lib.event import subscribe


class Controller:
    """
    Controller
    """

    def __init__(self, model: Model, view: View):
        """
        __init__ Initializer

        Args:
            model (Model): Model for use with the controllers
            view (View): View for use with the controller
        """
        self.model = model
        self.view = view

    def save(self, email: str):
        """
        save Save the email

        Args:
            email (str): email address to save
        """
        try:

            # save the model
            self.model.email = email
            self.model.save()

            # show a success message
            self.view.show_success(f"The email {email} saved!")

        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def setup_event_handlers(self):
        """
        setup_event_handlers Register the event handlers
        """
        subscribe("save_button_clicked", self.save)
