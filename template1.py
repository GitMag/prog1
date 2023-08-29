"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id:
Name:
Email:

Template for sorting by price assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def payload(key):
    """
    Get value with a given key from dictionary. Returns value
    :param key: str, key for dict
    :return: int, value from dict item
    """
    return PRICES[key]


def main():
    for item in sorted(PRICES, key=payload):
        print(f"{item} {PRICES[item]:.2f}")


if __name__ == "__main__":
    main()
