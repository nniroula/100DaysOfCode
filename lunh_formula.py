#!/Users/nabinniroula/anaconda3/bin/python

""" Given a number determine whether or not it is valid per the Luhn formula.

The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers, such as credit 
card numbers and Canadian Social Insurance Numbers.

Strings of length 1 or less are not valid. Spaces are allowed in the input, but they should be stripped before 
checking. All other non-digit characters are disallowed.

>>> given number is 4539 3195 0343 6467

If doubling the number results in a number greater than 9 then subtract 9 from the product. The results of our doubling:
8569 6195 0383 3437

Then sum all of the digits:
8+5+6+9+6+1+9+5+0+3+8+3+3+4+3+7 = 80

If the sum is evenly divisible by 10, then the number is valid. This number is valid!

"""
class Card_Number_Validation:
    def __init__(self, card_number):
        self.card_number = card_number.replace(" ", "") # replace white space with nothing

    def valid(self):
        if len(self.card_number) <= 1:
            return "Invalid"
        # remove the white spaces 
        # new_card_num = self.card_number.replace(" ", "")

        # chekc for all non-digit numbers
        if not self.card_number.isdigit():
            return False
        
    
