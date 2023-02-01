import smtplib, ssl

def otpmailbody(AppName, firstName, lastname, otpp, supportmailid):
    message = """
    Subject: Welcome to """ + AppName + """ | Account Verification OTP

    Hi """ + firstName + " " + lastname + """,

    Your OTP is : """ + str(otpp) + """

    This will be valid for next 30 minutes only.
    Do not reply to this email.
    For any concerns / queries,
    Please reach out to """ + supportmailid + """.

    Thanks & Regards,
    Team """ + AppName + "\n\n"
    return message


def otpmailbodypasswordRecovery(AppName, firstName, lastname, otpp, supportmailid):
    message = """
    Subject: """ + AppName + """ | Password Recovery OTP

    Hi """ + firstName + " " + lastname + """,

    Your OTP is : """ + str(otpp) + """

    This will be valid for next 30 minutes only.
    Do not reply to this email.
    For any concerns / queries,
    Please reach out to """ + supportmailid + """.

    Thanks & Regards,
    Team """ + AppName + "\n\n"
    return message

def sendEmail(email, mailbody):
    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP("smtp.office365.com", 587)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login("noreply@simplify3x.com", "#simplify123")
        server.sendmail("noreply@simplify3x.com", email, mailbody)
    except Exception as e:
        print(e)
    finally:
        server.quit()