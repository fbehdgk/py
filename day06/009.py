#dictionary : 키(값의 이름)와 값의 쌍
ice={'바밤바' : 1000,'옥동자' : 1200,'월드콘' : 2000,}

#자바스크립트의 json
#{'바밤바' : '1000','옥동자' : '1200','월드콘' : '2000',}
print(ice)
print(ice["바밤바"])
print(ice["월드콘"])
#create
ice["빵빠레"]=1500
print(ice)
#update
ice["빵빠레"]=1800
print(ice)
#delete
del ice["빵빠레"]
print(ice)