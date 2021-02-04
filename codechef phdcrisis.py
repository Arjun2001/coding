n = int(input())
for i in range(n):
    a = input()
    if a == 'P=NP':
        print('skipped')
    else:
        a = a.split('+')
        print(int(a[0])+int(a[1]))
