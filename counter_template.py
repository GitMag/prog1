"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 0123456
Name:       Xxxx Yyyyyy
Email:      xxxx.yyyyyy@tuni.fi

Code template for counter program.
"""

from tkinter import *


class Counter:

    def reset_counter(self):
        # reset the counter and update counter label value
        self.__current_value = 0

        self.update_counter_label()

    def update_counter_label(self):
        self.__current_value_label.configure(text=self.__current_value)

    def increase_value(self):
        self.__current_value += 1

        self.update_counter_label()

    def decrease_value(self):
        self.__current_value -= 1

        self.update_counter_label()

    def quit_program(self):
        self.__main_window.destroy()

    def __init__(self):
        # TODO: You have to creater one label and four buttons and store
        #       them in the following attributes:
        #
        #       self.__current_value_label  # Label displaying the current value of the counter.
        #       self.__reset_button         # Button which resets counter to zero.
        #       self.__increase_button      # Button which increases the value of the counter by one.
        #       self.__decrease_button      # Button which decreases the value of the counter by one.
        #       self.__quit_button          # Button which quits the program.
        #
        #       Make sure you name the components exactly as shown above,
        #       otherwise the automated tests will fail.

        # create the variable to store the current value
        self.__current_value = 0

        # create the main window
        self.__main_window = Tk()

        # counter label stuff
        self.__current_value_label = Label(self.__main_window,
                                           text="0")
        self.__current_value_label.pack()

        # reset button
        self.__reset_button = Button(self.__main_window, text="Reset",
                                     command=self.reset_counter)
        self.__reset_button.pack(side=LEFT)

        # increase button
        self.__increase_button = Button(self.__main_window, text="Increase",
                                        command=self.increase_value)
        self.__increase_button.pack(side=LEFT)

        # decrease button
        self.__decrease_button = Button(self.__main_window, text="Decrease",
                                        command=self.decrease_value)
        self.__decrease_button.pack(side=LEFT)

        # quit button
        self.__quit_button = Button(self.__main_window, text="Quit",
                                    command=self.quit_program)
        self.__quit_button.pack(side=LEFT)

        # open window
        self.__main_window.mainloop()

def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()
