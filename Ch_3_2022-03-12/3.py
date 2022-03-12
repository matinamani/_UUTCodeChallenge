caps = 0
a = ""
st1 = ""

number = input()
number = int(number)
while number > 0 :
    a = input()
    if a == "CAPS" :
        if caps == 1 :
            caps = 0
        else: 
            caps = 1
<<<<<<< HEAD
        number -= 1 # this line added to code
=======
        number -= 1 # this line added to code
>>>>>>> b881247aa2103fa9d3c94a9ea8cc4a4591eec474
        continue

    if caps == 1 :
        a = a.capitalize()
    st1 = st1 + a
    number = number - 1

print(st1)
