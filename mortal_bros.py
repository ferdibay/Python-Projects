import random

# bu bölümde kahramanların isim bilgisini alıyoruz
def isim(yazi, digerKahraman):
    while True:
        print('-----', yazi, 'Kahraman -----')

        name = input("Lütfen kahramanınızın adını yazın: ")
        name = name.capitalize()

        #eğer bu isim alınmışsa başka bir isim girmesini istiyoruz
        if name in digerKahraman:
            print(name, "alındı,lütfen başka bir isim seçin")
        else:
            print(yazi, "kahramanın adı", name)
            break

    return name

# bu bölümde saldırı büyüklüğü istiyoruz
def saldiriBuyuklugu():
        deger = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin: "))

        if deger > 50:
            print ("Saldırı büyüklüğü 1 ile 50 arasında olmalıdır.")
        elif deger < 1:
            print ("Saldırı büyüklüğü 1 ile 50 arasında olmalıdır.")
        else:
            return deger

#random modülüyle saldırıya geçecek kahramanın hasarını alıyoruz.
def saldiri(puan, ad):

    hasar = random.randint(0, 100)

    print("---------------", ad, "Saldır !! ---------------")

    atak = saldiriBuyuklugu()


    if hasar > atak:
        print(ad, "hasar", atak, "verdi!!")
        puan -= atak
    else:
        print("Ooopsy!", ad, "saldırıyı kaçırdı!")

    return puan

#ekranda güncel puan(can) bilgilerini bazı matematiksel operatörler kullanarak yazdırıyoruz
def ekran(puan1, puan2, ad1, ad2):
    print(ad1, "                                                                 ", ad2)
    print(f"HP [{puan2}]:", puan2//2 * "|" ,"        ",f"HP [{puan1}]:", puan1//2 * "|" ,"        ")


def oyun():

    liste = []

    kahraman = isim("İlk", liste)
    liste.append(kahraman)

    kahraman = isim("İkinci", liste)
    liste.append(kahraman)

    random.shuffle(liste)

    yazi_tura = liste[0]
    oyuncu= liste[1]

    print(f"Yazı tura sonucu: {yazi_tura} önce başlar!")

    # döngü

    running = True

    while running:

        hp1, hp2 = (100, 100)

        # oyun

        while hp1 > 1 and hp2 > 1:
            hp1 = saldiri(hp1, yazi_tura)
            ekran(hp1, hp2, yazi_tura, oyuncu)

            if hp1 <= 1:
                break

            hp2 = saldiri(hp2, oyuncu)
            ekran(hp1, hp2, yazi_tura, oyuncu)

        # oyun bitti

        if hp1 <= 1:
            print(yazi_tura, " kazandı")
        if hp2 <= 1:
            print(oyuncu, " kazandı")



        soru = input('Tekrar oynamak ister misiniz [Y/N]?').lower().strip()


        if soru == 'y':
            running = True
        else:
            running = False


oyun()


# Projenin belli bölümlerinde google,github tan yardım aldım. örnek sayılabilecek kodları inceledim ..