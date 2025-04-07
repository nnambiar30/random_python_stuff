def print_window(lines):

    width = 38                   
    inner_width = width - 4      
    border = "*" * width

    print(border)
    for line in lines:
        print("* " + line.ljust(inner_width) + " *")
    print(border)

def int_to_roman_steps(year):
    steps = [] 
    roman_numeral = ""
    remaining = year
    
    steps.append((roman_numeral, remaining))
    
    while remaining >= 1000:
        roman_numeral += "M"
        remaining -= 1000
        steps.append((roman_numeral, remaining))
    
    if remaining >= 900:
        roman_numeral += "CM"
        remaining -= 900
        steps.append((roman_numeral, remaining))
    elif remaining >= 500:
        roman_numeral += "D"
        remaining -= 500
        steps.append((roman_numeral, remaining))
    elif remaining >= 400:
        roman_numeral += "CD"
        remaining -= 400
        steps.append((roman_numeral, remaining))
    
    while remaining >= 100:
        roman_numeral += "C"
        remaining -= 100
        steps.append((roman_numeral, remaining))
    
    if remaining >= 90:
        roman_numeral += "XC"
        remaining -= 90
        steps.append((roman_numeral, remaining))
    elif remaining >= 50:
        roman_numeral += "L"
        remaining -= 50
        steps.append((roman_numeral, remaining))
    elif remaining >= 40:
        roman_numeral += "XL"
        remaining -= 40
        steps.append((roman_numeral, remaining))
    
    while remaining >= 10:
        roman_numeral += "X"
        remaining -= 10
        steps.append((roman_numeral, remaining))
    
    if remaining == 9:
        roman_numeral += "IX"
        remaining -= 9
        steps.append((roman_numeral, remaining))
    elif remaining >= 5:
        roman_numeral += "V"
        remaining -= 5
        steps.append((roman_numeral, remaining))
    elif remaining == 4:
        roman_numeral += "IV"
        remaining -= 4
        steps.append((roman_numeral, remaining))
    
    while remaining >= 1:
        roman_numeral += "I"
        remaining -= 1
        steps.append((roman_numeral, remaining))
    
    return steps

def main():
    initial_window = [
        "Enter a year [1 to 3000]:",
        "",
        "",
        "",
        "",
        "",
        ""
    ]
    print_window(initial_window)


    year_input = input("Enter a year [1 to 3000]: ")
    year = int(year_input)
    if year < 1 or year > 3000:
        print("Year must be between 1 and 3000.")
        return
    
    final_window = [
        "Enter a year [1 to 3000]:",
        str(year),
        "",
        "",
        ""
        ""
    ]

    print_window(final_window)
    steps = int_to_roman_steps(year)
    
    print("\nConversion Steps:")
    for roman, rem in steps:
        if rem != 0:
            print(f'"{roman}"\t{rem}')
        else:
            print(f'"{roman}"')

if __name__ == '__main__':
    main()
