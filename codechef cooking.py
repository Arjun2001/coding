test = int(input())
while(test):
    test-=1
    n = int(input())
    a = input()
    if n%2 == 0:
        print("Bob wins")
    elif n%2 != 0 and a[0] == 'R':
        print("Alice wins")
    else:
        print("Bob wins")
