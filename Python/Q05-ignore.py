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

def mergesort(list):
    if len(list) > 1:
        mid = len(list) / 2
        left = list[:mid]
        right = list[mid:]

        mergesort(left)
        mergesort(right)

        i, j, k =0
        
        while i < len(left) and j < len(right):
            if(left[i] <= right[j]):
                list[k] = left[i]
            else:
                list[k] = right[j]
            k = k+1
        while i < len(left):
            list[k] = left[i]
            i = i+1
            k=k+1
        while j < len(right):
            list[k] = right(j)
            j=j+1
            k=k+1



bookandid = [[],[]] # 0 for Ids, 1 for Books

# bookandid= []

for Pupil in libraryRecord:
    totalNumberOfBooksRead = totalNumberOfBooksRead + Pupil[3]
    totalnumberofstudents = totalnumberofstudents + 1
    if Pupil[3] > Gold[3]:
        Gold = Pupil
    if Pupil[3] > Silver[3] and not Pupil == Gold:
        Silver = Pupil
    if Pupil[3] > Bronze[3] and not (Pupil == Gold) and not (Pupil == Silver):
        Bronze = Pupil
    # bookandid[1].append(Pupil[3]) 
    bookandid.append(Pupil) 

    
print(bookandid)
# def getquantity(object):
#     return object.booksread
sortedbookd = bookandid[1].sort()

# print(bookandid)


for i in range(0,10):
    print("IIII")
    for q in range(0,10):
        print("QQQ")

        print(bookandid[1][q])
        print(bookandid[0][3][q])
        if(bookandid[1][q] == bookandid[0][i]):        
            bottom10.append(bookandid[0][q])


print("aaaa")
for z in bottom10:
    print(z)



# print("-" *len(f"| Gold | {Gold[1]} | {Gold[2]} | {Gold[3]} | {Gold[0]} |"))
# print(f'| Gold | {Gold[1]} | {Gold[2]} | {Gold[3]} | {Gold[0]} |')
# print("-" *len(f"| Gold | {Gold[1]} | {Gold[2]} | {Gold[3]} | {Gold[0]} |"))

# print("-" *len(f"| Silver | {Silver[1]} | {Silver[2]} | {Silver[3]} | {Silver[0]} |"))
# print(f'| Silver | {Silver[1]} | {Silver[2]} | {Silver[3]} | {Silver[0]} |')
# print("-" *len(f"| Silver | {Silver[1]} | {Silver[2]} | {Silver[3]} | {Silver[0]} |"))

# print("-" *len(f"| Bronze | {Bronze[1]} | {Bronze[2]} | {Bronze[3]} | {Bronze[0]} |"))
# print(f'| Bronze | {Bronze[1]} | {Bronze[2]} | {Bronze[3]} | {Bronze[0]} |')
# print("-" *len(f"| Bronze | {Bronze[1]} | {Bronze[2]} | {Bronze[3]} | {Bronze[0]} |"))

# averageNumberOfBooksRead = totalNumberOfBooksRead / totalnumberofstudents

# print("-" *len(f'| Average Books | {averageNumberOfBooksRead} |'))
# print(f'| Average Books | {averageNumberOfBooksRead} |')
# print("-" *len(f'| Average Books | {averageNumberOfBooksRead} |'))

# print("-" *len(f'| Total Books read | {totalNumberOfBooksRead} |'))
# print(f'| Total Books read | {totalNumberOfBooksRead} |')
# print("-" *len(f'| Total Books read | {totalNumberOfBooksRead} |'))

# print(Gold)
# print(Silver)
# print(Bronze)

# print(totalNumberOfBooksRead)
# print(averageNumberOfBooksRead)