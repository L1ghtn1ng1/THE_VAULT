from tkinter import ttk

class page:
    def create(self):

        # All these make labels/entry boxes/buttons and places them in the window using grid. ALl have the same font
        # (Video Cond) and different font sizes. Places them on the grid and into the window.
        self.Title = ttk.Label(self,
                               text="Adding Password",
                               font=("Video Cond", 25))
        self.Title.grid(column=1, row=1)

        self.details = ttk.Label(self,
                                 text ="Details",
                                 font=("Video Cond", 23))
        self.details.grid(column=1, row=2)

        self.passwordName = ttk.Label(self,
                                      text = "Password Name:",
                                      font=("Video Cond", 18))
        self.passwordName.grid(column=1, row=3)

        self.passwordnameEntry = ttk.Entry(self)
        self.passwordnameEntry.grid(column=1, row=4)

        self.password = ttk.Label(self,
                                  text = "Password:",
                                  font=("Video Cond", 18))
        self.password.grid(column=1, row=5)

        self.passwordEntry = ttk.Entry(self)
        self.passwordEntry.grid(column=1, row=6)

        self.savePassword = ttk.Button(self,
                                       text="Save Password",
                                       command = self.SavePass) # Uses the function made to save the password and add
                                                                # it to the list.
        self.savePassword.grid(column=1, row=7)

        self.goBack = ttk.Button(
            self,
            text="Cancel", command=lambda: self.changePage(2)) # Button's purpose is to switch to manage passwords page.
        self.goBack.grid(column=1, row=8)

