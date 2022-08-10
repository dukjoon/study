class Post:

    # 생성자는 매개변수로 작성자와 내용을 받아,
    # 그 값을 속성에 저장합니다.
    def __init__(self, author, content):
        
        # 속성들을 초기화합니다.
        self.author = author
        self.content = content

my_post = Post("elice", 1457)
my_post.like(["Hello","World"])

class User:
    def __init__(self, year_of_birth):
        if type(year_of_birth) is not int:
            return

class Post:
    def __init__(self,author,content):
        if not isinstance(author, User):
            return
        if type(content) is not str: #type 비교시에는 is를 사용
            return

class Person:
    def __init__(self, year_of_birth):
        if year_of_birth > 2005:
            raise Exception("Too young") #raise: 에러 발생 시키기
    

