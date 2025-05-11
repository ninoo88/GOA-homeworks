number=int(input("enter your age: "))
if number >= 18:
    print("you're an adult")

elif number == 15:
    print("You're a teenager")

else:
    print("You're a child")



name=(input ("enter a name: "))
if name == "ალექსანდრე":
    print("შენ ხარ მენტორი")

elif name == "გურამი":
    print("შენ არ ხარ მენტორი")

else:
    print("შენ ხარ მოსწავლე")



num = int(input("Enter a number: "))
numb = int(input("Enter another number: "))
if numb > num:
    print("Level up!")
elif num > numb:
    print("Level down!")
else:
    print("Level updown!")


#if: შეამოწმებს პირველ პირობას
#elif: შეამოწმებს დამატებით პირობას, თუ პირველი არ შესრულდა
#else: შეასრულებს კოდს, თუ არცერთი პირობა არ შესრულდა