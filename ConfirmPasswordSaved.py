from tkinter import ttk

class page():
    def create(self):
        # This page is to display to the user that their password has been saved.
        # Label to say password is saved. Places them on the grid and into the window.
        self.Title = ttk.Label(self,
                               text="Password Saved!",
                               font=("Video Cond", 25))
        self.Title.grid(column=1, row=1)

        self.goBack = ttk.Button(
            self,
            text="Return", command=lambda: self.changePage(2)) # Button purpose is to go to menu page.
        self.goBack.grid(column=1, row=2) # Place on grid into window.