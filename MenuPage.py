from tkinter import ttk


class page:
    def create(self):
        # Label Menu title.
        self.Title = ttk.Label(
            self,
            text="Menu",
            font=("Video Cond", 25))
        self.Title.grid(column=1, row=1, pady=(0, 10))
        # Place on grid into window.

        # Label to welcome user.
        self.welcomeLabel = ttk.Label(
            self, text="Welcome!", font=(
                "Video Cond", 20))
        self.welcomeLabel.grid(column=1, row=2, pady=(0, 10))
        # Place on grid into window.

        # Label for instructions.
        self.instructionsLabel = ttk.Label(
            self,
            text="Please select one of the options.",
            font=("Video Cond", 20))
        # Place on grid into window.
        self.instructionsLabel.grid(column=1, row=3, pady=(0, 9), padx=5)

        # Button to switch to manage passwords page.
        # Switch to manage password page.
        self.manageLabel = ttk.Button(
            self,
            text="Manage Passwords",
            command=lambda: self.changePage(2))
        self.manageLabel.grid(column=1, row=4, pady=(0, 5))
        # Place on grid into window.

        # Button to switch to password generator.
        # Switch to the password generator page.
        self.passGenerator = ttk.Button(
            self,
            text="Password Generator",
            command=lambda: self.changePage(5))
        self.passGenerator.grid(column=1, row=5, pady=(0, 5))
        # Place on grid into window.

        # Button to switch themes.
        self.theme = ttk.Button(self,
                                text="Switch to light/dark mode.",
                                command=lambda: self.svtk.toggle_theme())
        self.theme.grid(column=1, row=6, pady=(0, 5))

        # Button to switch pages.
        # Switches to the login page.
        self.logoff = ttk.Button(
            self,
            text="Log Out",
            command=lambda: self.changePage(0))
        self.logoff.grid(column=1, row=7, pady=(0, 5))
        # Place on grid into window.
