# Parsing input from user and additional arguments
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Decorator to handle input errors
def input_errors(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except KeyError as e:
            return f"User {e.args[0]} not found"
        except IndexError:
            return "Enter user name"
        except Exception as e:
            return f"Error: {e}"
    return inner

# Adds new contact to the dictionary
@input_errors
def add_contact(args, contacts):
    name, phone = args
    if phone.startswith('+'):
        if not phone[1:].isdigit():
            raise ValueError("Only digits should be after +")
    elif not phone.isdigit():
        raise ValueError("Only digits should be in the phone number")
    contacts[name] = phone
    return "Contact added."

# Changes existing contact in the dictionary (updates phone number)
@input_errors
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        if phone.startswith('+'):
            if not phone[1:].isdigit():
                raise ValueError("Only digits should be after +")
        elif not phone.isdigit():
            raise ValueError("Only digits should be in the phone number")
        contacts[name] = phone
        return "Contact updated"
    else:
        raise KeyError(name)

# Shows phone number for contact by name
@input_errors
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"User's {name} phone number is {contacts[name]}"
    else:
        raise KeyError(name)

# Shows all contacts in dictionary
@input_errors
def all_contacts(args, contacts):
    if not contacts:
        return "Contact book is empty"
    contact_book = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return f"Contact book:\n{contact_book}"

# Main function which handles all inputs and outputs
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            result = add_contact(args, contacts)
            print(result)
        elif command == "change":
            result = change_contact(args, contacts)
            print(result)
        elif command == "phone":
            result = show_phone(args, contacts)
            print(result)
        elif command == "all":
            result = all_contacts(args, contacts)
            print(result)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
