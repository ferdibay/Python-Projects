def fonk(word):
    
    new=list(word)
    new2=sorted(new)

    if new==new2:
        return True
    else:
        return False    

c=fonk("asz")        
print(c)