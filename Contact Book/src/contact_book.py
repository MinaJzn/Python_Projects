class ContactBook:
    """
    This is a ContactBook that stores user names with their phone numbers.
    """
    def __init__(self):
        self.my_contact=dict()
        self.next_id=1
        
    def add_contact(self , user_name:str , phone:str=None):
        """Add a new contact.
        
        :param phone:The phone number of the contact (must be a string).
                     If given as an integer, an error may occur.
        """
        self.user_name=user_name
        self.phone=phone
        self.my_contact[self.next_id]={'User Name':self.user_name,'Contact User':self.phone}
        self.next_id+=1
        
    def delete_user(self , contact_id:int):
        """Remove a contact by their ID"""
        self.contact_id=contact_id
        if self.contact_id in self.my_contact.keys():
            removed=self.my_contact.pop(self.contact_id)
            print(f'Contact "{removed['User Name']}" with this contact "{removed['Contact User']}" removed!')
        else:
            print('No contact found with that ID !')
    
    
    def update_user(self , contact_id:int , new_phone:str):
        """
        Update the phone number of an existing contact.
        """
        self.contact_id=contact_id
        self.new_phone=new_phone
        if self.contact_id in self.my_contact.keys():
            self.my_contact[contact_id]['Contact User']=self.new_phone
        else:
            print('No contact found with that ID !')
        
        
    def show_all_contact(self):
        """
        Display all saved contacts.
        """
        for i,user in self.my_contact.items():
            print (f'{i} : Name= {user['User Name']} , Contact= {user['Contact User']}\n{"-"*50}')
        
        
if __name__ == "__main__":
    book = ContactBook()
    
    while True:
        print("\n--- Contact Book Application ---")
        print("1. Add contact")
        print("2. Delete contact")
        print("3. Edit contact")
        print("4. View contacts")
        print("5. Quit")
        user_choice = input("\nPlease choose an option: ")

        if user_choice == '1':
            name = input("\nEnter Contact name: ")
            phone = input("Enter Contact phone: ")
            book.add_contact(name, phone)

        elif user_choice == '2':
            contact_id = int(input("\nEnter ID of contact to delete: "))
            book.delete_user(contact_id)

        elif user_choice == '3':
            contact_id = int(input("\nEnter ID of contact to update: "))
            phone = input("Enter new/updated phone number : ")
            book.update_user(contact_id, phone)

        elif user_choice == '4':
            print("\nshow all Contacts:")
            book.show_all_contact()

        elif user_choice == '5':
            print("\nThank You for using Contact Book Application. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please try again.")