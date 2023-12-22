for i in range(1,205):
    file = open('train ('+str(i)+').txt', 'r')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
    data = file.read()
    for j in range(1,8):
        file_copy = open('train ('+str(i)+'-'+str(j)+').txt', 'w')
        file_copy.write(data)
        file_copy.close()
    file.close()                     # 파일 객체 닫기