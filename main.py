# Base libraries
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *  # Library for error messages
from cryptography.fernet import Fernet  # Library for encryption
import os
import sv_ttk

# Import Pages
import LoginPage
import MenuPage
import ManagePage
import AddingPasswordPage
import ConfirmPasswordSaved
import PasswordGeneratorPage
import DisplayGeneratedPassword
import ShowSavedPassword


class App(ttk.Frame):
    def __init__(self, parent):
        self.svtk = sv_ttk  # Making theme a class variable.
        sv_ttk.use_dark_theme()  # Default theme.
        ttk.Frame.__init__(self)  # initialize the superclass(frame)

        # Page list
        # ADD NEW CLASSES YOU MAKE TO LIST!  (pages will be indexed
        # chronologically)
        self.availablePages = [
            LoginPage.page,
            MenuPage.page,
            ManagePage.page,
            AddingPasswordPage.page,
            ConfirmPasswordSaved.page,
            PasswordGeneratorPage.page,
            DisplayGeneratedPassword.page,
            ShowSavedPassword.page

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
                showerror(title="Invalid Entry",
                          message="Re-enter 4 digit pin without spaces.")
            elif len(self.pin) == 4:
                if self.pin == self.mainPin:
                    self.changePage(1)  # Change pages if pin is correct.
                else:
                    showerror(
                        title="Invalid Entry",
                        message="Password is not correct.")
            else:
                raise Exception
        except BaseException:
            showerror(title="Invalid Entry", message="Please enter 4 digits.")

    # Function to save a new password.
    def SavePassword(self):
        self.pswd_len = len(self.passwordEntry.get())
        try:
            self.pswdEntrytxt = self.passwordEntry.get()
            if "" == self.pswdEntrytxt or " " in self.pswdEntrytxt:
                raise ValueError("Enter a password/ no spaces allowed.")
            elif (self.pswd_len > 25 or self.pswd_len < 8):
                raise ValueError("Password must be between 8-25 characters!")
            elif len(self.passwordnameEntry.get()) > 15:
                raise ValueError("Maximum character limit is 15 for name!")
            elif len(self.pswdBtnList) == 15:
                raise ValueError("Limit reached, please delete a password!")
            # Opens file and reads it.
            with open("PasswordsList.txt", "r") as f:
                for line in f:  # Goes through each line in the file.

                    # Finds if password is already saved in file.
                    if self.passwordnameEntry.get() in line:
                        raise ValueError("Password already exists.")

            self.encryptedPassword = self.encryptPassword(
                self.passwordEntry.get()).decode('utf-8')

            passwordsfile = open("PasswordsList.txt", "a")
            passwordsfile.write(
                self.passwordnameEntry.get() +
                ":" +
                self.encryptedPassword +
                "\n")  # Encrypts password to file
            passwordsfile.close()
            self.changePage(4)
        except ValueError as e:
            showerror(title="Error", message=e.args[0])

    # Function to display password when the name of password from the list is
    # clicked.
    def showsavedPassword(self, wanted):
        # Opens and reads file with all password details.
        pswds = open("PasswordsList.txt", "r")
        for line in pswds:
            # Splits the name and the password with the ':'.
            self.lineSplit = line.split(":")
            # Checks for our wanted name and its corresponding password.
            if wanted == self.lineSplit[0]:
                self.thePassword = self.decryptPassword(self.lineSplit[1])
                self.theName = self.lineSplit[0]
        pswds.close()
        self.changePage(7)  # Change page to display the password details.

    # Function to encrypt passwords saved.
    def encryptPassword(self, rawPassword):
        # Open the key file
        self.f = Fernet(open("key.key", "rb").read())
        # rawPassword is encoded to bytes
        # Encrypt `rawPassword` using the key and store to `encryptedP`
        self.encryptedP = self.f.encrypt(bytes(rawPassword, 'utf-8'))

        # Return the encrypted password
        return self.encryptedP

    #   Function to decrypt encrypted passwords.
    def decryptPassword(self, encryptedPassword):
        # Open the key file
        self.f = Fernet(open("key.key", "rb").read())

        # encryptedPassword is encoded to bytes
        # Decrypt `encryptedPassword` using the key and store to `decryptedP`
        self.decryptedP = self.f.decrypt(bytes(encryptedPassword, 'utf-8'))

        # Decode decryptedP to normal password and then return it
        return self.decryptedP.decode('utf-8')

    # Function to delete passwords
    def deletePassword(self, temp):
        with open("PasswordsList.txt", 'r') as file:
            self.lines = file.readlines()

        with open("PasswordsList.txt", 'w') as file:
            for line in self.lines:
                # find() returns -1 if no match is found
                if line.find(temp) != -1:
                    pass
                else:
                    file.write(line)
        self.changePage(2)


# If this file is run directly, run the following code
if __name__ == "__main__":

    if not os.path.exists("./key.key"):  # Checks if key already exists
        key = Fernet.generate_key()  # Generates key if there isn't one.
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        print("Key generated successfully")
    else:
        print("Key already exists")

# This loop checks if the app is being run for the first time and allows
# the user to set up a pin, else it keeps
# as normal.
    breakOut = 0  # initalise variable for while loop.
    while breakOut == 0:
        if (not os.path.exists("topsecret.txt")):
            newPin = input("Enter a 4 digit pin! ")
            # Makes sure the pin that is being set meets the requirements.
            if len(newPin) == 4 and newPin.isdigit():
                confirmPin = input("Confirm Pin ")
                if (confirmPin == newPin):
                    file = open("topsecret.txt", 'a')
                    file.write(newPin)
                    file.close()
                    pswdFile = open("PasswordsList.txt", "w")
                    pswdFile.close()
                    print("Done")
                    breakOut = 1
                else:
                    print("Pin does not match, please try again.")
            # Makes sure there is no spaces between the numbers and makes sure
            # the user enters numbers.
            elif " " in newPin:
                print("Error: Please re-enter your pin without spaces!")
            else:
                print("Error: Please enter 4 digits.")
        else:
            breakOut = 1  # Stops the while loop from running.

    root = tk.Tk()  # Create a window
    root.title("The Vault")  # Add title
    app = App(root)  # Link the App and window we made
    app.pack(fill="both", expand=True)  # Allow resizing
    root.mainloop()  # Run the app
