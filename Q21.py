# Step 21
# Currently, your script throws a TypeError because you are trying to add a string to an integer. You can fix this by converting the digit variable to an integer before adding it to sum_of_odd_digits, using the built-in int function:

# Example Code
# my_string = '123'
# my_int = int(my_string)
# Convert the digit variable to an integer before adding it to sum_of_odd_digits. Then, move the print call to the end of the verify_card_number function to print the value of sum_of_odd_digits.

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)             #step 21
    print(sum_of_odd_digits)                        #step 21
        
def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    verify_card_number(translated_card_number)

main()


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial