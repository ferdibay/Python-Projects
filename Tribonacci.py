
def tribo():
    a=1
    b=1
    c=1
    d=0

    sayi=int(input("Tribonacci dizisinin nin ilk kaç elemanını istiyorsunuz: "))

    if sayi<3:
        print("Tribonacci dizisi en az 3 elemandan oluşur!")
    
        return tribo()
      
    elif sayi>=3:
        
        print("1 \n1 \n1")
        
        for i in range(sayi-3):
            
            d=a+b+c
            a=b
            b=c
            c=d
     
            print(d) 

    else:
        return 0        


tribo()            



