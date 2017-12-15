#asking user a string
userstring = raw_input("enter a string to check if it is palindrome :")
userstring = userstring.lower()
if userstring == userstring[::-1]:
    print "the word is palindrome"
else:
    print "the word entered is not a palindrome"

