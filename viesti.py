"""
COMP.CS.100 Programming 1
Code Template
"""
def read_message():
    """
    Reads user input and appends each input row to a list
    :return: list, list of text rows inputted by the user
    """
    msg_list = []
    while True:
        msg = input()
        if msg == "":
            break
        msg_list.append(msg)
    return msg_list


def print_message(message_list):
    """
    Prints text rows from a supplied list <message_list>
    :param message_list: list, the messages to print
    :return: None
    """
    for message in message_list:
        print(message.upper())


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("The same, shouting:")
    print_message(msg)


if __name__ == "__main__":
    main()
