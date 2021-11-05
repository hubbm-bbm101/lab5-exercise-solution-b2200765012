def isitemail(b):
    if "." and "@" in b:
        return True
    else:
        return False
    
    
email=str(input("please enter your email"))
if isitemail(email) == True:
    print(email + " is is a valid e-mail thank you")
else:
    print(email + " isn't a valid e-mail sorry")