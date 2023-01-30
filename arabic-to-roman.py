def roman_func(num):
    num = int(num)  # Converts input to integer
    symbols = []  # List of arabic numbers in simple form
    for i in range(len(str(num))):
        symbols.append(int(str(num)[i]) * 10 ** (len(str(num)) - i - 1))
    roman_symbols = []  # List of converted arabic numbers to roman
    for e in symbols:
        if e % 1000 == 0 and e != 0:
            roman_symbols.append((e // 1000) * 'M')
        elif e == 900:
            roman_symbols.append('CM')
        elif 900 > e >= 500:
            roman_symbols.append('D' + ((e - 500) // 100) * 'C')
        elif e == 400:
            roman_symbols.append('CD')
        elif 400 > e >= 100:
            roman_symbols.append((e // 100) * 'C')
        elif e == 90:
            roman_symbols.append('XC')
        elif 90 > e >= 50:
            roman_symbols.append('L' + ((e - 50) // 10) * 'X')
        elif e == 40:
            roman_symbols.append('XL')
        elif 40 > e >= 10:
            roman_symbols.append((e // 10) * 'X')
        elif e == 9:
            roman_symbols.append('IX')
        elif 9 > e >= 5:
            roman_symbols.append('V' + (e - 5) * 'I')
        elif e == 4:
            roman_symbols.append('IV')
        elif e == 1 or e == 2 or e == 3:
            roman_symbols.append(e * 'I')
    roman_num = ''
    for e in roman_symbols:  # Creates word with elements from roman_symbols list
        roman_num += e
    print(roman_num)  # Prints roman number


roman_func(12345)
