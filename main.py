# Base libraries
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import * # Library for error messages

#Import Pages
import LoginPage
class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)  # initialize the superclass(frame)

        # Page list
        # ADD NEW CLASSES YOU MAKE TO LIST!  (pages will be indexed chronologically)
        self.availablePages = [
            LoginPage.page

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
            if len(self.pin) == 4:
                if self.pin == self.mainPin:
                    print("works")
                else:
                    showerror(title="Invalid Entry", message="Password is not correct.")
                print(int(self.pin))
            else:
                raise Exception
        except:
            showerror(title="Invalid Entry", message="Please enter 4 digits.")



if __name__ == "__main__":  # If this file is run directly, run the following code
    root = tk.Tk()  # Create a window
    root.title("The Vault")  # Add title
    app = App(root)  # Link the App and window we made
    app.pack(fill="both", expand=True)  # Allow resizing
    root.mainloop()  # Run the app
