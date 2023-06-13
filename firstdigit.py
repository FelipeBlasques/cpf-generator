# validating the first digit of the cpf

MULTIPLIERS = [10, 9, 8, 7, 6, 5, 4, 3, 2]

cpf_input = input("Enter CPF (numbers only): ")
cpf = [int(digit) for digit in cpf_input]

result = []

for i in range(len(cpf)):
    result.append(cpf[i] * MULTIPLIERS[i])

addc = sum(result)

digit = addc * 10
digit = digit % 11

if digit > 9:
    digit = 0

print(f"O primeiro dígito do CPF é: {digit}")
