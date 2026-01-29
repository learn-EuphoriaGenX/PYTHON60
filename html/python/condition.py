# age = 1
# if age > 18:
#     print("you can drive")
# elif age == 18:
#     print("Come to our office")
# else:
#     print("you can't")

num = 56
if num > 500:
    if num > 750:
        print("Num is gt 500 and 750")
    else:
        print("Num is gt 500 only")
elif num > 100:
    if num > 250:
        print("Num is gt 100 and 250")
    else:
        print("Num is gt 100 only")
else:
    print("Num is lt 100")


# Fine Calculator
ins = False
hel = False
lic = False

fine = 0
if not ins: fine += 500
if not hel: fine += 500
if not lic: fine += 500
# your code

print("Fine is rs:", fine)

