# -*- coding: utf-8 -*-.



"""MANJKA: branje kontaktov iz TXT datoteke in kreacija objektov iz njih (to naj se zgodi, ko uporabnik zažene ContactBook program)"""




class Contact(object):
    def __init__(self, first_name, last_name, phone_number, birth_year):
        self.first_name=first_name
        self.last_name=last_name
        self.phone_number=phone_number
        self.birth_year=birth_year

contacts_list = []


while True:
    new = raw_input("Please, add new contact. Press enter. If you want to cancel, press n. ")
    if new== "n":
        break
    else:
        person = Contact(first_name=str(raw_input("Enter first name: ")), last_name=str(raw_input("Enter last name: ")), phone_number=str(raw_input("Enter a phone number: ")), birth_year=str(raw_input("Enter birth year: ")))
        contacts_list.append(person)


for person in contacts_list:
    print "First name: " + person.first_name
    print "Last name: " + person.last_name
    print "Phone number: " + str(person.phone_number)
    print "Birth year: " + str(person.birth_year)
    print "_________________________"

while True:
    edit = raw_input("Do you want to edit any of the contacts? yes/no")
    if edit == "no":
        break
    else:
        wrong = str(raw_input("Which information do you want to correct? Write the information as in the existing Contactbook:"))
        right = str(raw_input("Write the correct information:"))

    for person in contacts_list:
        if person.first_name == wrong:
            person.first_name = right
        if person.last_name == wrong:
            person.last_name = right
        if person.phone_number == wrong:
            person.phone_number = right
        if person.birth_year == wrong:
            person.birth_year = right


for person in contacts_list:
    print "First name: " + person.first_name
    print "Last name: " + person.last_name
    print "Phone number: " + str(person.phone_number)
    print "Birth year: " + str(person.birth_year)
    print "_________________________"


while True:
    deletion = raw_input("Do you want to delete any of the contacts? Press yes to delete, press no to exit programme.")
    if deletion == "no":
        break
    else:
        delete_what = str(raw_input("Which contact do you want to delete? Write the name of the contact as in the existing Contactbook:"))

    for person in contacts_list:
        if delete_what == person.first_name:
            contacts_list.remove(person)

ContactBook = open("ContactBook.txt", "w+")



ContactBook.write("All contacts:\n")

for person in contacts_list:
    print "First name: " + person.first_name
    print "Last name: " + person.last_name
    print "Phone number: " + str(person.phone_number)
    print "Birth year: " + str(person.birth_year)
    print "_________________________"

    ContactBook.write("- " +  "First name: " + person.first_name + ";" " Last name: " + person.last_name + ";" " Phone number: " + str(person.phone_number) + ";" " Birth year: " + str(person.birth_year) + "\n")

ContactBook.close()


