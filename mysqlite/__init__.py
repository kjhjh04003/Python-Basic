from .database import *
# __init__.py
# 패키지 import 할 때 초기화 작업을 수행하는 파일
# 패키지를 만들려면 __init__.py가 있어야 패키지로 인식되지만
# 3.x에서부터는 없어도 패키지로 인식

# from 패키지 import * : 내부에 있는 모든 객체를 import
__all__ = ["Database"] # 명시된 심볼(객체)만 export된다.
# __all__ = [] # *로 임포트시 아무 것도export 안한다.
