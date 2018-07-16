# условия/conditions

if 1 :
    print(1)

a = 5

b = 6

if  a < 5:
    print('Меньше')

if a > 5:
    print('Больше')
elif a < 5: 
    print('меньше в elif')
else: 
    print('Равно')
a = 5

b = 6

if a > 5 and b < 4:
    print('54')


# loop/циклы 
a = 0
while a < 5:
    print('a')
    a += 1

# while True:
#     print('a')

a = 10
while a:
    print('a')
    a -= 1
    if a == 5:
        print('стоп')
        break

# for loop

for v in range(0, 5):
    print(v)

for v in range(0, 5, 2):
    print(v)

for char in 'string':
    print(char)
