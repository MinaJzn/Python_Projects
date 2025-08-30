# Contact Book
A simple command-line contact management system built with Python. This app allows users to **add**, **view**, **update**, and **delete** contacts easily. Each contact is stored with a unique ID, name, and phone number.
## Project Structure
```
Contact Book/
│
├── src/
│   ├── contact_book.py - The main game class
│
├── README.md - This file
```

## ContactBook Class
```python
class ContactBook
```

### Methods:

- `add_contact(user_name: str, phone: str = None)`
Adds a new contact with the given name and optional phone number.

- `delete_user(contact_id: int)`
Deletes a contact using their unique ID.

- `update_user(contact_id: int, new_phone: str)`
Updates the phone number of a contact with the given ID.

- `show_all_contact()`
Displays all contacts in a readable format.

## Running the Project
1. **Run the script**
```bash
cd src
python contact_book.py
```
2. **Follow the menu**
```markdown
1. Add contact
2. Delete contact
3. Edit contact
4. View contacts
5. Quit
```
3. **Input your desired option and follow the prompts.**

## Example
```bash
--- Contact Book Application ---
1. Add contact
2. Delete contact
3. Edit contact
4. View contacts
5. Quit

Please choose an option: 1

Enter Contact name: Alice
Enter Contact phone: 123456789
```

## Notes
- The phone number should be entered as a string (e.g., '123456789') to avoid any formatting issues.
- This is a simple, in-memory implementation. Closing the app will erase all contacts.
- Contacts are stored based on their unique ID and can be deleted or edited accordingly.


---
<p align="center">👧 Author: <b>Mina Jazini</b></p>
