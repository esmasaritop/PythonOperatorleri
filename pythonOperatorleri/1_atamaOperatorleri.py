#x=5
#y=10
#z=20

x,y,z=5,10,20
print(x,y,z)
x,y=y,x # değişkenlerin içeriği değişir
print(x,y,z)
x-=5        #x=x-5
x+=5        #x=x+5
x*=5        #x=x*5
x/=5        #x=x/5
x%=5        #x=x%5
x//=5       #x=x//5     #bölmede tam tarafı tek alır
y**=z       #y=y**z     #üst alma
print(x,y,z)

values=1,2,3,4,5

print(type(values))

x,y,*z=values # znin basına yıldız eklediğimiz izin xve y'ye kadar her eleman eslesir geri kalan liste halinde zye gider

print(x,y,z[1])  #z'nin elemanlarına da böyle ulaşılabilir (index numarası ile)
