import os
import ssl
import smtplib
from string import Template
from email.message import EmailMessage


# Return two lists names, emails containing names and email addresses
def get_contacts(filename):
    names = []
    emails = []
    contacts_file = open(filename, mode='r', encoding='utf-8')
    for a_contact in contacts_file:
        names.append(a_contact.split()[0])
        emails.append(a_contact.split()[1])
    contacts_file.close
    return names, emails


# Returns a Template object comprising the contents of the 
def read_template(filename):    
    template_file = open(filename, mode='r', encoding='utf-8')
    template_file_content = template_file.read()
    template_file.close()
    return Template(template_file_content)

# send email function
def send_email():
    sender = 'anndrei014@gmail.com'
    app_psswd = os.environ.get('EMAIL_PASSWORD')
    # receiver = 'andreidinu408@yahoo.com'

    subject = 'Informative Message'
    # message = 'Hello My Neighbours'

    # read contacts
    names, emails = get_contacts('contacts.txt')
    message_template = read_template('message.txt')

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

if __name__ == '__main__':
    send_email()
