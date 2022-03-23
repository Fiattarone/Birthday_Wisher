import smtplib
import datetime as dt
from random import choice

now = dt.datetime.now()
my_email = "birthdayreminders00@gmail.com"
my_password = "xyzlul!"

# Monday
if now.weekday() == 0:
    subject = "Inspirational Quote"
    with open("quotes.txt") as quotes:
        quoteList = quotes.readlines()
        body = choice(quoteList)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="fiattarone@me.com", msg=f"subject:{subject}\n\n{body}")

