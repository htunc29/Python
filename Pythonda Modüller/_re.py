import re
str ="Python Kursu:Python Programlama Rehberiniz | 40 saat"

# result=re.findall("Python",str)
# result=re.split(" ",str)
# result=re.sub("\s","-",str)
# result=re.search("Python",str)
# result=result.string
# result=re.findall("[abc]",str)
# result=re.findall("[saat]",str)
# result=re.findall("[a-z]",str)
# result=re.findall("[0-5]",str)
# result=re.findall("[^abc]",str)
# result=re.findall("...",str)
# result=re.findall("Py..on",str)
# result=re.findall("^K",str)
# result=re.findall("t$",str)
result=re.findall("sa*t",str)
print(result)