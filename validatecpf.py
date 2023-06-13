FIRST_MULTIPLIERS = [10, 9, 8, 7, 6, 5, 4, 3, 2]
SECOND_MULTIPLIERS = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

cpf_input = input("Enter CPF (11 digits / numbers only): ")
cpf = [int(digit) for digit in cpf_input]

cpf_validator = cpf.copy()

del cpf_validator[10]
del cpf_validator[9]

def validate_cpf(cpf, multipliers):
    result = []
    for i in range(len(cpf)):
        result.append(cpf[i] * multipliers[i])

    addc = sum(result)

    digit = (addc * 10) % 11
    if digit > 9:
        digit = 0

    return digit

first_digit = validate_cpf(cpf_validator, FIRST_MULTIPLIERS)
cpf_validator.append(first_digit)
second_digit = validate_cpf(cpf_validator, SECOND_MULTIPLIERS)
cpf_validator.append(second_digit)

if cpf == cpf_validator:
    print(f'The CPF is valid')
else:
    print(f'The CPF is invalid')


