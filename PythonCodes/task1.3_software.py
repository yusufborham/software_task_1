# Implement a program that takes an amount of money (in Egyptian Pounds), and outputs the least amount of papers that can form that amount of money.
# Examples:
# Input: 217	Output: 1x 200 L.E. + 1x 10 L.E. + 1x 5 L.E. + 2x 1 L.E.
# Input: 453	Output: 2x 200 L.E. + 1x 50 L.E. + 3x 1 L.E.
# Recall that Egyptian Pounds can be in the form of those paper bills: 1 L.E, 5 L.E, 10 L.E, 20 L.E, 50 L.E, 100 L.E, and 200 L.E.
while True :
 print('')
 money=int(input('enter the amount of money '))
 u=money
 i_200=0
 i_100=0
 i_50=0
 i_20=0
 i_10=0
 i_5=0
 i_1=0

 while money>=200 :
    money=money-200
    i_200=i_200+1 
 if(i_200 !=0) : 
       print(i_200,'x 200 L.E. ',end='')
    
 while money>=100 :
    money=money-100
    i_100=i_100+1
 if(i_100 !=0) : 
       print(i_100,'+ x 100 L.E. ',end='')
    
 while money>=50 :
    money=money-50
    i_50=i_50+1
 if(i_50 !=0) : 
       print(i_50,'+ x 50 L.E. ',end='')
    
 while money>=20 :
    money=money-20
    i_20=i_20+1
 if(i_20 !=0) : 
       print(i_20,'+ x 20 L.E. ',end='')
   
 while money>=10 :
    money=money-10
    i_10=i_10+1
 if(i_10 !=0) : 
       print(i_10,'+ x 10 L.E. ',end='')
    
 while money>=5 :
    money=money-5
    i_5=i_5+1     
 if(i_5 !=0) : 
       print(i_5,'+ x 5 L.E. ',end='')  
    
 while money>=1 :
    money=money-1
    i_1=i_1+1 
 if(i_1 !=0) : 
       print(i_1,'+ x 1 L.E.',)
    
  