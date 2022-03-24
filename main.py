import smtplib
import datetime as dt
# from random import choice
import pandas
import contact

now = dt.datetime.now()
my_email = "birthdayreminders00@gmail.com"
my_password = "ENTER PASSWORD HERE"

data = pandas.read_csv("birthdays.csv")
# print(data["month"])
birthday_line = data[data["month"] == now.month]
birthday_line = birthday_line[birthday_line["day"] == now.day].values.tolist()


def send_email(contact_obj, letter_number):
    email_subject = "Happy Birthday from David!"
    with open(f"letter_templates/letter_{letter_number}.txt") as letter:
        email_letter = letter.read()
        # print(new_letter)
        email_letter = email_letter.replace("[NAME]", contact_obj.name)
        # print(new_letter)
        with smtplib.SMTP("smtp.gmail.com", port=587) as econnection:
            econnection.starttls()
            econnection.login(user=my_email, password=my_password)
            econnection.sendmail(from_addr=my_email, to_addrs=contact_obj.email,
                                msg=f"subject:{email_subject}\n\n{email_letter}")


if birthday_line:
    contacts = []
    if type(birthday_line[0]) == type([]):
        print("There was an array in here")
        for arr in birthday_line:
            contacts.append(contact.Contact(name=arr[0], email=arr[1], month=arr[2], day=arr[3]))

    # check to see if this contact has already had a birthday sent to them before, if not,
    # send them letter 1 and write them on the list
    sending_letter = []
    # subject = "Happy Birthday from David!"

    try:
        sent_data = pandas.read_csv("birthday_sent_list.csv")
    except FileNotFoundError:
        print("File wasn't found! Make, continue with letter one for this person(s) and record them")
        new_data = pandas.DataFrame([x.return_self_list_append_one()
                                     for x in contacts]).to_csv("birthday_sent_list.csv")
        #Send the first letter
        for person in contacts:
            send_email(contact_obj=person, letter_number=1)
    except smtplib.SMTPAuthenticationError:
        print("Something's wrong with gmail, go fix!")
    else:
        print("read and update data")
        list_of_letter_numbers = sent_data.values.tolist()
        print(list_of_letter_numbers)

        # Quadratic, O(n**2), brute force for now.
        edited_contacts = []
        for x in list_of_letter_numbers:
            for person in contacts:
                if x[1] == person.name:
                    send_email(contact_obj=person, letter_number=x[5]+1)
                    # Save the number of the letter just sent
                    edited_contacts.append(person.return_self_list_append(x[5]+1))
                    if x[5]+1 > 3:
                        print("ALERT NEED MORE LETTERS")
                        send_email(contact.Contact(name="David", email="fiattarone@me.com"), 99999)
        pandas.DataFrame([x for x in edited_contacts]).to_csv("birthday_sent_list.csv")

# Monday
# if now.weekday() == 0:
#     subject = "Inspirational Quote"
#     with open("quotes.txt") as quotes:
#         quoteList = quotes.readlines()
#         body = choice(quoteList)
#
#     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=my_password)
#         connection.sendmail(from_addr=my_email, to_addrs="fiattarone@me.com", msg=f"subject:{subject}\n\n{body}")
