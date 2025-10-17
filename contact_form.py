class ContactForm:
    def __init__(self, name, ID, email, phone_number) -> None:
        self.name = name
        self.ID = ID
        self.email = email
        self.phone_number = phone_number

    def __repr__(self) -> str:
        return f'<Contact: {self.name}, {self.ID}, {self.email}, {self.phone_number}>'
