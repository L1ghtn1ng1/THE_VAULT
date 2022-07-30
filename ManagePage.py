import tkinter as tk
from tkinter import ttk

class page():
    def create(self):
        self.pswdBtnList = []  # Create empty list for all password names
        self.passwords = []  # Create empty list for all passwords.
        try:
            filething = open("PasswordsList.txt", "r")  # Open and read file.
            for line in filething:
                lineList = line.split(":")  # Split the page into two columns with ':'.
                self.pswdBtnList.append(lineList[0])  # Appends the first column (the names) to the empty list
                # dedicated for it.
                self.passwords.append(lineList[1])  # Appends the second column (the passwords) to the empty list
                # dedicated for it.
            filething.close()  # Close the file.
        except:
            print("No passwords found yet")  # If no passwords are saved, there will be nothing in the file,
            # hence, print this.

        # Label the title.
        self.Title = ttk.Label(self,
                               text="Manage Passwords",
                               font=("Video Cond", 25))
        self.Title.grid(column=1, row=0)  # Place on grid into window.

        # The for loop makes as many buttons as there are passwords. All have the same command, to display the
        # password corresponding to the password name. This produces an updated list of passwords to view everytime a
        # password is added.
        for element in self.pswdBtnList:
            self.details = ttk.Button(self,
                                      text=element,
                                      command=lambda tempz=element: self.showsavedPassword(tempz))
            self.details.grid(column=1, row=self.pswdBtnList.index(element) + 1)  # Place on grid into window.

        self.details = ttk.Button(self,
                                  text="Add Password",
                                  command=lambda: self.changePage(3))  # Switches to add password page.
        self.details.grid(column=1, row=998)  # Places it at second to last in the window.

        self.goBack = ttk.Button(
            self,
            text="Cancel", command=lambda: self.changePage(2))  # Switches to Manage Page.
        self.goBack.grid(column=1, row=999)  # Places it at the very last in the window.
