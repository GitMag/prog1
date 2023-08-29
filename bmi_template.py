"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Body Mass Index template
"""

from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()

        # TODO: Create an Entry-component for the weight.
        self.__weight_value = Entry()

        # TODO: Create an Entry-component for the height.
        self.__height_value = Entry()

        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        #       the default colour.
        self.__calculate_button = Button(text="Calculate", command=self.calculate_BMI)

        # TODO: Create a Label that will show the decimal value of the BMI
        #      after it has been calculated.
        self.__result_text = Label(text="")

        # TODO: Create a Label that will show a verbal description of the BMI
        #       after the BMI has been calculated.
        self.__explanation_text = Label(text="")

        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(text="Stop", command=self.stop)

        # Label for height:
        self.__height_label = Label(text="Height:")

        # Label for weight:
        self.__weight_label = Label(text="Weight:")

        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        self.__weight_label.grid(row=0, column=0, sticky="W", padx=1)
        self.__weight_value.grid(row=1, column=0, sticky="W")
        self.__height_label.grid(row=2, column=0, sticky="W", padx=1)
        self.__height_value.grid(row=3, column=0, sticky="W")
        self.__calculate_button.grid(row=6, column=0, sticky="W", padx=2)
        self.__stop_button.grid(row=6, column=1, padx=2, sticky="W")
        self.__result_text.grid(row=4, column=0, sticky="W", padx=1)
        self.__explanation_text.grid(row=5, column=0, sticky="W", padx=1)

    # TODO: Implement this method.
    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """

        # get values from ui Entry boxes
        # weight in kg
        try:
            weight = float(self.__weight_value.get())
            # height in meters
            height = float(self.__height_value.get()) / 100
        except ValueError:
            self.__explanation_text.config(text="Error: height and weight must be numbers.")
            self.reset_fields()
            return

        # check if values are positive
        if weight < 0 or height < 0:
            # negative, display error
            self.__explanation_text.config(text="Error: height and weight must be positive.")
            self.reset_fields()
            return

        # checks complete, calculate BMI
        # try to calculate BMI
        raw_bmi = weight/(height**2)
        bmi = f"{raw_bmi:.2f}"

        # verbal info about bmi
        # check if underweight
        if raw_bmi < 18.5:
            self.__explanation_text.config(text="You are underweight.")
        # check if overweight
        elif raw_bmi > 25:
            self.__explanation_text.config(text="You are overweight.")
        # if not under or overweight, must be normal weight
        else:
            self.__explanation_text.config(text="Your weight is normal.")

        # set result label value to bmi
        self.__result_text.configure(text=bmi)



    # TODO: Implement this method.
    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """
        self.__result_text.config(text="")
        self.__height_value.delete(0, END)
        self.__weight_value.delete(0, END)

    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
