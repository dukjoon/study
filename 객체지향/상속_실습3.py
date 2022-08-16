class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.shared_users = []
        self.is_private = False

    def share(self, user):
        self.shared_users.append(user)
        

class PrivatePost(Post):
    # 생성자를 구현합니다.
    # is_private 속성을 True 로 설정합니다.
    def __init__(self, author, content):
        super().__init__(author, content)
        self.is_private = True
    
    # share 메소드를 호출 시 TypeError를 발생시킵니다.
    def share(self, user):
        if self.is_private is True:
            raise TypeError("private 게시물 입니다.")
