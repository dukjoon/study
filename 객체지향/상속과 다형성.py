# 클래스의 상속: 여러 클래스가 비슷한 속성과 메소드를 공유해야 할 때
# 계층, 형제관계가 확실할 때 상속이 필요


#부모 클래스
from tkinter import Image


class Post:
    def like(self, user):
            self.likers.append(user)
    def __init__(self, content): #생성자
        self.content = content

        self.likers = []


#자식 클래스
class ImagePost(Post):
    def __init__(self, content, images):
        super().__init__(content) #super(): 파이썬의 기본 함수, 부모 클래스에 접근할 때 사용
        #상위 클래스에 접근, ImagePost라는 인스턴스가 생기는데 이때 Post도 생성됨

        self.images = images
my_post = ImagePost(alice, "#강남맛집")
my_post.like(bob)
print(my_post.likers) #[]

