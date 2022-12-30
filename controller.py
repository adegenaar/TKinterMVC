"""
Controller for the Tkinter app
"""
from lib.event import subscribe
from model import Model
from view import View


class Controller:
    """
    Controller
    """

    def __init__(self, model: Model, view: View) -> None:
        """
        __init__ Initializer

        Args:
            model (Model): Model for use with the controllers
            view (View): View for use with the controller
        """
        self.model: Model = model
        self.view: View = view

    def save(self, email: str) -> None:
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

    def setup_event_handlers(self) -> None:
        """
        setup_event_handlers Register the event handlers
        """
        subscribe("save_button_clicked", self.save)
