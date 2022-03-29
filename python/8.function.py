#함수를 배워보자
def sum(a,b) :
    return a+b

def byte_to_bit(byte_):
    return byte_*8
print('\n')
times=[1,2,3]
for i in times:
    choice_val = int(input(f'1 : sum \n2 : byte_ to bit\nYour choice : '))
    if choice_val==1:
        # print('\n')
        first_value = int(input(f'first value : '))
        second_value = int(input(f'second value : '))
        print(sum(first_value,second_value))
        print(f'------{i}회 실행------')
    elif choice_val==2:
        value = int(input('몇 byte?'))
        print(byte_to_bit(value))
        print(f'------{i}회 실행------')
    else :
        print('you choice wrong number.')
        print(f'------{i}회 실행------')
