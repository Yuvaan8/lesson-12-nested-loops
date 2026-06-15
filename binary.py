num = float(input('Enter a decimal number:'))
binary = ''
while num > 0:
    for i in range(1):
        remainder = num % 2
        binary = str(remainder)+ binary
        num = num // 2
print('Binary number =', binary)