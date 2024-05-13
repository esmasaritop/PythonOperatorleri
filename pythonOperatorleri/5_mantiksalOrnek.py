# 1- Girilen bir sayının 0-100 arasında olup olmadıgını kontrol ediniz
sayi=float(input('Sayı giriniz: '))
result = (sayi<=100) and (sayi>0)
print(f'{sayi} sayisi 0-100 arasında mı:{result}')

# 2- Girilen bir sayının pozitif çift sayı olup olmadıgını kontrol ediniz
sayi= float(input('Sayı giriniz: '))
result= (sayi>0) and (sayi%2==0)
print(f'{sayi} çift midir : {result}')

# 3- Email ve parola bilgileri ile giriş kontrolu yapınız
email='esmasaritop@gmail.com'
password='abc123'

girilenmail=input('email: ')
girilenPassword=input('password: ')

result= (girilenmail==email) and (girilenPassword==password)
print(f'uygulamaya giriş başarılı mı : {result}')

# 4- Girilen 3 sayıyı büyüklük olarak karsılastırınız
a=int(input('Sayı1: '))
b=int(input('Sayı2: '))
c=int(input('Sayı3: '))
result=(a>b) and (a>c)
print(f'Sayı1 en büyük sayı mıdır: {result}')
result=(b>a) and (b>c)
print(f'Sayı2 en büyük sayı mıdır: {result}')
result=(c>b) and (c>a)
print(f'Sayı3 en büyük sayı mıdır: {result}')

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
# Eğer ortalama 50 ve üstü ise gecti değilse kaldı
# a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır
# b-) finalden 70 aldıgında ortalamanın onemi olmasın
vize1=float(input('vize1: '))
vize2=float(input('vize2: '))
final=float(input('final: '))
ortalama=((((vize1+vize2)/2)*0.6)+(final*0.4))
result= (ortalama>=50) and (final>=50)
print(f'öğrencinin ortalaması:{ortalama} ve geçme durumu: {result}')
