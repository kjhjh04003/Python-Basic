# if and loop
# 1. 키보드로부터 score1, score2를 입력받아 조건에 부합하면 '합격', 아니면 '불합격'을 출력
# 조건1 : 두 과목 모두 50점 이상
# 조건2 : 두 과목 평균 60점 이상
def quiz01():
    sub1 = int(input("점수 입력> "))
    sub2 = int(input("점수 입력> "))
    avg = (sub1 + sub2)/2

    if sub1 >= 50 and sub2 >= 50 and avg >= 60:
        print("합격")
    else:
        print("불합격")

# 2. 구구단 만들기
def quiz02():
    for i in range(1, 10):
        print(i, "단")
        for j in range(1, 10):
            print(i,"*",j,"=", i*j)

# 3. 무한 루프 작성
# 키보드로부터 입력을 받는다.
# 입력값이 q면 루프를 탈출한다.
# 입력값이 d, w면 금액을 입력받는다.
# q, d, w이외의 값이면 ?를 출력한다.
# 금액을 총액에 합산(d)혹은 차감(w)한다.
def quiz03():
    while True:
        inputs = str(input("method: "))

        if inputs == "d":
            amount = int(input("Amount: "))
            balance = int(input("Balance: "))
        elif inputs == "w":
            amount = int(input("Amount: "))
            balance = int(input("Balance: "))
        elif inputs == "q":
            break
        else:
            print("?")

def q1():
    score1 = int(input("점수1 : "))
    score2 = int(input("점수2 : "))

    avg = (score1 + score2) / 2

    if score1 >= 50 and score2 >= 50 and avg >= 60:
        message = "합격"
    else:
        message = "불합격"
    print(message)

def q2():
    for dan in range(2, 10): # 2 ~ 9단 반복
        print(dan, "단")
        for num in range(1, 10): # 1 ~ 9 반복
            print("{} x {} = {}".format(dan, num, dan*num))

def q3():
    # continue, break 문 사용
    balance = 0 # 잔액
    while True: # 무한루프
        method = input("method : ")
        method = method.lower()

        if method == "q":
            break # 루프 종료

        if method != "d" and method != "w":
            print("?")
            continue

        # d, w 남음
        # 금액 입력
        amount = int(input("Amount : "))
        balance += amount if method == "d" else - amount
        # if method == "d": # 입금
            # balance += amount
        # else: # 출금
            # balance -= amount
        print("Balance : ", balance)
    print("프로그램 종료")

if __name__ == "__main__":
    # quiz01()
    # quiz02()
    # quiz03()
    # q1()
    # q2()
    q3()