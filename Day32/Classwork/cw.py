#1
string = "Hiiiiiii!"

lower_case = string.lower()
print("დაპატარავებული:", lower_case)

upper_case = string.upper()
print("გადიდებული:", upper_case)

capitalized = string.capitalize()
print("პირველი ასო გადიდებული:", capitalized)

replaced = string.replace('i', 'h')
print("შეცვლილი:", replaced)





#2
my_list = ['hello', 'HIII', 'python', 'programming', 'watermelon']

print(my_list[0].upper())  # HELLO

print(my_list[1].lower())  # hiii

print(my_list[2].find('n'))  # 5

print(my_list[3].replace('g', 'k'))  # prokramming

print(my_list[4].title())  # Watermelon

