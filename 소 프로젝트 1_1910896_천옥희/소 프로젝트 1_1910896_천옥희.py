#1-1
import random #난수 발생모듈, 임의의 두 정수를 생성하기 위해 필요
for i in range(1,6): #문제1~문제5 5개의 문제 출제를 위한 함수
    num1=random.randint(10,100) #첫번째 정수의 변수, 임의의 두자릿수의 정수 생성
    num2=random.randint(10,100) #두번째 정수의 변수, 임의의 두자릿수의 정수 생성
    answer=int(input('문제%d: %d+%d?'%(i, num1, num2))) #사용자가 입력한 답, 사용자의 답 입력 받기
    if answer==num1+num2:   #사용자가 입력한 답이 정답일때의 '정답입니다!'를 출력
        print('정답입니다!')
    else:                   #사용자가 입력한 답이 틀렸을 때의 '틀렸습니다!'를 출력
        print('틀렸습니다!')

#1-2
import random #난수 발생모듈, 임의의 두 정수와 연산자를 생성하기 위해 필요

for i in range(1,6): #문제1~문제5 5개의 문제 출제
    num1=random.randint(10,100) #첫번째 정수의 변수, 임의의 두자릿수의 정수 생성
    num2=random.randint(10,100) #두번째 정수의 변수, 임의의 두자릿수의 정수 생성
    symbol = ['+', '-', '*']  # 연산자 리스트
    arithmetic = random.choice(symbol) #랜덤하게 정해진 연산자의 변수,연산자를 랜덤생성
    answer=int(input('문제%d: %d%s%d?'%(i, num1, arithmetic, num2))) #사용자가 입력한 답, 사용자의 답 입력 받기
    if arithmetic=='+':       #랜덤하게 정해진 연산자가 +일 경우의 조건문
        if answer==num1+num2: #사용자가 입력한 답이 정답일때의 '정답입니다!'를 출력
            print('정답입니다!')
        else:                 #사용자가 입력한 답이 틀렸을 때의 '틀렸습니다!'를 출력
            print('틀렸습니다!')
    elif arithmetic=='-':     #랜덤하게 정해진 연산자가 -일 경우의 조건문
        if answer==num1-num2:  #사용자가 입력한 답이 정답일때의 '정답입니다!'를 출력
            print('정답입니다!')
        else:                  #사용자가 입력한 답이 틀렸을 때의 '틀렸습니다!'를 출력
            print('틀렸습니다!')
    else:                      #랜덤하게 정해진 연산자가 *일 경우의 조건문
        if answer==num1*num2:  #사용자가 입력한 답이 정답일때의 '정답입니다!'를 출력
            print('정답입니다!')
        else:                  #사용자가 입력한 답이 틀렸을 때의 '틀렸습니다!'를 출력
            print('틀렸습니다.')


#1-3
import random   #난수 발생모듈, 임의의 두 정수와 연산자를 생성하기 위해 필요
import time     #시간과 관련된 모듈, 시간 제한을 주기위해 필요

correct= 0      #정답개수의 초깃값

for i in range(1,6):  #문제1~문제5 5개의 문제 출제
    num1=random.randint(10,100)  #첫번째 정수의 변수, 임의의 두자릿수의 정수 생성
    num2=random.randint(10,100)  #두번째 정수의 변수, 임의의 두자릿수의 정수 생성
    symbol = ['+', '-', '*']  #연산자 리스트
    arithmetic = random.choice(symbol) #랜덤하게 정해진 연산자의 변수,연산자 랜덤생성
    starttime=time.time() #문제출제시간
    answer=int(input('문제%d: %d%s%d?'%(i, num1, arithmetic, num2))) #사용자가 입력한 답, 사용자의 답 입력 받기
    endtime=time.time() #문제맞춘시간
    taketime=endtime-starttime  #문제 맞추는데 걸린 시간, 문제맞춘시간-문제출제시간
    if arithmetic == '+':        #랜덤하게 정해진 연산자가 +일 경우의 조건문
        if answer==num1+num2: #두개의 정수를 더한 값을 맞췄을 경우
            if taketime < 5:     #시간 내에 맞췄을 경우 '시간내에 맞췄습니다'를 출력
                print('시간 내에 맞췄습니다.')
                correct= correct+1 #시간 내에 맞췄을 때 정답의 갯수 1증가
            else:                 #맞췄지만 시간을 초과했을 때 '답을 맞췄으나 시간이 초과되었습니다'를 출력
                print('답을 맞췄으나 시간이 초과되었습니다.')
        else:                     #사용자가 입력한 답이 틀렸을 때의 '틀렸습니다.'를 출력
            print('틀렸습니다.')  
    elif arithmetic == '-':   #랜덤하게 정해진 연산자가 -일 경우의 조건문
        if answer==num1-num2: #두개의 정수를 뺀 값을 맞췄을 경우
            if taketime < 5:      #시간 내에 맞췄을 경우 '시간내에 맞췄습니다'를 출력
                print('시간 내에 맞췄습니다.')
                correct= correct+1  #시간 내에 맞췄을 때 정답의 갯수 1증가
            else:                    #맞췄지만 시간을 초과했을 때 '답을 맞췄으나 시간이 초과되었습니다'를 출력
                print('답을 맞췄으나 시간이 초과되었습니다.')
        else:                       #사용자가 입력한 답이 틀렸을 때의 '틀렸습니다.'를 출력
            print('틀렸습니다.')
    else:                     #랜덤하게 정해진 연산자가 *일 경우의 조건문
        if answer==num1*num2:  #두개의 정수를 곱한값을 맞췄을 경우
            if taketime < 5:       #시간 내에 맞췄을 경우 '시간내에 맞췄습니다'를 출력
                print('시간 내에 맞췄습니다.')
                correct= correct+1  #시간 내에 맞췄을 때 정답의 갯수 1증가
            else:                   #맞췄지만 시간을 초과했을 때 '답을 맞췄으나 시간이 초과되었습니다'를 출력
                print('답을 맞췄으나 시간이 초과되었습니다.')
        else:                      #사용자가 입력한 답이 틀렸을 때의 '틀렸습니다.'를 출력
            print('틀렸습니다.')
print('정답을 맞춘 갯수: %d/5' %correct) #5개 중에 시간내에 맞춘 정답의 개수를 출력





