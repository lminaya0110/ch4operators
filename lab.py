'''
Part 1: Write a Python program that produces the following outputs:
100 times 2.71828 = 271.828
100 divided by 2.71828 = 36.787968862663156
2.71828 raised to the power of 3.14159 to 6 decimals is 23.140582
100 plus 200 THEN multiplied by 2.71828 is 815.484
100 plus 200 THEN divided by 2.71828 plus 3.14159 is 51.1956749893769
100 divided by 2.71828 plus 200 divided by 3.14159 is 100.44999987243847
Is 100 less than 200? True
Is 100 greater than 2.71828 OR 3.14159 equal to 200? True
Is 100 cubed greater than 200 squared? True
Is true greater than false? True
The letter "f" in "abcdef" ? True
The letter "K" is not in "abcdef" ? True
100 equals 100.0 ? True
100 is the same object as 100.0 ? False

'''

num1 = 100
num2 = 2.71828
num3 = 200
pi = 3.14159
q1 = 100 < 200
q2 = 100 > num2 or pi == 200
letters = "abcdef"


print(f'{num1} times {num2} = {num1 * num2}')
print(f'{num1} divided by {num2} = {num1 / num2}')
print(f'{num1} raised to the power of {pi} to 6 decimals is {num2**pi}')
print(f'{num1} plus {num3} THEN multiplied by {num2} is {float((num1 + num3)) * num2}')
print(f'{num1} plus {num3} THEN divided by {num2} plus {pi} is {float(num1 + num3) / num2 + pi }')
print(f'{num1} divided by {num2} plus {num3} divided by {pi} is {num1 / num2 + num3 / pi}')
print(f'Is 100 less than 200? {q1}')
print(f'Is 100 greater than 2.71828 OR 3.14159 equal to 200? {q2}')
print(f'Is 100 cubed greater than 200 squared? {100**3 > 200**2}')
print(f'Is Is true greater than false? {True > False}')

if "f" in letters: 
    print(f'The letter "f" in "abcdef" ?  True')
    
if "K" is not letters:
    print(f'The letter "K" is not in "abcdef" ? True')

print(f'100 equals 100.0 ? {100 == 100.0}')
print(f'100 is the same object as 100.0 ? {id(100) == id(100.0)}')



'''
Part 2: Write a Python program that converts Celsius to Fahrenheit by using the
following formula:
Faren = ( ( 9 * Cels) / 5 ) + 32
Prompt the user for a Celsius temperature. Remember that user input is returned
as a character string and must be converted!
The program may be done in two lines
'''

celsius = float(input("Enter the temp in Celsius to be converted to Farenheit: "))
print(f"The temperature is {( ( 9 * celsius) / 5 ) + 32}")