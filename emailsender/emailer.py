import smtplib

print("Please enable less secure app in gmail at this url:\n https://myaccount.google.com/lesssecureapps")

recipient = input("Please enter the email of the recipient:...\n")
message_content = input("Please enter the content of the email:...\n")
your_email = input("Please enter your email:...\n")
your_password = input("Please enter your email password:..\n")



def emailer(recipient, message_content, your_email,your_password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(your_email,your_password)
    server.sendmail(your_email, recipient, message_content)
    server.close()

emailer(recipient,message_content,your_email,your_password)