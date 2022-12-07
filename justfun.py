# 입력 받기
txt = input('공백 5개 이상 문자열 입력: ')


# 1. 문자열 단어 수 세기
print('1. 문자열 단어 수 세기')
print(len(txt.split(' ')))
print('')


# 2. 문자열 역순
print('2. 문자열 역순')
print(txt[::-1])
print('')


# 3. 문자열에서 공백 문자 삭제
print('3. 문자열에서 공백 문자 삭제')
none_empty = txt.replace(' ', '')
print(none_empty)
print('')


# 4. 문자열에서 다시 공백 첨가
print('# 4. 문자열에서 다시 공백 첨가')
add_empty = list(none_empty)

re_ = -1
for i in range(txt.count(' ')):
    re_ = txt.index(' ', re_ + 1)
    add_empty.insert(re_, ' ')
    
add_empty = ''.join(add_empty)
print(add_empty)
print('')


# 5. 문자열 단어 발생 빈도
print('5. 문자열 단어 발생 빈도')
frequency = dict()


for word in txt.split(' '):
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
        
word = list(frequency.keys())
f = list(frequency.values())

while bool(word):
    m = min(f)
    print(word.pop(f.index(m)))
    f.remove(m)
print('')