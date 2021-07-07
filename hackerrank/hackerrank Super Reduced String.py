s = "aaabccddd"
index = 1
while index < len(s):
    if s[index] == s[index - 1]:
        s = s[:index -1] + s[index +1:]
        index = 0
    index += 1
if len(s) == 0:
    print("Empty String")
else:
    print(s)

