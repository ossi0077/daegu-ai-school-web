# 반복문을 배워보자
members=['oss', 'spoon']
for member in members :
    print(f'member : {member}')

print('\n')
members2 = [
    ['egoing','seoul','programmer'],
    ['oss','daegu','to be programmer']
]

print(members2[0][0])
print('\n')
for member in members2 :
    print(f'{member[0]}, {member[1]}, {member[2]}')


#dictionary 실습
oss = ['egoing','seoul','programmer']
oss = {'name':'egoing','city':'seoul','job':'programmer'} #사전형
print('\n')
for item in oss:
    print(item)
print('\n')
for item in oss:
    print(oss['name'])

print('\n')
members3 = [
    {'name':'egoing','city':'seoul','job':'programmer'},
    {'name':'oss','city':'daegu','job':'to be programmer'}
]
for member in members3 :
    print(member['name'])