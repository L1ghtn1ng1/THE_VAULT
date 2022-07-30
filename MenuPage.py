from tkinter import ttk


class page():
    def create(self):
        # Label Menu title.
        self.Title = ttk.Label(
            self,
            text="Menu",
            font=("Video Cond", 25))
        self.Title.grid(column=1, row=1) # Place on grid into window.

        # Label to welcome user.
        self.welcomeLabel = ttk.Label(self, text="Welcome!", font=("Video Cond", 20))
        self.welcomeLabel.grid(column=1, row=2) # Place on grid into window.

        # Label for instructions.
        self.instructionsLabel = ttk.Label(
            self,
            text="Please select one of the options.",
            font=("Video Cond", 20))
        self.instructionsLabel.grid(column=1, row=3) # Place on grid into window.

        # Button to switch to manage passwords page.
        self.manageLabel = ttk.Button(
            self,
            text="Manage Passwords", command=lambda: self.changePage(0)) # Switch to manage password page.
        self.manageLabel.grid(column=1, row=4)  # Place on grid into window.

        # Button to switch to password generator.
        self.passGenerator = ttk.Button(
            self,
            text="Password Generator", command=lambda: self.changePage(0))  # Switch to the password generator page.
        self.passGenerator.grid(column=1, row=5)  # Place on grid into window.

        # Button to switch pages.
        self.logoff = ttk.Button(
            self,
            text="Log Out", command=lambda: self.changePage(0))  # Switches to the login page.
        self.logoff.grid(column=1, row=6)  # Place on grid into window.
