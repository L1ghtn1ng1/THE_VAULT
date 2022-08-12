from tkinter import ttk
import clipboard


class page():
    def create(self):

        # All these make labels/entry boxes/buttons and places them in the
        # window using grid. ALl have the same font
        # (Video Cond) and different font sizes. Places them on the grid
        # and into the window.
        self.Title = ttk.Label(self,
                               text="Here are your details.",
                               font=("Video Cond", 25))
        self.Title.grid(column=1, row=1, pady=(0, 10), padx=5)

        self.passwordName = ttk.Label(self,
                                      # Prints out the name of the password
                                      text="Password Name:" + "\n" +
                                      self.theName,
                                      font=("Video Cond", 18),
                                      justify='center')
        self.passwordName.grid(column=1, row=2, pady=(0, 5))

        self.passwordName = ttk.Label(self,
                                      text="Password:" + "\n" +
                                      self.thePassword,
                                      # Prints out the password
                                      font=("Video Cond", 18),
                                      justify='center')
        self.passwordName.grid(column=1, row=3, pady=(0, 5))

        self.copyButton = ttk.Button(
            self,
            text="Copy Password",
            width=15,
            command=lambda: clipboard.copy(
                self.thePassword))
        self.copyButton.grid(column=1, row=4, pady=2)

        self.deleteButton = ttk.Button(
            self,
            width=15,
            text="Delete",
            command=lambda tempx=self.theName: self.deletePassword(tempx))
        self.deleteButton.grid(column=1, row=5, pady=2)

        # Switches to manage passwords page.
        self.goBack = ttk.Button(
            self,
            width=15,
            text="Return",
            command=lambda: self.changePage(2))
        self.goBack.grid(column=1, row=6, pady=2)
