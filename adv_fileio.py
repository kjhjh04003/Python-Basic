# 파일 모드
# action: r(읽기:default), w(쓰기), a(추가)
# type : t(텍스트:default), b(바이너리)

def write01():
    f = open("./sample/test.txt", "w", encoding="UTF-8") # wirte text
    write_size = f.write("Life is too short, you need Python")
    print(write_size)
    f.close()

def write02():
    f = open("./sample/multilines.txt", "w", encoding="UTF-8")
    for i in range(10):
        f.write("Line %d\n" % i)
    f.close()

def read01():
    f = open("./sample/multilines.txt", "r", encoding="UTF-8")
    text = f.read()
    print(text)
    f.close()

def read02():
    # readline 메서드를 이용하면 한 줄 단위로 읽을 수 있다.
    f = open("./sample/multilines.txt", "r", encoding="UTF-8")
    while True:
        line = f.readline() # 한 줄 읽기
        if not line: # 더 읽을 내용이 없다면
            break
        print(line)
    f.close()
    # 읽고자 하는 파일 사이즈가 크다면

def read03():
    # readline 메서드를 이용하면 모든 라인을 불러 리스트로 변환 제공
    f = open("./sample/multilines.txt", "r", encoding="UTF-8")
    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()

def copy_binary():
    # binary 파일을 다루려면 모드에 'b'를 붙여 바이너리로 설정
    # rose-flower.jpeg 파일 -> rose-flower-copy.jpeg로 복사
    f_src = open("./sample/rose-flower.jpeg", "rb")
    data = f_src.read()
    print(type(data))
    f_src.close()

    f_dest = open("./sample/rose-flower-copy.jpeg", "wb")
    f_dest.write(data)
    f_dest.close()

if __name__ == "__main__":
    # write01()
    # write02()
    # read01()
    # read02()
    # read03()
    copy_binary()