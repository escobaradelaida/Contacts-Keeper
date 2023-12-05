from breezypythongui import EasyFrame
from tkinter.font import Font

class ContactsDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, width=500, height=400, title="Contacts")

        self.contacts = {}

        self.label = self.addLabel(text="First Name",
                                  row=0, column=0,
                                  columnspan=2,
                                  sticky="NSEW")
        #input field
        self.nameField = self.addTextField(text="", row=0, rowspan=1, column=4, columnspan=1, sticky="NSEW")
        font = Font(family="Grotesque", size=15, weight="bold")
        self.label["font"] = font
        self.label["foreground"] = "blue"
        self.label = self.addLabel(text="Last Name",
                                   row=1, column=0,
                                   columnspan=2,
                                   sticky="NSEW")
        self.lastnameField = self.addTextField(text="", row=1, rowspan=1, column=4, columnspan=1, sticky="NSEW")
        font = Font(family="Grotesque", size=15, weight="bold")
        self.label["font"] = font
        self.label["foreground"] = "blue"
        self.label = self.addLabel(text="Phone number",
                                   row=2, column=0,
                                   columnspan=2, sticky="NSEW")
        self.phoneField = self.addTextField(text="", row=2, rowspan=1, column=4, columnspan=1, sticky="NSEW")
        font = Font(family="Grotesque", size=15, weight="bold")
        self.label["font"] = font
        self.label["foreground"] = "blue"
        self.label = self.addLabel(text="Email",
                                   row=3, column=0,
                                   columnspan=2, sticky="NSEW")
        self.emailField = self.addTextField(text="", row=3, rowspan=1, column=4, columnspan=1, sticky="NSEW")
        font = Font(family="Grotesque", size=15, weight="bold")
        self.label["font"] = font
        self.label["foreground"] = "blue"

        self.addButton(text="Add Contact", row=5, column=5,columnspan=2,
                                         command=self.addContact)
        self.addButton(text="Retrieve Contacts", row=6, column=5,columnspan=2, command=self.retrieveContact)

    def addContact(self):
        firstname = self.nameField.getText()
        lastname = self.lastnameField.getText()
        phone = self.phoneField.getText()
        email = self.emailField.getText()

        if firstname and lastname and phone and email:
            contact_info = [firstname, lastname, phone, email]
            with open("contacts.txt", 'a') as file:
                file.write(f"{contact_info[0]} {contact_info[1]}: {contact_info[2]} - {contact_info[3]}\n")
            self.messageBox(title="Success", message="Contact has been added successfully!")


            self.nameField.setValue("")
            self.lastnameField.setValue("")
            self.phoneField.setValue("")
            self.emailField.setValue("")

        else:
            self.messageBox(title="Error!", message="The fields cannot be empty!")

    def retrieveContact(self):
        try:
            with open("contacts.txt", 'r') as file:
                contacts = file.read()
                self.messageBox(title="Contacts", message=contacts, width=50, height=25)
        except FileNotFoundError:
            self.messageBox(title="Error!", message="No contacts have been found.")

def main():
    ContactsDemo().mainloop()

main()
# I want it to write the name into a file with the contact information
