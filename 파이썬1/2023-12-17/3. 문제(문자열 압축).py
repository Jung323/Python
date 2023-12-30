# 문자열 압축 : 주어진 문자열을 압축하는 함수를 작성하시오
# 압축 규칙은 다음과 같습니다.
# aaabbbb는 a3b4로 압축됩니다.
# abcde는 abcde(압축되지 않음)




# 연속되지 않아도 압축

def compress_string(word):
    word_list = []
    word_dict = {}
    compressed_str = ''
    for i in range(len(word)):
        if word[i] not in word_list:
            word_list.append(word[i])
            word_list.sort()
            word_dict[word[i]] = str(word.count(word[i]))
    for alphabet,count in word_dict.items():
        if count == '1':
            s = alphabet
            compressed_str += s
        else:
            s = alphabet + count
            compressed_str += s
    return compressed_str

compressed_str = compress_string('aaabbb')
print(compressed_str) #결과: "a3b4"

compressed_str = compress_string('abcde')
print(compressed_str) #결과: "abcde"

compressed_str = compress_string('ababaabb')
print(compressed_str) #결과: "a4b4"


print()


# 연속된 문자만 압축
def compress_string(s):
    if not s:
        return ''

    compressed = []
    count = 1

    for i in range(1,len(s)):
        # 현재 문자가 이전 문자와 같은 경우 카운트 추가
        if s[i] == s[i-1]:
            count += 1
        else:
            # 현재 문자가 이전 문자와 다른 경우
            # 연속된 개수가 1보다 큰 경우 숫자를 추가하여 압축 문자열에 추가
            compressed.append(s[i-1] + (str(count) if count > 1 else ''))
            # 카운트 초기화
            count = 1
    # 마지막 문자 처리
    compressed.append(s[-1] + (str(count) if count > 1 else ''))

    compressed_str = ''.join(compressed)
    return compressed_str


compressed_str = compress_string('aaabbb')
print(compressed_str) #결과: "a3b4"

compressed_str = compress_string('abcde')
print(compressed_str) #결과: "abcde"

compressed_str = compress_string('ababaabb')
print(compressed_str) #결과: "ababa2b2"

print()

def compress_string(s):
    if not s:
        return ''

    compressed = []
    count = 1

    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            if count > 1:
                compressed.append(s[i-1] + str(count))
                count = 1
            else:
                compressed.append(s[i-1])
                count = 1
    compressed.append(s[-1] + (str(count) if count > 1 else ''))
    compressed_str = ''.join(compressed)
    return compressed_str


compressed_str = compress_string('aaabbb')
print(compressed_str) #결과: "a3b4"

compressed_str = compress_string('abcde')
print(compressed_str) #결과: "abcde"

compressed_str = compress_string('ababaabb')
print(compressed_str) #결과: "ababa2b2"


