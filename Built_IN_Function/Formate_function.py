



user =['prahlad chandra','shubham ','rohan das','mayank ','arcgate udaipur']
computer =['anroid','mac','iphone','raspberry pi']
template= "Computer used by {} is {}"
# for i in range(0,len(user)):
#     print("Computer used by ",user[i],"is",computer[i])  Before formate function
for i in range(len(user)):
   print(template.format(user[i],computer[i]))