# Q03a
import re
#	Open the file and input data
badEmails = []
try:

    with open("Email.txt", "r") as Emails:
        for Email in Emails:
            # print(Email)
            found = re.search("@", Email)
            if not found:
                badEmails.append(Email)


#	Open output file
    with open("badEmails.txt","w") as file:
#	Find errors and write to output file
       for Line in badEmails:
            file.write(Line)
except:
    print("error")
#	Close files

# No need to as we are using "with" when dealing with the files