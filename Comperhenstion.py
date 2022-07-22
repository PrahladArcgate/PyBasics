''' Comprehentions
 List 
 Dictionary
 set 
'''
# list comprihentions
Number=[3,4,56,674,33,556,3456]
divi_3=[]
for item in Number:
    if item%3 == 0:
        divi_3.append(item)
print("without using list comprihention ",divi_3)
print("Using Comprehensions",[item for item in Number if item%3==0])

#Dictionary Comparihentions

dic1= {'a':45,'b':65,'A':5}
print({k.lower():dic1.get(k.lower(), 0)+dic1.get(k.upper(), 0) for k in  dic1.keys()})

squared ={x**2 for x in [1,2,3,5,43,2,3,4,43,34,22,5,6,7,7]}   # Set Comprihentions
print(squared)

#genrator compri

gen = (i for i in range(56))
print(gen)
