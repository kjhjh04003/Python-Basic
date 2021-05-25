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

import pickle
def pickle_dump():
    with open("./sample/player.bin", "wb") as f: # 자원 자동 정리, pickle을 사용하려면 바이너리 모드
        data = {"baseball": 9}
        pickle.dump(data, f) # 데이터 보완X
    print("덤프 완료!")

def pickle_load():
    # 객체 역직렬화 : 2진 데이터 -> 파이썬 객체로 복원하는 작업
    with open("./sample/player.bin", "rb") as f:
        data = pickle.load(f)
        print(data, type(data))
    print("로드 완료!")

def pickle_dump_multi():
    # dump 메서드를 중복 실행하면 여러 객체를 dump 할 수 있다.
    with open("./sample/players.bin", "wb") as f:
        pickle.dump({"baseball": 9}, f, 1) # 프로토콜의 버전 명시 가능
        pickle.dump({"basketball": 5}, f, pickle.HIGHEST_PROTOCOL) # 가장 최신 버전의 프로토코로 사용
        pickle.dump({"soccor": 11}, f)
    print("중복값 덤프 완료!")

def pickle_load_multi():
    # 파일 내부에 몇 개의 파일 객체가 저장되어 있는지 확인 어렵다
    with open("./sample/players.bin", "rb") as f:
        # print(pickle.load(f))
        # print(pickle.load(f))
        # print(pickle.load(f)) # EOF
        # print(pickle.load(f)) # EOFERROR 발생

        # EOF 에러가 발생할 때까지 loop를 돌면서 load
        data_list = []
        while True:
            try:
                data = pickle.load(f)
            except EOFError: # 더 이상 읽을 피클이 없다.
                break
            data_list.append(data)
        print(data_list)

def slamdunk_read():
    # sangbuk.csv를 한 줄 단위로 읽는다.
    # 읽은 것 dict 시키고 list에 적재
    # pickle에 덤프
    players = []
    with open("./sample/sangbuk.csv", "rt", encoding="UTF-8") as f:
        while True:
            line = f.readline()
            if not line: # 읽을 데이터가 없으면
                break
            # 읽은 데이터를 사전화
            # 정제
            line = line.strip().replace(" ", "")
            info = line.split(",")
            print(info)
            member = {"name": info[0], "backno": info[1], "height": info[2], "position": info[3]}
            players.append(member)
    print(players)
    # pickle에 덤프
    with open("./sample/sangbuk_players.bin", "wb") as f:
        pickle.dump(players, f)
    print("피클 덤프 완료!")

if __name__ == "__main__":
    # write01()
    # write02()
    # read01()
    # read02()
    # read03()
    # copy_binary()
    # pickle_dump()
    # pickle_load()
    # pickle_dump_multi()
    # pickle_load_multi()
    slamdunk_read()