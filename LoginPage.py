# Import Base Libraries
from tkinter import ttk


class page:  # Home page class
    def create(self):  # Function will create widgets when invoked

        # All these make labels/entry boxes/buttons and places them in the window using grid. ALl have the same font
        # (Video Cond) and different font sizes.
        self.mainTitle = ttk.Label(
            self,
            text="Password Manager",
            font=("Video Cond", 25))
        self.mainTitle.grid(column=1, row=1)  # Places on the grid and into the window.

        self.entryKey = ttk.Label(
            self, text="Enter your 4 digit key!",
            font=("Video Cond", 20))
        self.entryKey.grid(column=1, row=2)  # Places on the grid and into the window.

        self.pinEntry = ttk.Entry(self)
        self.pinEntry.grid(column=1, row=3)  # Places on the grid and into the window.

        self.loginButton = ttk.Button(
            self,
            text="LOGIN",
            command=self.getPin)
        self.loginButton.grid(column=1, row=4)  # Places on the grid and into the window.
