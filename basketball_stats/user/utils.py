# 유효성 검사
import re

def idCheck(id):
    # 영문으로 시작, 5~15자 길이
    print('형식 검사할 아이디: ', id)
    ID_regex = re.compile("([A-za-z]{5,15})")
    ID_validation = ID_regex.search(id.replace(" ",""))
    
    if ID_validation:
        return True
    else:
        return False

def passwordCheck(password):
    
    if len(password) < 7 or len(password) > 21 and not re.findall('[0-9]+', password) and not \
    re.findall('[a-z]', password):
        print('비밀번호 기준(숫자, 영문 대소문자 구성)에 맞지 않습니다.')
        return False

    elif not re.findall('[`~!@#$%^&*(),<.>/?]+', password):
        print('비밀번호는 최소 1개 이상의 특수문자가 포함되어야 함')
        return False

    print('비밀번호의 길이, 숫자, 영문자 등 유효함!!')
    return True
