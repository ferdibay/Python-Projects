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

