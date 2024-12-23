# Step 33
# Adjust the verify_card_number call such that if it returns True, print 'VALID!' to the console. Otherwise, print 'INVALID!'.


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
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):       # step 33
        print("VALID!")                                  # step 33
    else:                                                # step 33
        print("INVALID!")                                # step 33

main()


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial