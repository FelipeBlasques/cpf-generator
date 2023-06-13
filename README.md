# CPF Generator

## What is CPF ?

CPF (Cadastro de Pessoas Físicas) is an identification number used in Brazil. It is a unique 11-digit number assigned to each Brazilian citizen, resident, and certain foreigners. The CPF serves as an essential document for various transactions, such as opening a bank account, obtaining credit, conducting business, and accessing government services.

The CPF consists of nine digits, followed by two verification digits. The first digit is used to validate the CPF number, and the second digit is used to validate the entire CPF number.

CPF numbers are issued by the Brazilian Federal Revenue Service and are associated with individual taxpayers. They help maintain records, track financial activities, and ensure compliance with tax and social security regulations.

## First Code
(firstdigit.py)

The first code aims to validate the first digit of a CPF number (Individual Taxpayer Registration)
Follow these steps:

First, it defines a list called 'MULTIPLIERS' that holds specific values used to multiply each digit of the CPF. This list represents the weights applied to each digit during the validation process.

Next, the code prompts the user to input a CPF number using the input function and stores it as a string in the variable cpf_input.

The string input is then converted to a list of integers called cpf using a list comprehension:

![image](https://github.com/FelipeBlasques/cpf-generator/assets/130731174/107ca991-6a8b-4993-b171-4724c8e92fb7)

To validate the first digit, the code performs the following steps:

a. It initializes an empty list called result to store the results of multiplying each digit of the CPF by its corresponding weight.

b. Using a for loop, the code iterates over each digit of the CPF and multiplies it by the corresponding multiplier from the MULTIPLIERS list. The results are then appended to the result list.

c. The code calculates the sum of all the elements in the result list using the sum function and stores it in the variable addc.

d. The variable addc is then multiplied by 10 and the modulo operator % is applied with a divisor of 11 to calculate the final value:

e. If the calculated final value is greater than 9, it is set to 0:

![image](https://github.com/FelipeBlasques/cpf-generator/assets/130731174/d3ab10cd-580d-424c-b433-4a15b399ea78)

Finally, the code prints the calculated value, representing the first digit of the CPF number:

![image](https://github.com/FelipeBlasques/cpf-generator/assets/130731174/b4950feb-bc9b-49a6-a2e0-bf9cdeb722ab)

Overall, the code takes user input for a CPF number, multiplies each digit by its corresponding weight, calculates a final value, and checks if it matches the first digit of the CPF number.

## Second Code
(seconddigit.py)

The second part of the code validates the first digit and second digit of the CPF number using similar logic as the first digit validation. It follows these steps:

a. The code defines a new list called 'SECOND_MULTIPLIERS' that holds specific values used to multiply each digit of the CPF for the second digit validation.

b. The code appends the previously calculated first digit to the cpf list to include it for the second digit validation.

c. Similar to the first digit validation, the code initializes an empty list called result to store the results of multiplying each digit of the CPF by its corresponding weight:

![image](https://github.com/FelipeBlasques/cpf-generator/assets/130731174/f29c2828-14ee-4053-bbdc-9adba277e7a3)

d. Using a for loop, the code iterates over each digit of the CPF, including the first digit, and multiplies it by the corresponding multiplier from the SECOND_MULTIPLIERS list. The results are then appended to the result list:

![image](https://github.com/FelipeBlasques/cpf-generator/assets/130731174/fa6bbc01-9935-4b9c-87d1-f75f171a99e2)

e. The code calculates the sum of all the elements in the result list using the sum function and stores it in the variable addc:

![image](https://github.com/FelipeBlasques/cpf-generator/assets/130731174/787bdb68-7eda-4a1a-9ab9-5df482daa16f)

f. The second digit is calculated by multiplying addc by 10 and applying the modulo operator % with a divisor of 11:

g. If the calculated second_digit value is greater than 9, it is set to 0.

h. Finally, the code prints the calculated value, representing the second digit of the CPF number:

![image](https://github.com/FelipeBlasques/cpf-generator/assets/130731174/79538f9c-88bb-4d44-be5d-edd895c9063f)

By following these steps, the code validates both the first and second digits of the CPF number based on the user input.
