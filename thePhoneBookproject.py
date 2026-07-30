phone_book = {
    "Ali": "05555555",
    "Sara": "06666666",
    "Adam": "07777777"
}

while True:
    print("""
==== PHONE BOOK ====
1. Add Contact
2. Search Contact
3. Show All Contacts
4. Exit  """)
    choose = int(input("choose: "))

    if choose == 1:
        new_contactname = input("add the name of the new contact: ")
        new_contactnumber = input("add the number of the new contact: ")
        phone_book[new_contactname] = new_contactnumber

    elif choose == 2:
        contact = input("search for a contact: ")
        if contact in phone_book:
            print(phone_book.get(contact))
        else:
            print("Contact not found.")

    elif choose == 3:
        print(phone_book)

    elif choose == 4:
        print("Exit")
        break








    
  
     
    

      
      
    
    

  
