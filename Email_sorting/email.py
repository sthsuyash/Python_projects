def send_emails(emails):
    # Create a dictionary to store the email addresses by domain
    email_dict = {}
    for email in emails:
        # Extract the domain from the email address
        domain = email.split('@')[1]

        # Add the email address to the dictionary
        if domain not in email_dict:
            email_dict[domain] = []
        email_dict[domain].append(email)

    # Send an email to the first address (in alphabetical order) for each domain
    for domain, addresses in email_dict.items():
        sendmail(addresses[0])  # assumed function to send mail

# assumed function


def sendmail(email):
    print(email)


# main function
if __name__ == "main":
    emails = [
        'ghi@hotmail.com',
        'def@yahoo.com',
        'ghi@gmail.com',
        'abc@channelier.com',
        'abc@hotmail.com',
        'def@hotmail.com',
        'abc@gmail.com',
        'abc@yahoo.com',
        'def@channelier.com',
        'jkl@hotmail.com',
        'ghi@yahoo.com',
        'def@gmail.com'
    ]
    send_emails(emails)
