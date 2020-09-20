#Instantiate contact
class Contacts:
    """create contact info"""
    def __init__(self, firstname, lastname, email, phone, groups):
        self.firstname = firstname.capitalize()
        self.lastname = lastname.capitalize()
        self.fullname = self.firstname + " " + self.lastname
        self.email = email
        self.phone = phone
        self.groups = groups
        self.last_contact = None

    def format_data(self):
        return {"name": self.fullname, "email": self.email, "phone": self.phone, "groups": self.groups, "last_contact": self.last_contact}
