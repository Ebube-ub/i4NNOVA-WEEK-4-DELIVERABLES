from contact_form import ContactForm
from typing import List

def main():
    contact_file_path = 'contact.csv'


    contact = get_user_contact()
    
    
    save_contact_to_file(contact, contact_file_path)
    
    
    summarize_contacts(contact_file_path, ContactForm)




def get_user_contact():
    print(f'Getting user contact details')
    user_name = input("Enter your name: ")
    user_amount = input("Enter your Student ID: ")
    user_email = input("Enter your email: ")
    user_phone_number = input("Enter your phone number: ")

    return ContactForm(name=user_name, ID=user_amount, email=user_email, phone_number=user_phone_number)

  

def save_contact_to_file(contact, contact_file_to_path):
    print(f'Saving User Contact: {contact} to {contact_file_to_path}')
    with open(contact_file_to_path, 'a') as f:
        f.write(f'{contact.name},{contact.ID},{contact.email},{contact.phone_number}\n')


def summarize_contacts(contact_file_path, contact_form):
    contacts : List[ContactForm] = []
    with open(contact_file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            contact_name, contact_ID, contact_email, contact_phone_number = line.strip().split(',')
            print(contact_name, 
                  contact_ID, 
                  contact_email,
                  contact_phone_number)
            line_contact = ContactForm(name=contact_name, ID=contact_ID, email=contact_email, phone_number=contact_phone_number)
            print(line_contact)
            contacts.append(line_contact)
    print(f'\nYou have {len(contacts)} contacts saved.')


   

if __name__ == "__main__":
    main()
