name=input("Lütfen adınızı girin:")
print(f"Hoşgeldin {name}!")

word="metallica"
live=len(word)
empty_string=""

while True:
    count=0
    guess_char=input("Bir harf girin:")
    empty_string += guess_char

    if guess_char not in word:
        live -=1
        print(f"{live} canınız kaldı!!")
    
    if live==0:
        print("Bir daha deneyin!!")
        break

    for i in word:
        if i in empty_string:
            print(i)
        else:
            print("-")
            count+=1   
            
    if count==0:
        print("Tebrikler kazandın!!")
        break    


