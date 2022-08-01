from tkinter import ttk
import random
import string
import clipboard


class page():
    def create(self):
        self.letter_digit_list = list(string.digits + string.ascii_letters)
        # shuffle random source of letters and digits
        random.shuffle(self.letter_digit_list)

        # first generate 7 random digits
        self.sample_str = ''.join(
            (random.choice(string.digits) for i in range(7)))

        # Now create random string of length 8 which is a combination of
        # letters and digits
        # Next, concatenate it with sample_str
        self.sample_str += ''.join((random.choice(self.letter_digit_list)
                                   for i in range(8)))
        self.aList = list(self.sample_str)
        random.shuffle(self.aList)

        self.final_str = ''.join(self.aList)

        # Output example ~ 81OYQ6D430'''

        # Label to display password
        self.Title = ttk.Label(self,
                               text="Here is your password!",
                               font=("Video Cond", 25))
        self.Title.grid(column=1, row=1)  # Place on grid into window.

        self.generatedPass = ttk.Label(self,
                                       # Label to display the password.
                                       text=self.final_str,
                                       font=("Video Cond", 25))
        self.generatedPass.grid(column=1, row=2)

        self.copyButton = ttk.Button(
            self, text="Copy Password", command=lambda: clipboard.copy(
                self.final_str))  # Allow user to copy password.
        self.copyButton.grid(column=1, row=3)

        # Button purpose to go back to Menu page.
        self.goBack = ttk.Button(
            self,
            text="Return",
            command=lambda: self.changePage(1))
        self.goBack.grid(column=1, row=4)
