# Step 14
# Just as the step is optional, a start at 0 and an end at the end of the slice are optional:
# Example Code
# my_string = 'camperbot'
# camperbot = my_string[::]
# Assign the reverse of the full card_number string to the card_number_reversed variable.

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]                # step 14
    print(card_number_reversed)
    
def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    print(translated_card_number)

    verify_card_number(translated_card_number)

main()


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial