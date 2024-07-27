# Address Book Exercise
def look_up(add_book, name):
    """ return the corresponding address """
    return add_book[name]


def add(add_book, name, address):
    """ adds an address to the address book"""
    add_book[name] = address


def edit(add_book, name, new_address):
    """ edits the address entry for name with a new address"""
    add_book[name] = new_address


def delete(add_book, name):
    """ deletes name and the address from the addressbook """
    del add_book[name]


def list_all(add_book):
    """ prints out all the addresses

    e.g.

    address_book = {

    }

    would print out

    Name:
    Address:

    Name:
    Address:

    """
    for key, value in add_book.items():
        print(f"Name: {key}")
        print(f"Address: {value}\n")


def main():
    # define empty address book
    address_book = {

    }

    choice = None
    while choice != "0":
        print(
            """Address Book
        0 - Quit
        1 - Look Up an Address
        2 - Add an Address
        3 - Edit an Address
        4 - Delete an Address
        5 - List Addresses
        """
        )
        choice = input("Choice: ")
        print()
        # exit
        if choice == "0":
            print("Good-bye.")
            # get a definition
        elif choice == "1":
            look_up_name = input("Please enter a name to look up their address:\n")
            if look_up_name in address_book:
                address = look_up(address_book, look_up_name)
                print(address)
            else:
                print(f"ERROR: No entry for {look_up_name} found.\n")
        # add a term-definition pair
        elif choice == "2":
            name_to_add = input("Please enter a name you wish to add:\n")
            if name_to_add not in address_book:
                address = input("What's the address?: ")
                add(address_book, name_to_add, address)
                print(f"\n{name_to_add} has been added.\n")
            else:
                print("ERROR: Name already exists.\n")
        # redefine an existing term
        elif choice == "3":
            name_to_edit = input("Please enter the name of the address you wish to edit: ")
            if name_to_edit in address_book:
                new_address = input("What's the new address?: ")
                edit(address_book, name_to_edit, new_address)
                print("\nAddress for ", name_to_edit, " has been edited.\n")
            else:
                print(f"\n{name_to_edit} is not in the address book.\n")
            # delete a term-definition pair
        elif choice == "4":
            name_to_del = input("What term do you want me to delete?: ")
            if name_to_del in address_book:
                delete(address_book, name_to_del)
                print(f"\nOkay, I deleted {name_to_del}\n")
            else:
                print(f"\nI can't do that! {name_to_del} doesn't exist in the address book.\n")
        elif choice == "5":
            list_all(address_book)
        else:
            print(f"Sorry, but {choice} isn't a valid choice.\n")


if __name__ == "__main__":
    main()