from tkinter import ttk
import clipboard

class page():
    def create(self):

        # All these make labels/entry boxes/buttons and places them in the window using grid. ALl have the same font
        # (Video Cond) and different font sizes. Places them on the grid and into the window.
        self.Title = ttk.Label(self,
                               text="Here are your details.",
                               font=("Video Cond", 25))
        self.Title.grid(column=1, row=1)

        self.passwordName = ttk.Label(self,
                                      text="Password Name:" + "\n" + self.theName, # Prints out the name of the password
                                      font=("Video Cond", 18), justify='center')
        self.passwordName.grid(column=1, row=2)

        self.passwordName = ttk.Label(self,
                                      text="Password:" + "\n" + self.thePassword, # Prints out the password
                                      font=("Video Cond", 18), justify='center')
        self.passwordName.grid(column=1, row=3)

        self.copyButton = ttk.Button(self,
                                     text="Copy Password",
                                     command=lambda: clipboard.copy(self.thePassword))
        self.copyButton.grid(column=1, row=4)

        self.deleteButton = ttk.Button(self,
                                       text = "Delete",
                                       command=lambda tempx = self.theName :self.deletePassword(tempx))
        self.deleteButton.grid(column = 1, row= 5)

        self.goBack = ttk.Button(
            self,
            text="Return", command=lambda: self.changePage(2)) # Switches to manage passwords page.
        self.goBack.grid(column=1, row=6)
