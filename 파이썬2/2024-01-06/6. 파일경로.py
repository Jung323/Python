# 변수는 프로그램을 실행할 때 데이터를 저장하기 좋은 방법이다.
# 그러나 프로그램을 종료한 후에도 데이터를 유지하고 싶으면, 파일 형태로 저장해야 한다.

# 1. 파일과 파일경로
# 파일에는 파일 이름과 경로라는 두가지 주요 속성이 있다.
# C:\python_주말반 이라는 경로에 1. 변수.py 라는 이름의 파일이 있는 경우
# python_주말반 폴더 안에는 파일이나 다른 폴더가 들어 있을 수 있다.

# 경로의 C:\는 루트 폴더를 나타내며 모든 폴더가 이 안에 있다.
# 윈도우에서 루트 폴더의 이름은 "C:\"이며 C드라이브라고 부른다.
# 맥 OS나 리눅스에서 루트 폴더는 '\'이다.
# 윈도우, 맥 OS 에서는 폴더이름이나 파일이름의 대소문자를 구분하지 않지만, 리눅스는 구분한다.


# 윈도우에서 폴더 구분은 '\'(백슬러시)를 사용하고, 맥 OS나 리눅스에서는 '/'(슬러시)를 사용함.
# 프로그램의 모든 운영체제에서 작동하게 하려면 '\','/' 두가지 경우를 모두 처리하도록 스크립트를 작성하는 것이 좋다.

from pathlib import Path
import platform

print(Path.cwd()) # 현재 파이썬이 실행되는 경로를 알려준다.

my_os = platform.system()
print('OS가 무엇인가?: ',my_os) #결과: OS가 무엇인가?:  Windows
if my_os == 'Windows':
    print('Windows 운영체제입니다.')
else:
    print('Windows 운영체제가 아닙니다.')

# 절대 경로와 상대 경로
# 절대 경로 : 항상 루트 폴더에서 시작하는 경로
# 상대 경로 : 현재 작업 디렉토리에 대한 경로

# 새로운 디렉토리 만들기
# os.makedirs() 함수로 새로운 디렉토리(폴더)를 만들 수 있다.
# os.path.isdir(path) : path의 디렉토리가 있는지 확인

# '.' : 현재 디렉토리
# '..' : 상위 디렉토리
# '...' : 상위 디렉토리의 상위 디렉토리

import os

path = './input'
if not os.path.isdir(path):
    os.makedirs(path) #현재 작업 디렉토리에 input이라는 폴더를 생성


# 파일 크기와 폴더 내용 확인하기
# os.path.getsize(path) : path 인자에 해당되는 파일 크기를 바이트(byte)단위로 반환
# os.listdir(path) : path에 있는 파일 이름 리스트로 반환

print(os.path.getsize(path))
print(os.listdir(path))