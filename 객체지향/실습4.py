import string

def encode_char(char):
    if char in string.ascii_lowercase:
        return chr(ord('z') - ord(char) + ord('a'))
    if char in string.ascii_uppercase:
        return chr(ord('Z') - ord(char) + ord('A'))
    return char


def decode_char(char):
    if char in string.ascii_lowercase:
        return chr(ord('z') - ord(char) + ord('a'))
    if char in string.ascii_uppercase:
        return chr(ord('Z') - ord(char) + ord('A'))
    return char


def reverse_string(string):
    return ''.join(reversed(string))


def encode(password):
    
    # 문자열을 뒤집습니다.
    reversed_password = reverse_string(password)
    
    # 각 글자를 암호화하여 이어 붙입니다.
    encoded = ""
    for char in reversed_password:
        encoded += encode_char(char)
    
    # 맨 끝에 암호화된 문자열의 길이의 일의 자리 숫자를 붙입니다.
    result = encoded + str(len(encoded) % 10)
    
    return result


def decode(encoded_password):
    
    # 맨 끝에 붙은 수를 제거합니다.
    number_stripped = encoded_password[:-1]

    # 각 글자를 복호화하여 이어 붙입니다.
    decoded = ""
    for char in number_stripped:
        decoded += decode_char(char)
    
    # 문자열을 뒤집습니다.
    result = reverse_string(decoded)
    
    return result
