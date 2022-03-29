times=[1,2,3]
for j in times:
    ID_name = input('Input your ID_name : ')
    if ID_name=='oss':
        print('주인장 납시오!!')
        password=input('Input your password : ')
        if password=='sso' :
            print('주인장 맞네!')
            print(f'--{j}회 동작 끝--')
        else :
            print('뭐야 너 누구야')
            print(f'--{j}회 동작 끝--')
    else :
        print('손놈 납시오!!!')
        print(f'--{j}회 동작 끝--')

        