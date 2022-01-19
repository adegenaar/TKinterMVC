"""
Model
"""
import re
import io


class Model:
    """
    Model for the MVC
    """

    def __init__(self, email: str) -> None:
        """
        __init__ Initializer

        Args:
            email (str): Email address
        """
        self.email = email

    @property
    def email(self) -> str:
        """
        email Retrieve the email address

        Returns:
            str: the email address
        """
        return self.__email

    @email.setter
    def email(self, value: str) -> None:
        """
        Validate the email
        """
        pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f"Invalid email address: {value}")

    def save(self) -> None:
        """
        Save the email into a file
        """
        with io.open("emails.txt", mode="a", encoding="utf-8") as the_file:
            the_file.write(self.email + "\n")
