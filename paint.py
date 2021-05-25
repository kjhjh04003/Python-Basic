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

if __name__ == "__main__":
    # bound_class_mathod()
    # unbound_class_method()
    class_member_test()