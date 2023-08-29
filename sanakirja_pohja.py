"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.
"""

def print_dict_content(dict):
    """
    Prints the contencts of the dict separated with a comma
    :param dict: dict, the dictionary to print the values from
    :return: None
    """
    print("Dictionary contents:")
    output = ", ".join(sorted(dict))
    print(output)

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    # print out the dictionary contents:
    print_dict_content(english_spanish)

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word =  input("Enter the word to be translated: ")
            if word in english_spanish:
                spanish_word = english_spanish[word]
                print(f"{word} in Spanish is {spanish_word}")
            else:
                print("The word", word, "could not be found from the"
                                        " dictionary.")

        elif command == "A":
            word = input("Give the word to be added in English: ")
            spanish_word = input("Give the word to be added in Spanish: ")
            english_spanish[word] = spanish_word
            print_dict_content(english_spanish)

        elif command == "R":
            word = input("Give the word to be removed: ")
            if word in english_spanish:
                del english_spanish[word]
            else:
                print(f"The word {word} could not be found from the dictionary.")

        elif command == "P":
            # we create the spanish- english dict on the fly
            spanish_english = {}
            print()
            print("English-Spanish")
            for word in sorted(english_spanish):
                print(word, english_spanish[word])
                spanish_english[english_spanish[word]] = word

            print()
            print("Spanish-English")
            for word in sorted(spanish_english):
                print(word, spanish_english[word])
            print()

        elif command == "T":
            sentence = input("Enter the text to be translated into Spanish: ")
            words = sentence.split()
            print("The text, translated by the dictionary:")

            i = 0
            for word in words:
                i += 1
                if word in english_spanish:
                    print(english_spanish[word], end="")
                else:
                    print(word, end="")
                if i < len(words):
                    print(" ", end="")
            print()

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
