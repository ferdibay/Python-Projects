# isim oluşturucu..
import random

def generate_name():
    first_name=["ali","veli","murat","onur","lara","yağız","cenker"]
    last_name=["bayram","zengin","korkusuz","sevecen","derin"]

    return "{} {}".format(random.choice(first_name),random.choice(last_name))

for i in range(5):
    print(generate_name())
