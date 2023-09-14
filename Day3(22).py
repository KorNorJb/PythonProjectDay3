# SIMPLE PASSWORD GENERATOR
import string # all possible symbols
import random # random choice
def generatePas(lenght, lowercase, uppercase, numbers, symbols): # function for generate custom password
    if (lowercase == 1 and uppercase == 2 and numbers == 2 and symbols == 2):
        characters = string.ascii_lowercase
        passw = ''.join(random.choice(characters) for _ in range(lenght))
        print(f"Ваш сгенерированный пароль: {passw}")
    elif (lowercase == 1 and uppercase == 1 and numbers == 2 and symbols == 2):
        characters = string.ascii_letters
        passw = ''.join(random.choice(characters) for _ in range(lenght))
        print(f"Ваш сгенерированный пароль: {passw}")
    elif (lowercase == 1 and uppercase == 1 and numbers == 1 and symbols == 2):
        characters = string.ascii_letters + string.digits
        passw = ''.join(random.choice(characters) for _ in range(lenght))
        print(f"Ваш сгенерированный пароль: {passw}")
    elif (lowercase == 1 and uppercase == 1 and numbers == 1 and symbols == 1):
        characters = string.ascii_letters + string.digits + string.punctuation
        passw = ''.join(random.choice(characters) for _ in range(lenght))
        print(f"Ваш сгенерированный пароль: {passw}")
    elif(lowercase == 2 and uppercase == 2 and numbers == 2 and symbols == 2):
          print("Вы должны выбрать хотя бы один пункт. Из чего делать пароль то?:(")
def inputs(): # just inputs:)
    lenght = int(input("Введите длину пароля: "))
    lowercase = int(input("Добавить буквы нижнего регистра? \n1)Да \n2)Нет \n"))
    uppercase = int(input("Добавить буквы верхнего регистра? \n1)Да \n2)Нет \n"))
    numbers = int(input("Добавить цифры? \n1)Да \n2)Нет \n"))
    symbols = int(input("Добавить символы? \n1)Да \n2)Нет \n"))
    generated_pass = generatePas(lenght, lowercase, uppercase, numbers, symbols)
inputs()
