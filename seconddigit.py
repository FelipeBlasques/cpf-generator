# validating the first and the second digit of the cpf

FIRST_MULTIPLIERS = [10, 9, 8, 7, 6, 5, 4, 3, 2]

cpf_input = input('Enter CPF (numbers only): ')
cpf = [int(first_digit) for first_digit in cpf_input]

result = []

for i in range(len(cpf)):
    result.append(cpf[i] * FIRST_MULTIPLIERS[i])

addc = sum(result)

first_digit = addc * 10
first_digit = first_digit % 11

if first_digit > 9:
    first_digit = 0

print(f'The first digit of the CPF is: {first_digit}')

SECOND_MULTIPLIERS = [11,10, 9, 8, 7, 6, 5, 4, 3, 2]

cpf.append(first_digit)

result = []

for i in range(len(cpf)):
    result.append(cpf[i] * SECOND_MULTIPLIERS[i])

addc = sum(result)

second_digit = addc * 10
second_digit = second_digit % 11

if second_digit > 9:
    second_digit = 0

print(f'The second digit of the CPF is: {second_digit}')

