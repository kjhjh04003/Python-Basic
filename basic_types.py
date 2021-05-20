# 기본적인 타입
def bool_ex(): # bool 자료형
    print("==== bool연습 ====")
    # 참(true), 거짓(false)
    # 내부적으로 거짓은 0, 나머지는 모두 참으로 판단
    # bool의 판정 방법
    print(bool(0), bool(1))
    a = 1
    print(a > 10) # 논리 연산 or 비교 연산의 결과

    b = a == 1 # b는 논리 연산의 결과가 저장
    print(b, type(b))

    print(b + 10)

    # bool은 bool의 객체인가?
    print(isinstance(True, bool)) # True is bool? -> int 객체를 상속받아 bool을 만든 것
    print(isinstance(True, int)) # True is int?

    # bool 캐스팅
    print("정수형", bool(10), bool(0))
    print("실수형", bool(3.14), bool(0.0)) # 실수형이더라도 3.14는 값이 있는 것으로 판단하여 true, 0.0은 값이 없는 것으로 판단하여 false
    print("문자열", bool("Pythoe"), bool("")) # 문자열이 있으면 값이 있는 것으로 판단하여 true, 빈값은 값이 없는 것으로 판단하여 false
    print("순차형", bool([1, 2, 3]), bool([]))
    print("Map형", bool({"a":2}), bool({}))
    print("None", bool(None)) # None 자료형은 자바의 Null과 비슷한 의미로 그 존재만으로 false


if __name__ == "__main__":
    bool_ex()