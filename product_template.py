"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Template for the product assignment.
"""


class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    def __init__(self, product_name, product_price, sale_percentage=0.0):
        """
        We initialize the product object with a product name and price

        :param product_name: str, the name of the product
        :param product_price: float, the price of the product
        :param sale_percentage: float, the sales percentage for the product
        price. Defaults to 0% if no args are passed.
        """

        self.__product_name = product_name
        self.__price = product_price
        self.__sale_percentage = sale_percentage

    def set_sale_percentage(self, percentage):
        """
        Sets the sale percentage for the product
        :param percentage: float, the sales percentage (0-100%)
        :return:
        """

        self.__sale_percentage = percentage

    def get_price(self):
        """
        Returns the price for the product, taking into account the sales
        percentage.
        :return: float, the price of the product
        """

        return self.__price * (100 - self.__sale_percentage) / 100

    def printout(self):
        print(self.__product_name)
        print(f"  price: {self.__price:0.2f}")
        print(f"  sale%: {self.__sale_percentage:0.2f}")
        print(20 * "-")


def main():
    ################################################################
    #                                                              #
    #  You can use the main-function to test your Product class.   #
    #  The automatic tests will not use the main you submitted.    #
    #                                                              #
    #  Voit käyttää main-funktiota Product-luokkasi testaamiseen.  #
    #  Automaattiset testit eivät käytä palauttamaasi mainia.      #
    #                                                              #
    ################################################################

    test_products = {
        "milk": 1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
