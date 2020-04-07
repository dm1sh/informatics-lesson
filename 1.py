dictionary = [chr(i) for i in range(ord('0'), ord('9')+1)] + \
    [chr(i) for i in range(ord('A'), ord('F')+1)]


def validation(string, ibase, tbase):
    for n in string:
        if not n in dictionary[:ibase] + [',', '.']:
            return False
    if ibase < 2 or ibase > 16 or tbase < 2 or tbase > 16:
        return False
    return True


def convert(string, ibase, tbase):
    if string == '0':
        return 0
    if ibase != 10:
        string = other_to_dec(string, ibase)
    if tbase == 10:
        return string
    string = float(string)
    integer = dec_to_other(int(string), tbase)
    decimal = string - int(string)
    if decimal:
        decimal = float_dec_with__to_other(decimal, tbase)
        return integer + ',' + decimal
    return integer


def other_to_dec(string, ibase):
    sum = 0
    amount = len(string.split('.')[0])-1
    for n in string:
        if n != '.':
            sum += int(dictionary.index(n)) * ibase**amount
            amount -= 1
    return sum


def dec_to_other(num, tbase):
    result = ''
    while num // tbase > 0:
        result += str(dictionary[int(num % tbase)])
        num //= tbase
    result += str(dictionary[int(num % tbase)])
    return result[::-1]


def float_dec_with__to_other(num, tbase):
    result = ''
    counter = 0
    while num - int(num) > 0 and counter < 8:
        result += str(dictionary[int(num * tbase)])
        num = num * tbase - int(num * tbase)
        counter += 1
    return result[:7]

# _____ MAIN PROGRAMM _____

input_number = input("Число: ").upper().replace(",", ".")
init_base = int(input("Основание исходной системы: "))
target_base = int(input("Основание конечной системы: "))

hasSign = False
if input_number[0] == '-':
    hasSign = True
    input_number = input_number[1:]

if not validation(input_number, init_base, target_base):
    print("Wrong input!")
    exit()

output = convert(input_number, init_base, target_base)

if hasSign:
    output = '-' + str(output)
print(output)
