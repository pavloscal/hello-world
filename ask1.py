running=True
import random

   
my_randoms=[]    
for i in range (4):    
    my_randoms.append(random.randrange(1,5,1))
    if my_randoms[i]==1:
        posx=my_randoms[i]
    elif my_randoms[i]==2:
            posx=my_randoms[i]
    elif my_randoms[i]==3:
                posx=my_randoms[i]
    elif my_randoms[i]==4:
                        posx=my_randoms[i]
     
  

my_randoms2=[]
for j in range (4):
    my_randoms2.append(random.randrange(1,5,1))
    if my_randoms2[j]==1:
        posy=my_randoms2[j]
    elif my_randoms2[j]==2:
            posy=my_randoms2[j]
    elif my_randoms2[j]==3:
                posy=my_randoms2[j]
    elif my_randoms2[j]==4:
                        posy=my_randoms2[j]
     
    


 

 
my_randoms3=[]    
for n in range (4):    
    my_randoms3.append(random.randrange(1,5,1))
    if my_randoms2[n]==1:
        posx2=my_randoms3[n]
    elif my_randoms3[n]==2:
            posx2=my_randoms3[n]
    elif my_randoms3[n]==3:
                posx2=my_randoms3[n]
    elif my_randoms3[n]==4:
                        posx2=my_randoms3[n] 
      
  

my_randoms4=[]
for v in range (4):
    my_randoms4.append(random.randrange(1,5,1))
    if my_randoms2[v]==1:
        posy2=my_randoms2[v]
    elif my_randoms4[v]==2:
            posy2=my_randoms4[v]
    elif my_randoms4[v]==3:
                posy2=my_randoms4[v]
    elif my_randoms4[v]==4:
                        posy2=my_randoms4[v]
    



print  "your place is",[posx,posy]

while running :
    
    m = int(input('press 1. to go right,2.to go up,3. to go left,4 to go down : '))
    y=posx-posx2
    x=posy-posy2

    if (m==1):
      posx=posx+1
      print "the distance is %s" %(abs(x)+abs(y))
    elif(m==2):
      posy=posy-1 
      print "the distance is %s" %(abs(x)+abs(y))
    elif(m==3):
      posx=posx-1
      print "the distance is %s" %(abs(x)+abs(y))                                                                                                               
    else:
         posy=posy+1
         print"the distance is %s" %(abs(x)+abs(y))
    if(posx==posx2):
        if(posy==posy2):
            running=False
            
    if (abs(x)+abs(y))==0:
        running=False
    

print"you WON"
            
        


