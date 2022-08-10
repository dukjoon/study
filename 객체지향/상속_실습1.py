from utils import go_to

class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content


# 아래에 LinkPost를 선언합니다.
class LinkPost(Post):
    def __init__(self, author, content, url):
        super().__init__(author,content)
        
        valid_url = url.startswith("http://") or url.startswith("https://") #boolean 값. (T or F)
        if not valid_url:
            raise ValueError("올바르지 않은 주소 형식입니다.")

        self.url = url

    def on_click(self):
        go_to(self.url)

post = LinkPost("elice", "hello", "http://academy.elice.io")
post.onclick()
print(post.url)