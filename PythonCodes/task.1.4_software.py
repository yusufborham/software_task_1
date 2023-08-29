while True :
 x=list(input('enter card number '))
 ln=len(x)
 i=ln
 y=0
 sum=0
 fs=0
 z=[]
 p=[]
 o=[]
 
 for i in range(ln,0,-1) :
        if (ln-i)%2 !=0:
          y=x[i-1]
          k=int(y)
          k=2*k
          if k<=9 :
              z.append(k)
          elif k>9 :
              z.append(1)
              k=k%10
              z.append(k) 
        elif (ln-i)%2==0 or x==0 :
            m=x[i-1]
            n=int(m)
            p.append(n)         
 a=z+p
 for q in range(0,len(a)) :
    g=a[q]
    t=int(g)
    sum=t+sum
 for w in range (0,2):
    r=x[w]
    d=int(r)
    fs=10*fs+d

 if (fs==51 or fs==52 or fs==53 or fs==54 or fs==55) and sum%10==0:
    print('Master Card *valid*')
 elif x[0]=='4' and sum%10==0 :
    print('Visa *valid*')
 elif (fs==37 or fs==34  ) and sum%10==0:
    print('American Express*valid*')
 else:
    print('invalid')