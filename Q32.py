# Step 32
# Return the result of comparing 0 to total modulo 10.

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
    
    return 0 == total % 10                  # step 32

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    verify_card_number(translated_card_number)

main()


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial