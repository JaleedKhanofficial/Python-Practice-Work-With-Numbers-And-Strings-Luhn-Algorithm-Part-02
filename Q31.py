# Step 31
# Below the second for loop of the verify_card_number function, create a variable named total, and assign it the value of the sum of the odd and even digits. Print total to the console.

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

        sum_of_even_digits += number
        if number >= 10:
            number = (number // 10) + (number % 10)
    
    total = sum_of_odd_digits + sum_of_even_digits               #step 30
    print(total)                                                 #step 30
            
        
def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    verify_card_number(translated_card_number)

main()


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial