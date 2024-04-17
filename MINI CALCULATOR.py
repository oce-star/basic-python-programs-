print('_______________MINI CALCULATOR_______________')

num1 = float(input('Enter your first value :'))
num2 = float(input('Enter your second value :'))
print(" Tap 1 for addition \n Tap 2 for substraction \n Tap 3 for multiplication \n Tap 4 for division")

choice = int(input( 'Enetr your choice between 1 to 4 :'))
if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    print(num1 / num2)
else:
    print('The given input is invalid :(')