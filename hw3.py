import random

def Viselica():
 print ('ВРЕМЯ ИГРАТЬ')

wordlist =['яблоко', 'апельсин', 'груша', 'пицца', 'сыр', 'бургер', 'каша', 'Лимон']
secret = random.choice(wordlist)
guesses = 'яагпсбкл'
turns = 5

while turns > 0:
     missed = 0
     for letter in secret:
         if letter in guesses:
             print (letter,end=' ')
         else:
           print ('_',end=' ')
           missed= missed + 1

     print

     if missed == 0:
         print ('\nТы выиграл!')
         break

     guess = input('\nугадай еду: ')
     guesses += guess

     if guess not in secret:
         turns = turns -1
         print ('\nNope.')
         print ('\n',turns, 'больше ходов')
         if turns < 5: print ('\n  |  ')
         if turns < 4: print ('  O  ')
         if turns < 3: print (' /|\ ')
         if turns < 2: print ('  |  ')
         if turns < 1: print (' / \ ')
         if turns == 0:
             print ('\n\nОтвет', secret)

playagain = 'да'
while playagain == 'да':
    Viselica()
    print('Ты хочешь снова сыграть? (да или нет)')
    playagain = input()
