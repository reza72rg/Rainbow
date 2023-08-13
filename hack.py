import hashlib
import csv
with open('D:/python/test.txt') as f:
    read=csv.reader(f)
    people=list()
    dic_people,dic_pass=dict(),dict()
    for i in read:
        dic_people[i[1]]=i[0]
    for i in range(10000):
        number=str(i).zfill(4)
        number=number.encode()
        hash_password=hashlib.sha256(number).hexdigest()
        dic_pass[hash_password]=i
    for i in dic_people:
        if i in dic_pass:
            print(f'{dic_people[i]},{dic_pass[i]}')
            
   


