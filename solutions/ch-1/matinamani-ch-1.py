key = input()
test = input().split()

dict = {}
flag = True

for i in range(len(key) - 1):
    if key[i] in dict.keys():
        if not dict[key[i]] == test[i]:
            flag = False
            break
    else:
        dict.update({key[i]: test[i]})

print(flag)
