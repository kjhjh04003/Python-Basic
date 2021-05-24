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

if __name__ == "__main__":
    # quiz01()
    # quiz02()
    quiz03()