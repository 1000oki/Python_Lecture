#1번 문제
f=open('1910896_천옥희.txt','w')
data="☆"*20+'\n프로그래밍 입문 중간고사 답안지\n'+"☆"*20+'\n학번: 1910896 \n이름: 천옥희'+'\nSookmyung Women\'s University'
f.write(data)
f.close()

with open('1910896_천옥희.txt','a') as f:
    f.write('''\n안녕하세요. 저는 숙명여자대학교 통계학과 1910896 천옥희입니다. 
주 전공은 통계학과이지만, 수학 이외에 it에도 관심있어 it 복수전공하려 합니다. 
제 고향은 천일염과 1004의 섬으로 유명한 신안입니다. 섬으로 고등학교를 다녀 배를 타고 고등학교에 다녔습니다!
제 취미는 혼자 요리하는 것이고, 좋아하는 음식은 떡볶이여서 일주일에 한 번은 꼭 먹습니다.
친구들, 가족들 사람들과 만나 이야기하는 것을 좋아하고, 사진찍는 것도 좋아합니다.
    ''')
with open('1910896_천옥희.txt','r') as f:
    data=f.read()
    print(data)

#2번 문제
class okcafe:
    def __init__(self,price,calorie,quantity):
        self.__price=price
        self.__calorie=calorie
        self.__quantity=quantity
    def reduce(self):
        if self.__quantity>0:
            self.__quantity = self.__quantity-1
        elif self.__quantity==0:
            print('''선택하신 음료의 잔여 수량이 없습니다. 
빠른 시일 내에 준비하겠습니다. 죄송합니다.
다른 음료를 선택해 주세요!''')
    def getPrice(self):
        return self.__price
    def getCalorie(self):
        return self.__calorie
    def getQuantity(self):
        return self.__quantity
americano=okcafe(3800,90,5)
moca=okcafe(4500,290,5)
greentea=okcafe(5000,185,4)
print('챗봇> 어서오세요! 여기는 행복으로 가득한 okcafe입니다.')
while True:
    print('-' * 39)
    print("♡"*10+'okcafe 메뉴판'+'♡'*10)
    print('1. 아메리카노 3800원|90칼로리|잔여수량:{0}'.format(americano.getQuantity()) )
    print('2. 카페모카   4500원|290칼로리|잔여수량:{0}'.format(moca.getQuantity()))
    print('3. 그린티라떼 5000원|185칼로리|잔여수량:{0}'.format(greentea.getQuantity()))
    print('4. 나가기')
    print('♡'*26)
    print('-'*39)
    menu=int(input('챗봇> 원하시는 메뉴를 주문해주세요:'))
    if menu==1:
        if americano.getQuantity()==0:
            print('아메리카노를 주문하셨습니다.')
        else:
            print('''아메리카노를 주문하셨습니다.
가격은 3800원 입니다.''')
        americano.reduce()
    elif menu==2:
        if moca.getQuantity()==0:
            print('카페모카를 주문하셨습니다.')
        else:
            print('''카페모카를 주문하셨습니다.
가격은 4500원입니다.''')
        moca.reduce()
    elif menu==3:
        if greentea.getQuantity()==0:
            print('그린티라떼를 주문하셨습니다.')
        else:
            print('''그린티라떼를 주문하셨습니다.
가격은 5000원입니다.''')
        greentea.reduce()
    elif menu==4:
        break


