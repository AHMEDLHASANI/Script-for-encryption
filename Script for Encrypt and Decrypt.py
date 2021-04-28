
text = "1234567890azertyuiopqsdfghjklmwxcvbn"
from random import sample
Go = []
power = int(input("power of key :"))
for i in range(len(text)):Go.append("".join(sample(text,power)))
for u in Go :print(u,end=":")
key1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'w', 'x', 'c', 'v', 'b', 'n'," "]
c = input("\nkey : ")
key2 = c.split(":")
dict ={}
for u in range(len(key1)):
    dict.update({key1[u]:key2[u]})
print("Encrypt : 1","\nDecrypt : 2")
def boos():
    check = input("> ")
    if check == "1" :
        def en():
            text1 = input("\nYour Text : ").lower()
            if text1 == ">exit" :
                return boos()
            else :
                for i in text1 :
                    for key,value in dict.items():
                        if i == key :
                            print(value,end=":")
            return en()
        en()
    elif check == "2" :
        def de():
            print("fcl:wk5:wk5:172:")
            text2 = input("\nYour Text : ")
            if text2 == ">EXIT" :
                return boos()
            else :
                text2.lower()
                clearText = text2.split(":")
                for i in clearText :
                    for key,value in dict.items():
                        if i == value :
                            print(key,end="")
            return de()
        de()
    else :
        print("Error, Try again\nFollow me in twitter @Ahmedlhasani")
        return boos()
boos()
#Check This :
#a8s:a6o:g68:ase:ka0:gvf:glj:ltc:gmp:wbg:aim:3xb:4ki:7h9:lv9:7cg:mok:3a5:wk5:s79:rk9:172:g69:hp9:gyj:j8t:4rt:mz6:i6p:k51:e4b:uo1:c8v:c85:fcl:u2r:
#------------------#
#hp9:wk5:i6p:i6p:wk5:e4b::k51:4ki::3a5:u2r::lv9:e4b:3a5:lv9:lv9:4ki:lv9::aim:j8t:k51:4ki:g69:i6p:j8t:aim:172:aim:u2r:3a5:
