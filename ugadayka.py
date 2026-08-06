from random import*
n=randint(1,100)
print('Добро пожаловать в числовую угадайку')
print('До какого числа возьмём отрезок?')
def stop():
    print('Введите целое число, большее единицы')
    n=input()
    while True:
        if n.isdigit() and n.count('.')==0 and int(n)>1:
            return int(n)
        else:
            print('Введите целое число, большее единицы')
            continue
def is_valid():
    while True:
        s=input()
        if s.isdigit() and s.count('.')==0 and int(s)>=1 and int(s)<=st:
            return int(s)
        else:
            print(f'А может быть все-таки введем целое число от 1 до {st}?')
def fin():
    while True:
        s=input()
        if s=='да' or s=='нет':
            return s
        else:
            print('Введите "да" или "нет"')
            continue
final=''
while final!='нет':
    st=stop()
    print(f'Введите число от 1 до {st}')
    s=is_valid()
    f=0
    cnt=0
    while f==0:
        if s>n:
            print('Ваше число больше загаданного, попробуйте еще разок')
            cnt+=1
            s=is_valid()
        if s<n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            cnt+=1
            s=is_valid()
        if n==s:
            cnt += 1
            print(f'Вы угадали, поздравляем! Вам понадобилось {cnt} попыток')
            f=1
            print('Хотите сыграть ещё? Напишите только да или нет')
            final=fin()
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')


