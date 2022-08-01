import tkinter as tk
from tkinter import ttk


class page():
    def create(self):
        self.pswdBtnList = []  # Create empty list for all password names
        self.passwords = []  # Create empty list for all passwords.
        try:
            filething = open("PasswordsList.txt", "r")  # Open and read file.
            for line in filething:
                # Split the page into two columns with ':'.
                lineList = line.split(":")
                # Appends the first column (the names) to the empty list
                self.pswdBtnList.append(lineList[0])
                # dedicated for it.
                # Appends the second column (the passwords) to the empty list
                self.passwords.append(lineList[1])
                # dedicated for it.
            filething.close()  # Close the file.
        except BaseException:
            # If no passwords are saved, there will be nothing in the file,
            print("No passwords found yet")
            # hence, print this.

        # Label the title.
        self.Title = ttk.Label(self,
                               text="Manage Passwords",
                               font=("Video Cond", 25))
        self.Title.grid(column=1, row=0)  # Place on grid into window.

        # The for loop makes as many buttons as there are passwords.
        # All have the same command, to display the
        # password corresponding to the password name.
        # This produces an updated list of passwords to view everytime a
        # password is added.
        for element in self.pswdBtnList:
            self.details = ttk.Button(
                self,
                text=element,
                command=lambda tempz=element: self.showsavedPassword(tempz))
            # Place on grid into window.
            self.details.grid(
                column=1, row=self.pswdBtnList.index(element) + 1)

        # Switches to add password page.
        self.details = ttk.Button(
            self,
            text="Add Password",
            command=lambda: self.changePage(3))
        # Places it at second to last in the window.
        self.details.grid(column=1, row=998)

        # Switches to Manage Page.
        self.goBack = ttk.Button(
            self,
            text="Cancel",
            command=lambda: self.changePage(1))
        # Places it at the very last in the window.
        self.goBack.grid(column=1, row=999)
