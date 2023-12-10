# Importing the Required Library
import os
import ssl
import smtplib
import pywhatkit
from string import Template
from twilio.rest import Client
from email.message import EmailMessage


# Return two lists names, emails containing names and email addresses
def get_contacts(filename):
    names = []
    emails = []
    phones = []
    contacts_file = open(filename, mode='r', encoding='utf-8')
    for a_contact in contacts_file:
        names.append(a_contact.split()[0])
        emails.append(a_contact.split()[1])
        phones.append(a_contact.split()[2])
    contacts_file.close()
    return names, emails, phones


# Returns a Template object comprising the contents of the 
def read_template(filename):
    template_file = open(filename, mode='r', encoding='utf-8')
    template_file_content = template_file.read()
    template_file.close()
    return Template(template_file_content)


# send email function
def send_email(File_contacts, File_message):
    sender = 'anndrei014@gmail.com'
    # EMAIL_PASSWORD should be in bashrc/zshrc..
    app_psswd = os.environ.get('EMAIL_PASSWORD')
    # receiver = 'andreidinu408@yahoo.com'

    subject = 'Informative Message'
    # message = 'Hello My Neighbours'

    # read contacts
    names, emails, phones = get_contacts(File_contacts)
    message_template = read_template(File_message)

    # For each contact, send the email:
    for receiver_name, receiver_email in zip(names, emails):
        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=receiver_name.title())

        em = EmailMessage()
        em['From'] = sender
        em['To'] = receiver_email
        em['Subject'] = subject
        em.set_content(message)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender, app_psswd)
            smtp.sendmail(sender, receiver_email, em.as_string())


# Do not touch anything when running
def send_Wapp_Message(message, File_contacts):
    # Defining the Phone Number and Message
    names, emails, phones = get_contacts(File_contacts)

    # Sending the WhatsApp Message
    for phone_number in phones:
        pywhatkit.sendwhatmsg_instantly(phone_number, message, 4, True, 1)

    # Displaying a Success Message
    print("WhatsApp message sent!")


# Sender and Receiver should have phone numbers verified by Twilio
def send_sms(message, File_contacts):
    # Defining the Phone Number and Message
    names, emails, phones = get_contacts(File_contacts)
    # ACCOUNT_SID, AUTH_TOKEN and TWILIO_NUMBER should be defined in bashrc/zshrc..
    account_sid = os.environ.get('ACCOUNT_SID')
    auth_token = os.environ.get('AUTH_TOKEN')
    twilio_number = os.environ.get('TWILIO_NUMBER')

    client = Client(account_sid, auth_token)
    for p in phones:
        sms = client.messages.create(
            body=message,
            from_=twilio_number,
            to=p
        )

        print(sms.body)