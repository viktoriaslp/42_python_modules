import json

from pydantic import ValidationError
from ex1.alien_contact import AlienContact


def main() -> None:
    with open("generated_data/alien_contacts.json", "r", encoding="utf-8") as file:
        contacts_data = json.load(file)
    
    for item in contacts_data:
        try:
            contact = AlienContact(**item)
            contact.show_info()
            print()
        except ValidationError as error:
            print("invalid contact:")
            for err in error.errors():
                print(err[msg])


if __name__ == "__main__":
    main()
