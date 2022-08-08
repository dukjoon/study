import string

def validate_name(name):
    
    # name이 문자열인지 확인합니다.
    if type(name) is not str:
        return False
    
    # name이 숫자를 포함하는지 확인합니다.
    for digit in string.digits:
        if digit in name:
            return False
    
    # name이 특수기호를 포함하는지 확인합니다.
    for punctuation in string.punctuation:
        if punctuation in name:
            return False
    
    return True

print(validate_name("엘리스"))
