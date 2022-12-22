# import datetime
# import random


# def getBirthdays(numberOfBirthdays):
#     birthdays = []
#     for i in range(numberOfBirthdays):
#         startOfYear = datetime.date(1999, 1, 1)
#         randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
#         birthday = startOfYear + randomNumberOfDays
#         birthdays.append(birthday)
#     return birthdays


# def getMatch(birthdays):
#     if (birthdays) == len(set(birthdays)):
#         return None

#     for a, birthdayA in enumerate(birthdays):
#         for b, birthdayB in enumerate(birthdays[a + 1:]):
#             if birthdayA == birthdayB:
#                 return birthdayA


# print('Парадокс дней рождений!!')
# print('В группе из 23 человек вероятность дня рождения в один день равна 50%. А в группе из 70 человек 99.9%')
# print('Давай докажем это!')

# MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
#           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')


# while True:
#     print('Сколько дней мне сгенерить? (Максимум 100)')
#     response = input('> ')
#     if response.isdecimal() and (0 < int(response) <= 100):
#         numBDays = int(response)
#         break
# print()

# print('Вот', numBDays, 'дней рождений: ')
# birthdays = getBirthdays(numBDays)
# for i, birthday in enumerate(birthdays):
#     if i != 0:
#         print(', ', end='')
#     monthName = MONTHS[birthday.month - 1]
#     dateText = '{}{}'.format(monthName, birthday.day)
#     print(dateText, end='')
# print()
# print()

# match = getMatch(birthdays)

# print('В этой симуляции, ', end='')
# if match != None:
#     monthName = MONTHS[match.month - 1]
#     dateText = '{}{}'.format(monthName, match.day)
#     print('Несколько людей празднуют день рожденье в ', dateText)
# else:
#     print('Нет совпадений!Неужели парадокс обманул нас?')


# print('Генерирую', numBDays, 'случайных дней рождений 100_000 раз')
# input('Нажмите Enter чтобы начать...')

# print('Запускаю еще 100_000 симуляций')
# simMatch = 0
# for i in range(100_000):
#     if i % 10_000 == 0:
#         print(i, 'симуляций пройдено...')
#     birthdays = getBirthdays(numBDays)
#     if getMatch(birthdays) != None:
#         simMatch += 1
# print('100_000 симуляций созданый успешно')

# probability = round(simMatch / 100_000 * 100, 2)
# print('Из 100_000 симуляций', numBDays, 'людей')
# print('Совпадений по дням было', simMatch, 'раз')
# print('Это значит что у ', numBDays,
#       'людей шанс отмечать день рождение в один день состовляет', probability)
# print('Это шокирует! Не так ли?')

import random
import datetime


def getBirthDays(numberOfBirthDays):
    birthdays = []
    for i in range(numberOfBirthDays):
        startOfYear = datetime.date(1999, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA


print('Парадокс дней рождений!!')
print('В группе из 23 человек вероятность дня рождения в один день равна 50%. А в группе из 70 человек 99.9%')
print('Давай докажем это!')

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('Сколько мне сгенерить?')
    response = input('> ')
    if response.isdecimal() or (0 < int(response) <= 100):
        numBDays = int(response)
        break

print()

print('Вот столько дней', numBDays)
birthdays = getBirthDays(numBDays)

for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{}{}'.format(monthName, birthday.day)
    print(dateText, end='')

print()

match = getMatch(birthdays)

if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('У нескольких людей днюха в день', dateText)
else:
    print('Не повезло ребят')


print()

print('Запускаем 10_000 симуляций по группе в {} человек '.format(numBDays))
input('Нажми чтобы начать')

print('Запускаем симуляции Летс гоооооу')

simMatch = 0
for i in range(10_000):
    if i % 50 == 0:
        print(i, ' Симуляций прошло')
    birthdays = getBirthDays(numBDays)
    if getMatch(birthdays) != None:
        simMatch += 1

print('10_000 симуляций закончено')


probability = round(simMatch / 10000 * 100, 2)
print('Из 10_000 симуляций', numBDays, 'людей')
print('Совпадений по дням было', simMatch, 'раз')
print('Это значит что у ', numBDays,
      'людей шанс отмечать день рождение в один день состовляет', probability)
print('Это шокирует! Не так ли?')
