while True :
 text=input('enter the sentance to compute ')
 sentences=text.count('.')+text.count('!')+text.count('?')
 spaces=text.count(' ')
 extra=text.count(',')+text.count(':')+text.count(';')+text.count('"')+text.count("'")
 letters=len(text)-sentences-spaces-extra
 words=len(text.split())
 L=(letters/words)*100
 S=(sentences/words)*100
 index = 0.0588 * L - 0.296 * S - 15.8
 if index>=16:
    print('Grade is 16+')

 elif int(index) <= index-0.5 :
    print('Grade is ', int(index)+1)
 elif int(index) > index-0.5 :
    print('Grade is ',int(index))
 

