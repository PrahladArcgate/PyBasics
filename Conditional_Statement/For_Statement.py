# Python’s for statement iterates over the items of any sequence (a list or a string), 
# in the order that they appear in the sequence. 
# words =['cat','dog','animal']
# for w in words:
#     print(w,len(w))


user = {'Activa':'Honda','Vespa':'Hero'}

for use,status in user.copy().items():
    if status =='inactive':
        del user[user]


active_users={}
for user_1, status in user.items():
    if status == 'active':
        active_users[user_1]=status