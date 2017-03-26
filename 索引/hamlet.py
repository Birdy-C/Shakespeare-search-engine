#words.py
# a hamlet.txt file is also included.
hamletf = input("Input the file to analyze: ")
txt = open(hamletf, "r").read()

txt = txt.lower()
for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
    txt = txt.replace(ch, " ")


words = txt.split()
#如何去掉无用的词---停用词,去掉停用词
stop=["the","and","to","of","you","a","i","my","in"]
words=[word for word in words if word not in stop]

counts = {}
for w in words:
    counts[w] = counts.get(w,0) + 1

items = list(counts.items()) #需要加list

#print(items[:20])
items.sort(key=lambda x:x[1], reverse=True)
for i in range(len(items)-1,len(items)-10,-1):  #如何显示"大"词?
    word, count = items[i]
    print (word, count)

f=open("hamletdic.txt","w")
for dic in items:
    f.write(str(dic)+'\n')
f.close()
