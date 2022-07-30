# Base libraries
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import * # Library for error messages
from cryptography.fernet import Fernet  # Library for encryption
import os

#Import Pages
import LoginPage
import MenuPage
import ManagePage
import AddingPasswordPage
class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)  # initialize the superclass(frame)

        # Page list
        # ADD NEW CLASSES YOU MAKE TO LIST!  (pages will be indexed chronologically)
        self.availablePages = [
            LoginPage.page,
            MenuPage.page,
            ManagePage.page,
            AddingPasswordPage.page

        ]
        #
        #
        # Split into 3 columns
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        self.columnconfigure(index=2, weight=1)

        # Show first page on list at start up
        self.availablePages[0].create(self)

    # Function to change between pages
    def changePage(self, number):
        for widget in self.winfo_children():  # For each widget on screen
            widget.destroy()  # Destroy each widget found
            #
            #
            # Run the create function on the desired page
            self.availablePages[number].create(self)

    # Function to check if pin is correct.
    def getPin(self):
        self.file = open("topsecret.txt", 'r+')
        self.mainPin = self.file.read()
        try:
            self.pin = self.pinEntry.get()
            if ' ' in self.pin:
                showerror(title ="Invalid Entry", message="Re-enter 4 digit pin without spaces.")
            elif len(self.pin) == 4:
                if self.pin == self.mainPin:
                    self.changePage(1) # Change pages if pin is correct.
                else:
                    showerror(title="Invalid Entry", message="Password is not correct.")
            else:
                raise Exception
        except:
            showerror(title="Invalid Entry", message="Please enter 4 digits.")

    # Function to save a new password.
    def SavePassword(self):
        try:
            if "" == self.passwordEntry.get() or " " in self.passwordEntry.get():
                raise ValueError("Enter a password/ no spaces allowed.")
            with open("PasswordsList.txt", "r") as f:  # Opens file and reads it.
                for line in f:  # Goes through each line in the file.

                    if self.passwordnameEntry.get() in line:  # Finds if password is already saved in file.
                        raise ValueError("Password already exists.")

            self.encryptedPassword = self.encrypt(self.passwordEntry.get()).decode('utf-8')

            passwordsfile = open("PasswordsList.txt", "a")
            passwordsfile.write(
                self.passwordnameEntry.get() + ":" + self.encryptedPassword + "\n")  # Encrypts password to file
            passwordsfile.close()
            self.changePage(1)
        except ValueError as e:
            showerror(title="Error", message=e.args[0])

#   Function to display password when the name of password from the list is clicked.
    def showsavedPassword(self, wanted):
        pswds = open("PasswordsList.txt", "r") # Opens and reads file with all password details.
        for line in pswds:
            self.lineSplit = line.split(":") # Splits the name and the password with the ':'.
            if wanted == self.lineSplit[0]: # Checks for our wanted name and its corresponding password.
                self.thePassword = self.lineSplit[1]
                self.theName = self.lineSplit[0]
        pswds.close()
        self.changePage(2) #Change page to display the password details.

    # Function to encrypt passwords saved.
    def encrypt(self, rawPassword):
        # Open the key file
        self.f = Fernet(open("key.key", "rb").read())
        # rawPassword is encoded to bytes
        # Encrypt `rawPassword` using the key and store to `encryptedP`
        self.encryptedP = self.f.encrypt(bytes(rawPassword, 'utf-8'))

        # Return the encrypted password
        return self.encryptedP


#   Function to decrypt encrypted passwords.
    def decrypt(self,encryptedPassword):
        # Open the key file
        self.f = Fernet(open("key.key", "rb").read())

        # encryptedPassword is encoded to bytes
        # Decrypt `encryptedPassword` using the key and store to `decryptedP`
        self.decryptedP = self.f.decrypt(bytes(encryptedPassword, 'utf-8'))

        # Decode decryptedP to normal password and then return it
        return self.decryptedP.decode('utf-8')


if __name__ == "__main__":  # If this file is run directly, run the following code

    if not os.path.exists("./key.key"):  # Checks if key already exists
        key = Fernet.generate_key()  # Generates key if there isn't one.
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        print("Key generated successfully")
    else:
        print("Key already exists")


    root = tk.Tk()  # Create a window
    root.title("The Vault")  # Add title
    app = App(root)  # Link the App and window we made
    app.pack(fill="both", expand=True)  # Allow resizing
    root.mainloop()  # Run the app
