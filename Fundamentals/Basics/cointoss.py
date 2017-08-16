import random
def Coin_Toss():
    
    sumh = 0
    sumt = 0
    x = random.random()
    x_rounded = int(round(x))   

    for index in range(1,5001):
        x = random.random()
        x_rounded = int(round(x))

        if x_rounded == 1: 
            sumh += 1
            print "Attempt #",index,":"," Throwing a coin ... It's heads ... Got ",sumh," head(s) so far and ",sumt," tail(s) so far"
        else: 
            sumt += 1
            print "Attempt #",index,":"," Throwing a coin ... It's heads ... Got ",sumt," head(s) so far and ",sumh," tail(s) so far"
       


Coin_Toss()



