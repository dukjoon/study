from validators import validate_email

class User:
    
    def __init__(self,email,password,name,gender):
        if not isinstance(email, password, name, gender):
            return
    
        # 이메일이 형식에 맞는지 확인하고, 설정합니다.
        self.email = email
        if validate_email(email) is False:
            return
        
        # 비밀번호가 조건을 만족하는지 확인하고, 설정합니다.
        self.password = password
        if len(password) < 8:
            raise Exception("Value Error")
        
        # 사용자의 이름이 조건을 만족하는지 확인하고, 설정합니다.
        self.name = name
        if name in " ":
            raise Exception("Value Error")
        
        # 성별이 조건을 만족하는지 확인하고, 설정합니다.
        self.gender = gender
        if gender != "M":
            raise Exception("Value Error")
        elif gender != "F":
            raise Exception("Value Error")
        elif gender != "O":
            raise Exception("Value Error")
        
        # 친구 목록을 설정합니다.
        self.friends = []
