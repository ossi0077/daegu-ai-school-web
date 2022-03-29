#출력
print(1)
print(2)
print(3)

print(1.2)
print(1+1)
print(2-1)
print(2*2)
print(6/2)

# 3을 두번곱하라는 뜻(제곱)
print(pow(3,2))
print(3**2)

#import로 라이브러리를 연동하자!
import random
print(random.random())

#String
print('Hello')
print("Hello")
# 따옴표 세개로 여러줄로 표현할 수 있다.
print('''
Hello
World
''')
# 문자열 길이 구하는 방법
print(len('hello'))
# 문자 바꾸기
print('hell world'.replace('hell','hello'))

#List(배열)
member = ['a','b','c']
print(member[0])
print(len(member))

print(random.choice(member))
score=[100,200,300]
print(sum(score))