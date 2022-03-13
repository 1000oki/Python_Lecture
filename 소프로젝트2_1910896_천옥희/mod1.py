#mod1
#2-1
#pythonLecture 클래스 정의
class PythonLecture:
    def __init__(self,first,second,third,absence):  #멤버함수 __init__ ,(1차 시험점수, 2차 시험점수, 3차 시험점수, 결석횟수)
        self.first=first
        self.second=second
        self.third=third
        self.absence=absence

    # 3개의 시험의 평균 점수를 산출하는 함수
    def average(self):
        return (self.first+self.second+self.third)/3

    # 3개의 점수를 20%, 30%, 50% 가중치로 평균을 산출하는 함수
    def weightavg(self):
        return self.first*0.2+self.second*0.3+self.third*0.5
#2-2
    #가중치 평균을 최종성적으로 받아 학점을 산출하는 함수
    def grade(self):
        final=self.weightavg()      #가중치 평균 final에 반환
        if self.absence<5:          #결석이 5회 미만일 때
            if final >= 90:         #가중치 평균이 90점이상~100점일 때 학점 A
                return 'A'
            elif final >= 80:       #가중치 평균이 80점 이상~90점 미만일 때 학점 B
                return 'B'
            elif final >= 70:       #가중치 평균이 70점 이상~80점 미만일 때 학점 C
                return 'C'
            elif final >= 60:       #가중치 평균이 60점 이상~70점 미만일 때 학점 D
                return 'D'
            else:                   #가중치 평균이 60점 미만일 때 학점 F
                return 'F'
        else:                       #결석이 5회 이상일 때 성적 상관없이 학점 F
            return 'F'


