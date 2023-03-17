# user has 50 coins
coin = 50

# Asks user to insert coin with defined amounts, if user puts undefined amount it prints same coin, when user puts defined coins it prints how many coins user has left, and when it reaches 0 it prints change owed 0
while coin > 0:
    print ("Amount Due: " + str(coin))
    coinamount = int(input("Insert Coin: "))
    
    if coinamount == 25 or coinamount == 10 or coinamount == 5:
            
        coin -= coinamount
           
            
change_owed = abs(coin)
print ("Change Owed:", change_owed)
            
        
    
          

        
                                    
          

         

            
           


            


        