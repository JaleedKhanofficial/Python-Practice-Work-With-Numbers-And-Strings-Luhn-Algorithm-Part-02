# Step 34
# Change the value of card_number such that 'INVALID!' is printed to the console.

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    print(total)
    
    return 0 == total % 10

def main():
    card_number = '4111-1111-4555-1145'              # step 34  // replace 5 to 2 to print output invalid
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):       
        print("VALID!")                                  
    else:                                                
        print("INVALID!")                           

main()


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial