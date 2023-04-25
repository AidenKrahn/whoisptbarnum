#oop
#AidenKrahn
#April 24

class bewd():
    attackpoints = 3000
    def attack():
        print("Blue Eyes White Dragon attacked")
        
    def defend():
        print("Blue Eyes White Dragon defended")
        
class darkmagician():
    attackpoints = 2500
    def attack():
        print("Dark Magician attacked")
        
    def defend():
        print("Dark Magician defended")
        

corn = input("Kaiba or Yugi?  ")
if corn == 'kaiba':
    kaiba = bewd
    corn2 = input("A or D?  ")
    if corn2 == 'a':
        kaiba.attack()
        print(kaiba.attackpoints)
        
    elif corn2 == 'd':
        kaiba.defend()
            
    else:
        print('no')
    
elif corn == 'Yugi':
    yugi = darkmagician()
    corn2 = input("A or D?  ")
    if corn2 == 'a':
        yugi.attack()
        print(yugi.attackpoints)
        
    elif corn2 == 'd':
        yugi.defend()
            
    else:
        print('no')
else:
    print('no')