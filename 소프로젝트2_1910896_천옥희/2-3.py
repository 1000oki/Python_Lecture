#2-3
import mod1           #mod1 모듈(PythonLecture클래스 사용을 위함)
print('='*31)         #'='의 30개 출력
print('Python Lecture Score Calculator')  #'Python Lecture Score Calculator' 출력
print('='*31)          #'='의 30개 출력

for i in range(1,4):                      #1~3까지 차례로 대입
    a=input('Student %d > ' %i).split()   #학생의 1차 2차 3차 시험 점수와 결석횟수 입력받고 공백을 기준으로 문자열 분리
    # i=1일 때, 학생 1이라는 객체를 가짐
    if i== 1:
        # 리스트인 a에서 인덱싱으로 각각의 변수값 가져오고, 정수로 바꾸줌
        student1 = mod1.PythonLecture(int(a[0]),int(a[1]),int(a[2]),int(a[3]))
    # i=2일 때, 학생 2이라는 객체를 가짐
    elif i==2:
        # 리스트인 a에서 인덱싱으로 각각의 변수값 가져오고, 정수로 바꾸줌
        student2 = mod1.PythonLecture(int(a[0]), int(a[1]), int(a[2]), int(a[3]))
    # i=3일 때, 학생 3이라는 객체를 가짐
    else:
        # 리스트인 a에서 인덱싱으로 각각의 변수값 가져오고, 정수로 바꾸줌
        student3 = mod1.PythonLecture(int(a[0]), int(a[1]), int(a[2]), int(a[3]))
#============Result============= 출력
print('='*12+'Result'+'='*13)
#Num Score Grade 출력
print('Num Score Grade')
#학생의 순서, 최종성적, 학점 순으로 출력
print(' 1  %0.2f   %s' %(student1.weightavg(),  student1.grade()))
print(' 2  %0.2f   %s' %(student2.weightavg(),  student2.grade()))
print(' 3  %0.2f   %s' %(student3.weightavg(),  student3.grade()))
