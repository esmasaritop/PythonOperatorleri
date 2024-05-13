x =int(input('sayi giriniz: '))

hak=5
devam='e'

result= 5 <= x < 10
print(result)

#and
result= (x>5) and (x<10) # true,true>> True /// true,false>>> False
print(result)

result=(hak>0)and (devam=='e')
print(result)

#or
result=(x>0) or (x%2==0) # or operatorunun biri true olması yeterli sonucun true olması icin

#not
result= not(x>0) #sordugun sorunun tersini alıyor

# x, 5-10 arasında olan bir çift sayı mı ?
result= ((x<10) and (x>5)) and (x%2==0)
print(result)

