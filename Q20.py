# Step 20
# Within the for loop, use the += operator to add the digit to the sum_of_odd_digits variable.

# Doing this your script throws a TypeError because you are trying to add a string to an integer, but don't worry, you will learn more about how to make it work in the next step.

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += digit      # step 20
        print(digit)
        
def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    verify_card_number(translated_card_number)

main()


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial