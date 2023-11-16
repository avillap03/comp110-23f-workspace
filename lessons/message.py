"""Class to store a message (operator overload, union types, default parameters)."""

class Email:

    to: str | int
    message: str
    important: bool


    def _init_(self, recipient: str, message_text: str = "", importance_flag: bool = False) -> None:
        """Constructor of an email."""
        self.to = recipient
        self.message = message_text
        self.important = importance_flag


    def _str_(self) -> str:
        m_string: str = f"To: {self.to} \n"
        m_string += f"Important? {self.important} \n"
        m_string += f'"{self.message}"'
        return m_string
    

    def __mul__(self, factor: int):
        self.message = self.message * factor 

email_to_chiara: Email = Email("chiara", "You're a great TA!", False)
email_to_chiara * 100
print(email_to_chiara)
email_to_lauren: Email = Email(123, "Great job!")
print (email_to_lauren)
