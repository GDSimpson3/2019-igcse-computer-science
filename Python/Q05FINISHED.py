#Q05FINISHED

libraryRecord =  [
["105MS" , "Marcus" , "Smith" , 25 ],
["103AZ" , "Anthony" , "Zarrent" , 5 ],
["108MW" , "Matt" , "White" , 12 ],
["112DB" , "Denise" , "Bilton" , 58 ],
["124MK" , "Malcolm" , "Kelly" , 26 ],
["116UK" , "Uzere" , "Kevill" , 29 ],
["127AL" , "Abduraheim" , "Leahy" , 94 ],
["124LS" , "Laura" , "Sampras" , 50 ],
["121AP" , "Azra" , "Potter" , 61 ],
["115AC" , "Anthony" , "Calik" , 10 ],
["117PI" , "Pablo" , "Iilyas" , 49 ],
["113MM" , "Mark" , "Montgomerie" , 68 ],
["130FH" , "Felicity" , "Heath" , 11 ],
["132JA" , "Jill" , "Alexander" , 61 ],
["123SG" , "Sara" , "Grimstow" , 9 ],
["134KD" , "Kevin" , "Dawson" , 74 ],
["122AB" , "Andrew" , "Bertwistle" , 42 ],
["125JF" , "Jaide" , "Feehily" , 55 ],
["128JS" , "Justin" , "Slater" , 68 ],
["126CG" , "Colleen" , "Grohl" , 39 ]
]


# ----------------------------------------------
# Write your code below this line
totalNumberOfBooksRead =0
totalnumberofstudents =0

bottom10 = []
Gold = libraryRecord[0]
Silver = libraryRecord[0]
Bronze = libraryRecord[0]


for Pupil in libraryRecord:
    totalNumberOfBooksRead = totalNumberOfBooksRead + Pupil[3]
    totalnumberofstudents = totalnumberofstudents + 1
    if Pupil[3] > Gold[3]:
        Gold = Pupil
    if Pupil[3] > Silver[3] and not Pupil == Gold:
        Silver = Pupil
    if Pupil[3] > Bronze[3] and not (Pupil == Gold) and not (Pupil == Silver):
        Bronze = Pupil
    if Pupil[3] < 10:
        print("-" *len(f'| Shame on | {Pupil[1]} {Pupil[2]} | for reading less than 10 |'))
        print(f'| Shame on | {Pupil[1]} {Pupil[2]} | for reading less than 10 |')
        print("-" *len(f'| Shame on | {Pupil[1]} {Pupil[2]} | for reading less than 10 |'))

print("-" *len(f"| Gold | {Gold[1]} | {Gold[2]} | {Gold[3]} | {Gold[0]} |"))
print(f'| Gold | {Gold[1]} | {Gold[2]} | {Gold[3]} | {Gold[0]} |')
print("-" *len(f"| Gold | {Gold[1]} | {Gold[2]} | {Gold[3]} | {Gold[0]} |"))

print("-" *len(f"| Silver | {Silver[1]} | {Silver[2]} | {Silver[3]} | {Silver[0]} |"))
print(f'| Silver | {Silver[1]} | {Silver[2]} | {Silver[3]} | {Silver[0]} |')
print("-" *len(f"| Silver | {Silver[1]} | {Silver[2]} | {Silver[3]} | {Silver[0]} |"))

print("-" *len(f"| Bronze | {Bronze[1]} | {Bronze[2]} | {Bronze[3]} | {Bronze[0]} |"))
print(f'| Bronze | {Bronze[1]} | {Bronze[2]} | {Bronze[3]} | {Bronze[0]} |')
print("-" *len(f"| Bronze | {Bronze[1]} | {Bronze[2]} | {Bronze[3]} | {Bronze[0]} |"))

averageNumberOfBooksRead = totalNumberOfBooksRead / totalnumberofstudents

print("-" *len(f'| Average Books | {averageNumberOfBooksRead} |'))
print(f'| Average Books | {averageNumberOfBooksRead} |')
print("-" *len(f'| Average Books | {averageNumberOfBooksRead} |'))

print("-" *len(f'| Total Books read | {totalNumberOfBooksRead} |'))
print(f'| Total Books read | {totalNumberOfBooksRead} |')
print("-" *len(f'| Total Books read | {totalNumberOfBooksRead} |'))

