import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''
    Я загадал число из {} цифр без повторений.
    Попробуй угадать его.
    Вот подсказки:
    Верно - цифра стоит на своем месте
    Близко - цифра стоит на чужом месте
    Мимо - Таких цифр я не загадывал

    Например:
    Число 834 - твой вариант 138.
    Я отвечаю - Близко, Верно
    Ответы в алфавитном порядке
    '''.format(NUM_DIGITS))

    while True:
        secretNum = getSecretNum()
        print('Я придумал число')
        print('У тебя {} попытки угадать'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Попытка №{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('У тебя закончились попытки')
        print('Хочешь сыграть еще раз? (Да или Нет)')
        if not input('> ').lower().startswith('д'):
            break
    print('Спасибо за игру!')


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return 'Ты Лучший'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Верно')
        elif guess[i] in secretNum:
            clues.append('Близко')
    if len(clues) == 0:
        return 'Мимо!'
    else:
        clues.sort()
        return ' 8 '.join(clues)


if __name__ == '__main__':
    main()

# import random

# NUM_DIGITS = 3
# MAX_GUESSES = 10


# def main():
#     print('''
#     Я загадал число из {} цифр без повторений.
#     Попробуй угадать его.
#     Вот подсказки:
#     Верно - цифра стоит на своем месте
#     Близко - цифра стоит на чужом месте
#     Мимо - Таких цифр я не загадывал

#     Например:
#     Число 834 - твой вариант 138.
#     Я отвечаю - Близко, Верно
#     Ответы в алфавитном порядке
#     '''.format(NUM_DIGITS))

#     while True:
#         secretNum = getRandomNumber()
#         print('Я загадал число')
#         print('У тебя есть {} попыток'.format(MAX_GUESSES))

#         guessNumber = 1
#         while guessNumber <= MAX_GUESSES:
#             guess = ''
#             if len(guess) != NUM_DIGITS or not guess.isdecimal():
#                 print('Попытка номер {}: '.format(guessNumber))
#                 guess = input('> ')

#             clues = getClues(guess, secretNum)
#             print(clues)
#             guessNumber += 1

#             if guess == secretNum:
#                 print('Ты победил!')
#                 break
#             if guessNumber > MAX_GUESSES:
#                 print('Ты проиграл!')
#                 print('Ответ был {}'.format(secretNum))
#         print('Ты хочешь сыграть еще? Напиши ДА или НЕТ')
#         if not input('> ').lower().startswith('д'):
#             break
#     print('Спасибо за игру!')


# def getRandomNumber():
#     numbers = list('0123456789')
#     random.shuffle(numbers)

#     secretNum = ''
#     for i in range(NUM_DIGITS):
#         secretNum += str(numbers[i])

#     return secretNum


# def getClues(guess, secretNum):
#     clues = []

#     for i in range(len(guess)):
#         if guess[i] == secretNum[i]:
#             clues.append('VERNO')
#         elif guess[i] in secretNum:
#             clues.append('BLIZKO')
#     if len(clues) == 0:
#         return 'MIMO'
#     else:
#         clues.sort()
#         return ' and '.join(clues)


# if __name__ == '__main__':
#     main()
