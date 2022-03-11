



"""
def fibonacci(n):
    #eleman=int(input("eleman sayısı:")) #bu durumda n yerine eleman yazılırdı..
    a=1
    b=1

    if (n>=2):
        print(a)
        print(b)
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(c)
    else:
        print("fibonacci en az 2 elmandan oluşur!")

fibonacci(10)                
"""




#Bir Stringteki harfler alfabetik sıradaysa True döndüren fonksiyonu yazınız..
def siraliMi():
    kelime=input("Bir kelime yazın:")
    dizi=[]
    dizi2=[]
    
    i=0
    while(i<len(kelime)):
            dizi.append(kelime[i])
            i+=1    

    dizi2=sorted(dizi)

    if (dizi==dizi2):
        return True         
    else:
        return False      
            
print(siraliMi())

