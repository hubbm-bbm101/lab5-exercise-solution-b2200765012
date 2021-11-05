def isitemail(b):
    if "." and "@" in b:
        return True
    else:
        return False
email=input("please enter your email: ")
while isitemail(email)==False:
	print(email , " isn't a valid e-mail")
	email=input("please enter a valid email: ")
print(email , " is is a valid e-mail")
