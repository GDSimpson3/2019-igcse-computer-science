# Q03c

# Write your code below this line
inputnumber = int(input("Enter a number from 1 to 50: "))

while not ((inputnumber >= 50) or (inputnumber <=1)):
    square = inputnumber * inputnumber
    cube = inputnumber * inputnumber * inputnumber
    print(f'Number: {inputnumber} \nSquare: {square} \nCube: {cube}')
    inputnumber = int(input("Enter a number from 1 to 50: "))
