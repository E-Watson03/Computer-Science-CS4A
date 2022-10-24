# 1
name = input("Greetings! How shall we call you?")
if name != "Lord" and "Lady":
    print("It shall be so,", name)
else:
    print("You may not be known by that name!")

# 2
spam_amount = int(input("How many slices of spam?"))
spam = "Spam "
spam_in_order = spam_amount * spam
reply = print("Egg with", spam_in_order, "coming up!")
print(reply)

# 3
import re


def validate():
    while True:
        password = input("Enter a password: ")
        if len(password) > 7:
            print("Incorrect! You may try again.")
        elif re.search('[0-9]', password) is True:
            print("Incorrect! You may try again.")
        elif re.search('[A-Z]', password) is True:
            print("Incorrect! You may try again.")
        else:
            password = input("parrot")
            print('Correct! You may enter.')
            break


validate()
 #or
password = print(input("Enter a password: "))
while True:
    if password != "parrot":
        print("Incorrect! You may try again.")
        print(input("Enter a password: "))
    else:
        var = password == "parrot"
        print('Correct! You may enter.')
        break















# 3


if choice == 1:
    if quantity <= apples:
        for x in range(quantity):
            print(' \nBEEEEEEEEEP')
            apples = apples - 1
            total = total + 1
    else:
        print('Uh oh we do not have enough. We only have', apples)

elif choice == 2:
    if quantity <= bananas:
        for x in range(quantity):
            print(' \nBEEEEEEEEEP')
            bananas = bananas - 1
            total = total + 1
    else:
        print('\nUh oh we do not have enough. We only have', bananas)
elif choice == 3:
    if quantity <= coke:
        for x in range(quantity):
            print('\nBEEEEEEEEEP')
            coke = coke - 1
            total = total + 5
    else:
        print('\nUh oh we do not have enough. We only have', coke)
elif choice == 4:
    if quantity <= pepsi:
        for x in range(quantity):
            print('\nBEEEEEEEEEP')
            pepsi = pepsi - 1
            total = total + 3
    else:
        print('\nUh oh we do not have enough. We only have', pepsi)
elif choice == 5:
    if quantity <= fanta:
        for x in range(quantity):
            print('B\nEEEEEEEEEP')
            fanta = fanta - 1
            total = total + 2
    else:
        print('\nUh oh we do not have enough. We only have', fanta)
elif choice == 6:
    if quantity <= kiwis:
        for x in range(quantity):
            print('\nBEEEEEEEEEP')
            kiwis = kiwis - 1
            total = total + 4
    else:
        print('\nUh oh we do not have enough. We only have', kiwis)
elif choice == 7:
    if quantity <= bread:
        for x in range(quantity):
            print('\nBEEEEEEEEEP')
            bread = bread - 1
            total = total + 1
    else:
        print('\nUh oh we do not have enough. We only have', bread)
elif choice == 8:
    if quantity <= eggs:
        for x in range(quantity):
            print('\nBEEEEEEEEEP')
            eggs = eggs - 1
            total = total + 2
    else:
        print('\nUh oh we do not have enough. We only have', eggs)
elif choice == 9:
    if quantity <= butter:
        for x in range(quantity):
            print('\nBEEEEEEEEEP')
            butter = butter - 1
            total = total + 2
    else:
        print('\nUh oh we do not have enough. We only have', butter)

if choice == 1:
    print('\nNow, there are only', apples, 'apples left in the store')

elif choice == 2:
    print('\nNow, there are only', bananas, 'bananas left in the store')

elif choice == 3:
    print('\nNow, there are only', coke, 'cans of Coke leftin the store')

elif choice == 4:
    print('\nNow, there are only', pepsi, 'cans of pepsi left in the store')

elif choice == 5:
    print('\nNow, there are only', fanta, 'bottles of fanta left in the store')

elif choice == 6:
    print('\nNow, there are only', kiwis, 'kiwis left in the store')

elif choice == 7:
    print('\nNow, there are only', bread, 'loafs of bread left in the store')

elif choice == 8:
    print('\nNow, there are only', eggs, 'eggs left in the store')

elif choice == 9:
    print('\nNow, there are only', butter, 'tubs of butter left in the store')

print('Your current total is $', total)
time.sleep(5)

decision = int(input('\nWhat would you like to do now? \n 1 - Purchase another item \n 2 - Checkout \n 1 or 2? '))
time.sleep(1)
if decision == 1:
    print('Sure!')
    x = 0
elif decision == 2:
    print('Oh well...checkout it is!')
    x = 1

time.sleep(2)
if total > 30 and total < 100:
    print(
        '\nGOOD NEWS! It seems as though you have purchased goods for over $30 which means you will get $5 off your bill.')
    total = total - 5
    print('\nYour discounted total is now', total)
elif total > 100:
    print('\nOH MY OH MY. You have bought a lot of stuff and for that you will get a $10 discount on your shopping')
    total = total - 10
    print('\nYour discounted total is now', total)

payment_method = int(input(
    '\nHow would you like to pay for your shopping? \nCard  (1) \nCash. (2)\nType the number that corresponds with your preffered payment option.'))

if payment_method == 1:
    print('Sure, card')
    time.sleep(2)
    print('Please present your card to the machnine and follow instructions on the screen')
    time.sleep(2)
    print('\nBEEEEEEEEEEEEEEP')
    time.sleep(2)
    print('Payment successful! A total of', total,
          'has been deducted from your bank account Thank you for shopping at Co-Op!')
elif payment_method == 2:
    print('Sure, cash')
    time.sleep(2)
    print('Please insert your cash into the machnine and follow instructions on the screen')
    time.sleep(2)
    print('\nBEEEEEEEEEEEEEEP')
    time.sleep(2)
    print('Payment successful! Thank you for shopping at Co-Op')
