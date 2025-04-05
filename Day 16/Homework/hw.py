# Debugging = შეცდომის პოვნა და გასწორება
x = "5"
y = 2
# შეცდომა: სტრინგი + რიცხვი
x = int(x) 
print(x + y)  # 7


# input() ყოველთვის აბრუნებს სტრინგს (str)
x = input("number: ")
print(type(x))  # ბეჭდავს <class 'str'>


# ცვლადის შექმნა: სახელი = მნიშვნელობა
age = 25  # age ინახავს 25-ს, ცვლადის ტიპი არის int

print(age)        # 25
print(type(age))  # <class 'int'>


# Casting არის ტიპების გადაყვანა, str → int

x = "5"         # სტრინგია
y = int(x)      # ვაკეთებთ casting → int

print(y + 1)    # 6

