import random

print('Hello, What is your name?')
name = input()
print('Well, ' + name + ', Now give me the number!')
num = int(input())

while(num != 1):
    if num % 2 == 1:
        num = num // 2
        print('Number is ' + str(num) + ' now!')
    elif num % 2 == 0:
        num = 3 * num + 1
        print('Number is ' + str(num) + ' now!')

print('Finally we reached 1!')
