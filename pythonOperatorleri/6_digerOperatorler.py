# Identity Operator: is

x=y=[1,2,3]
z=[1,2,3]

print(x==y)
print(z==x)
# objelerin aynı mı değil mi yani aynı adrese sahipler mi
print(x is y )
print(x is z ),
x=[1,2,3]
y=[2,4]

del x[2]
y[1]=1
y.reverse()

print(x==y)
print(x is y )
print(x is not y)

# Membership Operator: in

x=['apple','banana']
print('banana'in x ) # liste içerisinde var mıdır diye sorar
name =('esma')
print('e'in name)
print('e'not in name)







