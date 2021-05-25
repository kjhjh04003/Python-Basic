# 테스트 코드
from point import Point

def bound_class_mathod():
    # 직접 인스턴스 명시 -> 멤버에 접근
    p = Point() # Point() 인스턴스 생성
    p.setX(10)
    p.setY(20)
    print(p.getX(), p.getY(), sep=",")
    print(p.getX, p.getY) # 메서드 객체 자체를 출력
                          # getX, getY가 bound method로 실행됨을 확인

def unbound_class_method():
    # 클래스에 인스턴스를 전달해서 인스턴스 내부의 메서드 호출
    p = Point() # Point() 인스턴스 생성
    Point.setX(p, 10)
    Point.setY(p, 20)
    print(Point.getX(p), Point.getY(p))
    print(Point.getX, Point.getY) # 메서드 객체 자체를 출력
                                  # Point class 내의 함수로 실행됨을 확인

def class_member_test():
    p1 = Point()
    p1.setX(10)
    p1.setY(20)

    print("p1 : {}, {}".format(p1.getX(), p1.getY()))
    print("instance_count : ", p1.instance_count, # 클래스 멤버는 인스턴스에서 접근 가능
    Point.instance_count) # 인스턴스 없이도 접근 가능

def test_lifecycle():
    p1 = Point(10, 20) # 생성자 사용
    print("instance count : ", Point.instance_count)

    p2 = Point() # 기본 값 사용
    print("instance count : ", Point.instance_count)

    print(p1, p2)

def test_print():
    p1 = Point(10, 10)
    print("p1:", p1) # __str__ 호출

    # __str__ : 일반 사용자가 보기 쉽게 출력하는 포맷
    # __repr__: 개발자가 객체 복원하기 위해 출력하는 포맷

    print(repr(p1)) # __repr__ 호출
    p2 = eval(repr(p1)) # __repr__ 출력 포맷으로 객체 복원
    print("p2:", p2, type(p2))

def arith_oper_overriding():
    p1 = Point(10, 20)
    p2 = Point(30, 40)

    # print(dir(object)) # __eq__, __ge__ 확인
    # Point + Point
    print(p1 + p2) # TypeError 오류난다. +연산자가 Point and Point를 할 수 없다는 것이다.

    # Point + int
    p1 = Point(10, 20)
    print(p1 + 10)

    # int + Point
    p1 = Point(10, 20)
    print(10 + p1) # TypeError 오류난다. + 연산자가 int and Point를 할 수 없다는 것이다.

    # # 연습문제
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    print(p1 - p2)
    p1 = Point(10, 20)
    print(p1 - 10)

    p1 = Point(10, 20)
    p2 = Point(10, 20)
    print("p1==p2?", p1==p2)

if __name__ == "__main__":
    # bound_class_mathod()
    # unbound_class_method()
    # class_member_test()
    # test_lifecycle()
    # test_print()
    arith_oper_overriding()
