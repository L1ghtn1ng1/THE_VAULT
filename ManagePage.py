import tkinter as tk
from tkinter import ttk

class page():
    def create(self):

        self.Title = ttk.Label(self,
                               text = "Manage Passwords",
                               font = ("Video Cond", 25))
        self.Title.grid(column = 1, row = 1)

        self.details = ttk.Button(self,
                                  text = "Password 1")
        self.details.grid(column = 1, row = 2)

        self.details = ttk.Button(self,
                                  text="Password 2")
        self.details.grid(column=1, row=3)

        self.details = ttk.Button(self,
                                  text="Password 3")
        self.details.grid(column=1, row=4)

        self.details = ttk.Button(self,
                                  text="Password 4")
        self.details.grid(column=1, row=5)

        self.details = ttk.Button(self,
                                  text="Add Password",
                                  command=lambda: self.changePage(3))
        self.details.grid(column=1, row=6)

        self.goBack = ttk.Button(
            self,
            text="Cancel", command=lambda: self.changePage(1))
        self.goBack.grid(column=1, row=7)
