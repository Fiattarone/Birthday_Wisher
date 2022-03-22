import smtplib

my_email = "birthdayreminders00@gmail.com"
my_password = "12345"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="fiattarone@me.com", msg="hi")
connection.close()