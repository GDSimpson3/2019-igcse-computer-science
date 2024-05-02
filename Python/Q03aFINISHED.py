# Q03a
import re
#	Open the file and input data
badEmails = []
try:

    emailtxt =  open("Email.txt", "r")

#	Open output file
    bademailstxt =  open("badEmails.txt","w")

#	Find errors and write to output file
    for Email in emailtxt:
        found = re.search("@", Email)
        if not found:
            badEmails.append(Email)

    for Line in badEmails:
        bademailstxt.write(Line)
    
except:
    print("an error occured")

#	Close files
emailtxt.close()
bademailstxt.close()
# No need to as we are using "with" when dealing with the files