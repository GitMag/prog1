"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Fractions code template
"""


class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    # we add default values for operator that can be used with the fraction
    # object

    def __str__(self):
        return self.return_string()

    def __lt__(self, other_fraction):
        """
        Default function that gets called when comparing fraction object
        to an other object. Returns true or false depending on if the other
        fraction is bigger or smaller.

        :param other_fraction: The fraction to compare size with
        :return: bool, result of the comparision
        """

        # we convert the fractions to decimal
        deci1 = self.__numerator / self.__denominator
        deci2 = other_fraction.__numerator / other_fraction.__denominator

        # compare if the value of self in decimal form is smaller than
        # other fraction
        if deci1 < deci2:
            return True
        return False

    def complement(self):
        """
        Creates a complement fraction of self. Returns the result as a new
        object.

        :return: object, complement fraction
        """
        inverted_nu = -1 * self.__numerator
        complement_frac = Fraction(inverted_nu, self.__denominator)

        return complement_frac

    def reciprocal(self):
        """
        Inverts fraction, e.g. 1/2 is 2/1. Returns the inverterd fraction
        as a new object

        :return: object, inverted fraction
        """
        temp_nu = self.__numerator

        # we switch numerator and denominator
        numerator = self.__denominator
        denominator = temp_nu

        reciprocal_frac = Fraction(numerator, denominator)

        return reciprocal_frac

    def multiply(self, mupltiplication_frac):
        """
        Multiplies self with another fraction. Returns the factor that is
        the product of the multiplication as a new object.

        :param mupltiplication_frac: the factor to multiply self with
        :return: object, fraction that is the result of the multiplication
        """
        num2 = mupltiplication_frac.__numerator
        den2 = mupltiplication_frac.__denominator

        num_prod = self.__numerator * num2
        den_prod = self.__denominator * den2
        multiplied_frac = Fraction(num_prod, den_prod)

        return multiplied_frac

    def divide(self, divided_frac):
        """
        Divides self with a fraction inputted by params, reaturns the new
        fraction that is the result of the division as a new object

        :param divided_frac: the fraction to divide self witih
        :return: object, fraction that is the result of the division
        """
        inverted = divided_frac.reciprocal()
        divided_frac = self.multiply(inverted)

        return divided_frac

    def deduct(self, frac_to_deduct):
        """
        Deducts 2 fractions together, uses the expand function to expand the
        both fractions to the same divisor

        :param frac_to_deduct: object, the fraction to deduct from self
        :return: object, the new fraction that is the sum of self and
        fraction_to_deduct
        """
        frac1, frac2, new_denominator = self.expand(frac_to_deduct)

        num_sum = frac1.__numerator - frac2.__numerator
        sum_frac = Fraction(num_sum, new_denominator)

        return sum_frac

    def expand(self, expand_frac):
        """
        Expands self and other factor object to allow addition and subtraction
        between the fractions

        :param expand_frac: the other fraction to be expanded
        :return: object, object, int. Returns the two fractions expanded to a
        common denominator and the int of the denominator
        """
        denom1 = expand_frac.__denominator
        denom2 = self.__denominator
        expand_denom = denom1 * denom2

        expand_frac1 = Fraction(denom1, denom1)
        expand_frac2 = Fraction(denom2, denom2)

        frac1_expanded = self.multiply(expand_frac1)
        frac2_expanded = expand_frac.multiply(expand_frac2)

        return frac1_expanded, frac2_expanded, expand_denom

    def add(self, frac_to_add):
        """
        Adds 2 fractions together, uses the expand function to expand the both
        fractions to the same divisor

        :param frac_to_add: object, the fraction to add to self
        :return: object, the new fraction that is the sum of self and
        fraction_to_add
        """
        frac1, frac2, new_denominator = self.expand(frac_to_add)

        num_sum = frac1.__numerator + frac2.__numerator
        sum_frac = Fraction(num_sum, new_denominator)

        return sum_frac

    def simplify(self):
        """
        Simplifies the fractions with the greatest common divisor. Uses the
        greatest common divisor function to perform the simplification.
        Sets new values for denominator and numerator.

        :return: None
        """
        greatest_divisor = self.greatest_common_divisor(self.__numerator,
                                                        self.__denominator)
        self.__denominator = self.__denominator // greatest_divisor
        self.__numerator = self.__numerator // greatest_divisor

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def greatest_common_divisor(self, a, b):
        """
        Euclidean algorithm. Returns the greatest common
        divisor (suurin yhteinen tekijä).  When both the numerator
        and the denominator is divided by their greatest common divisor,
        the result will be the most reduced version of the fraction in question.
        """

        while b != 0:
            a, b = b, a % b
        return a


def list_fractions(fractions_dict):
    """
    Lists all the fractions in fractions_dict sorted from smallest to biggest

    :param fractions_dict: dict, key=name and value=fraction are stored in the
    dictionary
    """
    for fraction in sorted(fractions_dict):
        name = fraction
        fraction = fractions_dict[name]

        print(f"{name} = {fraction}")


def add(fractions_dict):
    """
    Adds a fraction with key=name and value=fraction to the
    fractions_dcit

    :param fractions_dict: dict, key=name and value=fraction are stored in the
    dictionary
    """
    fraction = input("Enter a fraction in the form integer/integer: ")
    name = input("Enter a name: ")

    numerator, denominator = fraction.split("/")

    # we add fraction to dict with key <name> and value <fraction>
    fractions_dict[name] = Fraction(int(numerator), int(denominator))


def print_fraction(fractions_dict):
    """
    Prints a fraction from the fractions_dict with key=name that is asked from
    the user. If the key is not found from the list an error message will be
    displayed

    :param fractions_dict: dict, key=name and value=fraction are stored in the
    dictionary
    """
    key = input("Enter a name: ")

    if key in fractions_dict:
        print(f"{key} = {fractions_dict[key]}")
    else:
        print(f"Name {key} was not found")


def multiply_two_fractions(fractions_dict):
    """
    Multiplies two fractions together by asking user to speciy their names.
    If the name=key is not found from fractions_dict an error message will
    be displyed to the user.

    :param fractions_dict: dict, key=name and value=fraction are stored in the
    dictionary
    """
    frac1_name = input("1st operand: ")

    if frac1_name not in fractions_dict:
        print(f"Name {frac1_name} was not found")
        return

    frac2_name = input("2nd operand: ")

    if frac2_name not in fractions_dict:
        print(f"Name {frac2_name} was not found")
        return

    # we multiply the fractions together
    fraction1 = fractions_dict[frac1_name]
    fraction2 = fractions_dict[frac2_name]

    # multiply and print
    product_fraction = fraction1.multiply(fraction2)

    print(f"{fraction1} * {fraction2} = {product_fraction}")
    product_fraction.simplify()
    print(f"simplified {product_fraction}")


def read_fractions_from_file(fractions_dict):
    """
    Reads fractions from file with format =name= x/y where x and y are
    integers. Appens the fractions to fractions_dict. Stops reading file
    if an invalid format is detected while reading file

    :param fractions_dict: dict, key=name and value=fraction are stored in the
    dictionary
    """
    filename = input("Enter the name of the file: ")

    # we try to open the file and display error if not possible
    try:
        file = open(filename, "r")
    except OSError:
        print("Error: the file cannot be read.")
        return

    # read the names and fractions from the file and append them to
    # fractions_dict
    # expected format name=int/int
    # display error if format is incorrect
    try:
        for line in file:
            # name is parsed by parsing the output from index=0 to equals sing
            name = line[:line.index("=")]

            # values for the frac can be parsed by finding the numerator and
            # denominator after the equals sign and splitting the remaining
            # text with split("/")
            numerator, denominator = line[line.index("=")+1:].split("/")

            # we add the fraction with key=<name> and value=<Fraction> (object)
            # to the fractions list
            fractions_dict[name] = Fraction(int(numerator), int(denominator))
    except ValueError:
        print("Error: the file cannot be read.")
        file.close()
        return

    file.close()


def main():
    # we define the dict where the keys and values are stored. The format is
    # name = key and fraction = value
    fractions_dict = {}

    # menu loop
    while True:
        command = input("> ")

        if command == "add":
            add(fractions_dict)
        elif command == "quit":
            print("Bye bye!")
            return
        elif command == "print":
            print_fraction(fractions_dict)
        elif command == "list":
            list_fractions(fractions_dict)
        elif command == "*":
            multiply_two_fractions(fractions_dict)
        elif command == "file":
            read_fractions_from_file(fractions_dict)
        else:
            print("Unknown command!")


if __name__ == "__main__":
    main()
