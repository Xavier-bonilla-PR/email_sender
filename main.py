try:
    import yagmail
    import keyring

    # Initialize the SMTP object
    yag = yagmail.SMTP({
        'your_email@gmail.com': 'Your Name'
    }, oauth2_file="~/oauth2_creds.json")

    #Variables
    to = 'your_email@gmail.com'
    subject = 'Can you read me?'
    body = 'Hi! My name is Joe. Just testing if this works.'
    html = '<a href="https://pypi.python.org/pypi/sky/">Click me!</a>'
    img = 'Saspost.jpg'


    # Send the email with inline
    #yag.send(to = [to], subject = subject, contents = [body, yagmail.inline(img)])
    
    # Send email with template
    template = """
    Dear {name},
    Your order #{order_id} is ready.
    """
    yag.send(contents=[template.format(name='John', order_id='12345')])
    
    print("Email sent successfully!")

except Exception as e:
    print(f"Error occurred: {str(e)}")
