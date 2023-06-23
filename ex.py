number = [1, 24, 26, 15, 12, 14, 19, 10]

ask = int(input("Enter the digit: "))

print("number you choose is", number[ask])


if number[ask] % 2 == 0:
    print("number is even")
else:
    print("Number is odd")

if number[ask] % 4 == 0:
    print("its fully divisible by 4.")
else:
    print("its not divisible by 4.")

if number[2] < number[3]:
    print("yes it smaller")
else:
    print(number[2], "is not less than", number[3])

maxvalue = max(number)
print ("maximum value from the list above is", maxvalue)


new = [1, 2, 5, 6, 12]
ask2 = int(input("Enter the number you want to add to our list: "))
new.append(ask2)
print("thank you for adding your number.Here is new list, with your number at the end", new )
maximum = max(new)
print("also the biggest number is", maximum)

