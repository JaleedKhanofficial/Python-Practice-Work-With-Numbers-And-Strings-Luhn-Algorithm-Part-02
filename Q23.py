# Step 23
# Create a variable even_digits and assign it the even digits of the reversed card number.

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    print(sum_of_odd_digits)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]                #step 23

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    verify_card_number(translated_card_number)

main()


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial