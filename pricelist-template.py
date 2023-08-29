"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id:
Name:
Email:

Template for pricelist assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def print_price(key):
    """
    Print out the price from the dict <PRICES> with <key>. If key not in dict
    prints out that the price is unknown
    :param key: key to search from dict
    :return: None
    """
    if key in PRICES:
        price = PRICES[key]
        print(f"The price of {key} is {price:.2f} e")
    else:
        print(f"Error: {key} is unknown.")


def main():
    while True:

        product_name = input("Enter product name: ")

        #we remove uselelss spaces
        product_name = product_name.strip()

        #check if product name is empy
        if product_name == "":
            break
        else:
            print_price(product_name)
    print("Bye!")


if __name__ == "__main__":
    main()
