a=['Prahlad','tSeriese','ashish','telusko','pen']
# i=0
# for item in a:
#     i=i+1                           without using Enumarater function
#     if i%2 ==0:
#         print(item)


# using Enumarate function  ..............
for i ,item in enumerate(a):
    if(i+1) %2 ==0:
        print(item)