# Step 19
# Use a for loop to iterate over each digit in the odd_digits list. Move your print call from the previous step into the for loop, and change it to print each digit.

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    print(odd_digits)

    for digit in odd_digits:    # step 19
        print(digit)            # step 19

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    verify_card_number(translated_card_number)

main()


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial