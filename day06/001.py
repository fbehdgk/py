#primitive타입(원시타입)8개 -> 확장은 import : 원하는 타입을 가져올 수 있다
#값1개(값의 종류) : int float str bool
    # 숫자 -> 정수(int), 실수(float)
    # 문자열 -> str
    # 참거짓 -> bool
#sequence
    #순서대로 읽고쓴다    # list  [1,2,3] # 리스트나 튜플은 운이좋으면 (찾는게 앞에 있으면) 빠르다
                        # tuple (1,2,3) #읽기전용
    #계산을 통해 위치를 파악한다   # set   {1,2,3} # 리스트나 튜플에 비해 속도가 빠르다 (계산에 의해서 위치가 지정된다)
    #키와 값의 쌍(pair) :  dictionary #{'홍길동':175,'길':15,'동':1,} 단점 : 데이터의 길이가 길어진다