import cs50

# prompt user for cardnumber
card = cs50.get_string("enter card number: ")


cardNumber = []
sum_one = 0
sum_two = 0
# convert card numbers from string to array
for i in range(len(card)):
    j = int(card[i])
    cardNumber.append(j)

# add every other value together strarting from the last value
for i in range(len(cardNumber) - 1, 0 or -1, -2):
    sum_one += cardNumber[i]
# apply the formula to every other number    
for i in range(len(cardNumber) - 2, 0 or -1, -2):
    p = cardNumber[i] * 2
    # if the number is a double digit then split it by converting into a string and then adding by convering back to and int
    if p > 9:
        p = str(p)
        one = p[0]
        two = p[1]
        one = int(one)
        two = int(two)
        p = one + two
    
    sum_two += p    
 

# add up the calculation
total = sum_one + sum_two

# convert total to string so we can get the last number
total = str(total)

# get the last of the string
valid = total[len(total) - 1]

# convert it back to an int 
valid = int(valid)

# if the last is not 0 then the card is not valid
if valid != 0:
    print("INVALID")
else:
    # check to see if it's a amex
    if len(card) == 15:
        if cardNumber[0] == 3 and cardNumber[1] == 4 or cardNumber[1] == 7:
            print("AMEX")
    # check to see if it's a master card  or visa
    elif len(card) == 16:
        if cardNumber[0] == 5 and cardNumber[1] == 1 or cardNumber[1] == 2 or cardNumber[1] == 3 or cardNumber[1] == 4 or cardNumber[1] == 5:
            print("MASTERCARD")
        if cardNumber[0] == 4:
            print("VISA")
    elif len(card) == 13:
        if cardNumber[0] == 4:
            print("VISA")
    # or else the card is invalid        
    else:
        print("INVALID")
            