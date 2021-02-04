secret = list(input())
guess = list(input())
bulls = cows = 0
for i in range(len(secret)):
    if secret[i] == guess[i]:
        index = secret.index(guess[i])
        secret[index] = 'x'
        bulls += 1
    elif guess[i] in secret:
        index = secret.index(guess[i])
        secret[index] = 'x'
        cows += 1
print(str(bulls)+'A'+str(cows)+'B')
