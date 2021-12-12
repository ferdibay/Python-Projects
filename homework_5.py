
# yıldızlarla şekil oluşturma.. ve faktöryel yazma..



for i in range(12,0,-1):
    if i<=6:
        print("*"*i)
        i-=1

print("--------------------")

for i in range(12,0,-1):
    if i<=6:
        print("*"*i)

    else:
        print("*"*(i-6))


print("--------------------")


a=5
for i in range(12):
    if i<=6:
        print("*"*i)
    else:
        print("*"*a)
        a-=1


print("--------------------")


number=int(input("Sayı giriniz:"))
def factorial(number):

    if number==0 or number==1:
        return 1
    else:
        return number*factorial(number-1)

sonuc=factorial(number)
print(sonuc)


