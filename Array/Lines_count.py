f=open("D:/Python Code Practice/Python-Practice/file.txt","r")
#print(f.readlines())
line_count=0
for i in f:
    print(i)
    line_count+=1
print(line_count)
f.close()
f=open("D:/Python Code Practice/Python-Practice/file.txt","r")
w_cnt=0
w=[]
for i in f:
    w=i.split(" ")
    print(w)
    for i in w:
        w_cnt+=1
        w.append(i)
print(w)
print("word count", w_cnt)
print("word count", len(w))
f.close()

f=open("D:/Python Code Practice/Python-Practice/file.txt","r")

c_cnt=0
for i in f:
    for j in i:
        c_cnt+=1
print("Character Count",c_cnt)

f.close()