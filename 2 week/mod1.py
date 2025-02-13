def add(a,b) :
    return a + b
def sub(a,b) :
    return a - b
print(add(1,4))
print(sub(4,2))
print(__name__)
if __name__ == ' __main__' :
    print('파일 실행')
else :
    print('모듈로 임포트')
print(__name__)