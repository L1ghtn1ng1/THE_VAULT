from tkinter import ttk


class page():
    def create(self):
        # Label for password generator.
        self.Title = ttk.Label(self,
                               text="Password Generator",
                               font=("Video Cond", 25))
        self.Title.grid(column=1, row=1, pady=(0, 10), padx=5)
        # Place on grid into window.

        # Button to generate password.
        self.details = ttk.Button(
            self,
            text="Generate Password!",
            command=lambda: self.changePage(6))  # Generates a random password
    # and switches pages
        # to display it.
        self.details.grid(column=1, row=2)  # Place on grid into window.

        # Button to go to Menu page.
        self.goBack = ttk.Button(
            self,
            text="Cancel", command=lambda: self.changePage(1))
        self.goBack.grid(column=1, row=3)  # Place on grid into window.
