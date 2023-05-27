import random

letters = "abcdefghijklmnopqrstuvwxyz"
capitalLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
numbers = "123456789"
symbols = "@#$%^*&*()!"

forPass = letters + capitalLetters + symbols + numbers

LenghtPass = 12

password = "".join(random.sample(forPass, LenghtPass))

print(password)