import random

while True:
    ilk_kahraman = input("-----İlk Kahraman ----- \nLütfen kahramanınızın adını yazın: ")
    if len(ilk_kahraman) > 1:
        print("İlk kahramanın adı:", ilk_kahraman.capitalize())
        break
    else:
        print("Kahramanınızın adı en az 1 karakter almalıdır!")

while True:
    ikinci_kahraman = input("----- İkinci Kahraman ----- \nLütfen kahramanınızın adını yazın: ")
    if len(ikinci_kahraman) <= 1:
        print("Kahramanınızın adı en az 1 karakter almalıdır!")
    elif ilk_kahraman == ikinci_kahraman:
        print(ilk_kahraman, "alındı, lütfen başka bir isim seçin!")

    else:
        print("İkinci kahramanınızın adı"), ikinci_kahraman.capitalize()
        break

oyuncular_listesi = [ilk_kahraman, ikinci_kahraman]
yazi_tura = random.choice(oyuncular_listesi)
oyuncular_listesi.remove(yazi_tura)
print(f"Yazı tura sonucu:{yazi_tura}önce başlar")  # yazı tura sonucu


def atak1(current_hp):
    hp2 = current_hp
    chance_of_damaging = random.randint(0, 100)
    print(f"--------------- {yazi_tura} SALDIR !! ---------------")
    while True:
        attack_magnitute = int(input("Atağınızın büyüklüğünü seçin (1 ie 50): "))

        if attack_magnitute > 50:
            print("Atak büyüklüğü 1 ile 50 arasında olmalı.")

        elif attack_magnitute < 1:
            print("Atak büyüklüğü 1 ile 50 arasında olmalı.")
        else:
            break

    while True:
        if chance_of_damaging > attack_magnitute:
            print(yazi_tura, f"{attack_magnitute} hasar aldı!!")
            hp2 = hp2 - attack_magnitute
            return hp2
        else:
            print(f"{yazi_tura} atağı kaçırdı!")
            return hp2


def attack2(current_hp):
    hp1 = current_hp
    chance_of_damaging = random.randint(0, 100)
    print(f"--------------- {oyuncular_listesi} SALDIR !! ---------------")
    while True:
        attack_magnitute = int(input("Atağınızın büyüklüğünü seçin (1 ie 50): "))

        if attack_magnitute > 50:
            print("Atak büyüklüğü 1 ile 50 arasında olmalı.")

        elif attack_magnitute < 1:
            print("Atak büyüklüğü 1 ile 50 arasında olmalı.")
        else:
            break

    while True:
        if chance_of_damaging > attack_magnitute:
            print(oyuncular_listesi, f"{attack_magnitute} hasar aldı!!")
            hp1 = hp1 - attack_magnitute
            return hp1
        else:
            print(f"Ooopsy! {oyuncular_listesi} atağı kaçırdı!")
            return hp1


def main():
    hp1, hp2 = (100, 100)
    while hp2 <= 1:
        print(oyuncular_listesi, " kazandı")
        break

    while hp1 > 1 and hp2 > 1:
        hp1 = atak1(hp1)
        print(yazi_tura, "                                                                ")

        print(f"HP [{hp2}]:", hp2 //2 * "|", "        ", f"HP [{hp1}]:", hp1 // 2 * "|")
        hp2 = attack2(hp2)
        print(yazi_tura, "                                                                ")

        print(f"HP [{hp2}]:", hp2 //2 * "|", "        ", f"HP [{hp1}]:", hp1 // 2 * "|")

    while hp1 <= 1:
        print(yazi_tura, " kazandı")
        break


main()

