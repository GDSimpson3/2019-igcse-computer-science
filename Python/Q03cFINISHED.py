# Q03c

# Write your code below this line
inputnumber = int(input("Enter a number from 1 to 50: "))

while  inputnumber <= 50 and inputnumber >=1:
    print(f'Number: {inputnumber} \nSquare: {inputnumber * inputnumber} \nCube: {inputnumber * inputnumber * inputnumber}')
    inputnumber = int(input("Enter a number from 1 to 50: "))
