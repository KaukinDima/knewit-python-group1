questions = [
    "Как дела?",
    "Че нового?",
]
anwsers = [
    "f",
    "f",
]
i = 0
while True:
    if i > len(questions)-1:
        break
    anwser = input("Добрый день" + questions[i])
    print('\n')
    if not len(questions) == len(anwsers):
        print('Массивы должны быть одинаковы')
        break
    if anwser == anwsers[i]:
        i += 1
        print("Ура,верно!", '\n')
    elif anwser == 'q':
        break
    else:
        print("Плохо")
        print('\n')


for v in zip(questions, anwsers):
    if input(v[0]) == v[1]:
        print('УРа')
